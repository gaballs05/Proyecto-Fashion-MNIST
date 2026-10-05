from pathlib import Path
import gzip
import urllib.request
import numpy as np
from PIL import Image, ImageOps

CLASES = ['camiseta', 'pantalon', 'sueter', 'vestido', 'abrigo',
          'sandalia', 'camisa', 'tenis', 'bolsa', 'botin']
BASE = 'https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/data/fashion/'


def leer_idx(ruta, imagen):
    # comprobamos el encabezado para detectar descargas incorrectas
    with gzip.open(ruta, 'rb') as archivo:
        contenido = archivo.read()
    cabecera = np.frombuffer(contenido[:16 if imagen else 8], dtype='>u4')
    esperado = 2051 if imagen else 2049
    if cabecera[0] != esperado:
        raise ValueError(f'archivo idx incorrecto: {ruta}')
    datos = np.frombuffer(contenido[16 if imagen else 8:], dtype=np.uint8)
    forma = (int(cabecera[1]), int(cabecera[2]), int(cabecera[3])) if imagen else (int(cabecera[1]),)
    return datos.reshape(forma).copy()


def cargar_datos(carpeta='data'):
    carpeta = Path(carpeta)
    carpeta.mkdir(exist_ok=True)
    nombres = ['train-images-idx3-ubyte.gz', 'train-labels-idx1-ubyte.gz',
               't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz']
    resultado = []
    for i, nombre in enumerate(nombres):
        destino = carpeta / nombre
        if not destino.exists():
            temporal = destino.with_suffix('.part')
            try:
                urllib.request.urlretrieve(BASE + nombre, temporal)
                temporal.replace(destino)
            finally:
                temporal.unlink(missing_ok=True)
        resultado.append(leer_idx(destino, imagen=i % 2 == 0))
    return tuple(resultado)


def preparar_foto(ruta):
    # el borde nos da una estimacion sencilla del fondo
    with Image.open(ruta) as original:
        gris = np.array(ImageOps.exif_transpose(original).convert('L'), dtype=np.float32)
    borde = np.concatenate([gris[0], gris[-1], gris[:, 0], gris[:, -1]])
    objeto = np.abs(gris - np.median(borde))
    maximo = objeto.max()
    if maximo < 15:
        raise ValueError(f'foto sin contraste suficiente: {ruta}')
    objeto = objeto / maximo
    ys, xs = np.where(objeto > 0.15)
    recorte = objeto[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    imagen = Image.fromarray((recorte * 255).astype('uint8'))
    imagen.thumbnail((20, 20), Image.Resampling.LANCZOS)
    lienzo = Image.new('L', (28, 28), 0)
    lienzo.paste(imagen, ((28 - imagen.width) // 2, (28 - imagen.height) // 2))
    return np.asarray(lienzo, dtype=np.float32) / 255.0
