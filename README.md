# Proyecto Fashion-MNIST
Gabriel Vallejo Castro y Javier Uc Ix · Laboratorio 2 · Aprendizaje maquina

Comparacion de regresion logistica, SVM, Random Forest, MLP de scikit-learn y CNN de PyTorch (version inicial y variante mejorada) en un notebook explicado paso a paso, complementado con una evaluacion extern de 30 imagenes.

---

## Guia rapida para ejecutar en cualquier PC (Presentacion del equipo)

Si vas a presentar o abrir el proyecto en tu computadora o en la laptop de un companero, sigue estos pasos sencillos:

### 1. Requisitos
- **Python 3.11 o 3.12** instalado en el sistema.
- Conexión a internet solo para la instalación inicial de librerías.

### 2. Pasos de instalacion y arranque

#### En Windows (PowerShell):
```powershell
# 1. Clonar el repositorio (o descomprimir el archivo ZIP) y entrar a la carpeta:
git clone https://github.com/gaballs05/Proyecto-Fashion-MNIST.git
cd Proyecto-Fashion-MNIST

# 2. Crear el entorno virtual:
python -m venv .venv

# 3. Activar el entorno virtual:
# (Si PowerShell da error de politicas de script, ejecutar primero: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass)
.\.venv\Scripts\activate

# 4. Instalar las dependencias del proyecto:
pip install -r requirements.txt

# 5. Abrir el notebook para la exposicion:
jupyter notebook fashion_mnist.ipynb
```

#### En macOS o Linux (Terminal):
```bash
# 1. Clonar y entrar a la carpeta:
git clone https://github.com/gaballs05/Proyecto-Fashion-MNIST.git
cd Proyecto-Fashion-MNIST

# 2. Crear y activar entorno virtual:
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependencias y abrir notebook:
pip install -r requirements.txt
jupyter notebook fashion_mnist.ipynb
```

> **NOTA CLAVE PARA LA PRESENTACION EN CLASE:**
> - El archivo [`fashion_mnist.ipynb`](fashion_mnist.ipynb) **ya viene 100% ejecutado** con todas las tablas, graficas y matrices de confusion guardadas. No es necesario volver a entrenar los modelos en vivo frente al profesor ni a los companeros.
> - Si durante la clase el profesor pide volver a ejecutar una celda o correr el notebook, tardara solo 2 o 3 segundos porque carga los modelos ya entrenados desde [`resultados/modelos_clasicos.joblib`](resultados/) y los pesos de la red convolucional.

---

## Evaluacion externa (30 imagenes)
Se incorporaron 30 imagenes externas (3 por categoria) almacenadas en `fotos/0` hasta `fotos/9`:

| Etiqueta | Clase | Carpeta | Ejemplos incluidos |
|---|---|---|---|
| 0 | camiseta / top | `fotos/0` | T-shirts casuales de cuello redondo (Puma, Inkfruit, Fila) |
| 1 | pantalon | `fotos/1` | Jeans y track pants largos (Peter England, Man. United, Jealous 21) |
| 2 | sueter / pullover | `fotos/2` | Sueteres y sudaderas cerradas (Benetton, Adidas) |
| 3 | vestido | `fotos/3` | Vestidos de una pieza (Arrow, Gini & Jony, Benetton) |
| 4 | abrigo | `fotos/4` | Blazers estructurados y chaquetas exteriores (Scullers, Forever New) |
| 5 | sandalia | `fotos/5` | Sandalias abiertas de tiras (Adidas, Ganuchi, Lotto) |
| 6 | camisa | `fotos/6` | Camisas abotonadas con solapa y cuello camisero (Turtle, Fabindia, Jealous 21) |
| 7 | tenis | `fotos/7` | Calzado deportivo y sneakers planos (Puma, Gas, Nike) |
| 8 | bolsa | `fotos/8` | Bolsas de mano y hombro estructuradas (Murcia, Baggit) |
| 9 | botin | `fotos/9` | Botines de cana corta al tobillo (Rockport, Timberland, Clarks) |

> **Nota importante sobre las fotos y su justificacion:**
> La consigna original del laboratorio sugeria tomar fotografias propias con camara.
> En este proyecto se utilizo una muestra curada de 30 imagenes de catalogo comercial con licencia abierta **MIT** (*Fashion Product Images (Small)* por Param Aggarwal).
> **Motivos de esta eleccion:**
> 1. Asegurar la correspondencia formal estricta de las 10 clases de Fashion-MNIST (diferenciar con exactitud camisa abotonada de camiseta, sueter cerrado de abrigo, y botines de zapatillas).
> 2. Disponer de fondos estandarizados para evaluar limpiamente el algoritmo de recorte y binarizacion.
> 3. Brindar total reproducibilidad cientifica con identificadores y licencia publica verificable en [`fotos/PROCEDENCIA.md`](fotos/PROCEDENCIA.md) y [`fotos/procedencia.csv`](fotos/procedencia.csv).
> Esta alternativa debe confirmarse con el profesor. Toda la tuberia esta modularizada en `datos.py`, por lo que reemplazar las imagenes por fotos personales es instantaneo si asi lo solicita el docente.

---

## Resultados en el dataset oficial (10,000 imagenes de prueba)

| Modelo | Accuracy validacion | Accuracy prueba | F1 macro prueba | Tiempo entrenamiento |
|---|---:|---:|---:|---:|
| Regresion logistica | 86.30% | 84.28% | 0.8421 | 16.0 s |
| SVM (kernel RBF, C=5) | 90.98% | 89.59% | 0.8956 | 179.1 s |
| Random Forest (100 arboles) | 88.37% | 87.44% | 0.8730 | 9.8 s |
| MLP (128, 64) | 89.20% | 88.18% | 0.8798 | 18.4 s |
| CNN Inicial (baseline) | 91.70% | 90.32% | 0.9026 | 61.8 s |
| **CNN Mejorada (doble conv + BN)** | **93.95%** | **92.68%** | **0.9270** | 150.0 s |

- **Modelo seleccionado por validacion:** `CNN Mejorada` (alcanzo 93.95% de accuracy en validacion y redujo la perdida a 0.1802). En la prueba oficial logro **92.68%**, superando en +2.36% a la CNN inicial.
- **Advertencia de convergencia:** La regresion logistica alcanzo el limite de 300 iteraciones y emitio una advertencia de convergencia (`ConvergenceWarning`), la cual se conserva y documenta como parte del comportamiento real del modelo lineal.

---

## Resultados en las 30 fotografias externas

| Modelo | Fotos evaluadas | Aciertos sobre 30 | Accuracy | F1 macro |
|---|---:|---:|---:|---:|
| Regresion logistica | 30 | 6 | 20.00% | 0.1483 |
| SVM | 30 | 5 | 16.67% | 0.1290 |
| Random Forest | 30 | 5 | 16.67% | 0.0769 |
| MLP | 30 | 8 | 26.67% | 0.1864 |
| CNN Inicial | 30 | 5 | 16.67% | 0.1017 |
| CNN Mejorada | 30 | 7 | 23.33% | 0.1191 |

### Observaciones de los errores en imagenes externas
1. **Diferencia de distribucion (Domain Shift):** El dataset oficial Fashion-MNIST tiene siluetas centradas y recortadas de forma muy uniforme. En fotos de catalogo, el preprocesamiento automatico produce siluetas continuas que los modelos confunden frecuentemente con vestidos (clase 3) o bolsas (clase 8).
2. **Ambiguedad de silueta a 28 x 28:** Camisas y camisetas, o sueteres y abrigos, comparten perfiles casi identicos al reducirse a 28 x 28 sin color, perdiendo botones y solapas.
3. **Muestra pequena:** 30 imagenes (3 por clase) representan una muestra pequena con alta sensibilidad estadistica (cada acierto representa 3.3% de accuracy). Su desempeno difiere significativamente del conjunto oficial de 10,000 imagenes.

---

## Estructura de archivos y material de exposicion
- `fashion_mnist.ipynb`: notebook ejecutable con todo el flujo y graficas reales.
- `guion_exposicion.md`: guion estructurado paso a paso para la exposicion de 5 a 10 minutos con respuestas preparadas a preguntas del profesor.
- `datos.py`: modulo de descarga, lectura IDX y preprocesamiento de imagenes.
- `fotos/`: 30 imagenes externas en carpetas `0/` a `9/`, con `procedencia.csv` y `PROCEDENCIA.md`.
- `resultados/`: tablas comparativas (CSV), graficas generadas, pesos de las redes (`.pt`), modelos clasicos (`.joblib`) y reportes de clasificacion.
- `PENDIENTES.md`: bitacora del proyecto y checklist de entrega.
