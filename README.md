# Proyecto Fashion-MNIST
Gabriel Vallejo Castro · Laboratorio 2 · Aprendizaje maquina

Comparacion de regresion logistica, SVM, Random Forest, MLP de scikit-learn y CNN de PyTorch (version inicial y variante mejorada) en un notebook explicado paso a paso, complementado con una evaluacion externa de 30 imagenes.

## Ejecutar el proyecto
Recomendado: Python 3.11 o 3.12. Desde la raiz del repositorio:

```bash
python -m venv .venv
```

En Windows: `.venv\Scripts\activate`. En macOS/Linux: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
jupyter notebook fashion_mnist.ipynb
```

Ejecutar todas las celdas en orden.
- El dataset oficial se incluye en `data/` para ejecucion sin conexion inmediata; si se elimina, `datos.py` lo descarga automaticamente de GitHub.
- Los modelos clasicos preentrenados estan guardados en `resultados/modelos_clasicos.joblib` y los pesos CNN en `resultados/cnn.pt` y `resultados/cnn_v2_dobleconv.pt`. Esto permite reproducir los resultados en pocos segundos sin necesidad de reentrenar.
- Si se desea reentrenar desde cero, basta con cambiar `REENTRENAR_TODO = True` en la celda 1 del notebook.
- `MODO_RAPIDO = True` permite verificar el flujo general en pocos segundos reduciendo el numero de muestras.

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

> **Nota importante sobre la entrega:**
> La consigna original pide tomar fotografias propias con camara.
> Estas 30 imagenes provienen del conjunto de datos publico *Fashion Product Images (Small)* (Param Aggarwal en Kaggle / Myntra) bajo licencia libre **MIT**.
> Constituyen una **alternativa estandarizada procedente de internet**, cuya validez en lugar de fotografias propias debe ser **confirmada por el estudiante con el profesor**.
> La procedencia completa, identificadores de origen, licencias y observaciones se detallan en [`fotos/PROCEDENCIA.md`](fotos/PROCEDENCIA.md) y [`fotos/procedencia.csv`](fotos/procedencia.csv).

## Resultados en el dataset oficial (10,000 imagenes de prueba)

| Modelo | Accuracy validacion | Accuracy prueba | F1 macro prueba | Tiempo entrenamiento |
|---|---:|---:|---:|---:|
| Regresion logistica | 86.30% | 84.28% | 0.8421 | 16.0 s |
| SVM (kernel RBF) | 90.98% | 89.59% | 0.8956 | 179.1 s |
| Random Forest (100 arboles) | 88.37% | 87.44% | 0.8730 | 9.8 s |
| MLP (128, 64) | 89.20% | 88.18% | 0.8798 | 18.4 s |
| CNN Inicial (baseline) | 91.70% | 90.32% | 0.9026 | 61.8 s |
| **CNN Mejorada (doble conv + BN)** | **93.95%** | **92.68%** | **0.9270** | 150.0 s |

- **Modelo seleccionado por validacion:** `CNN Mejorada` (alcanzo 93.95% de accuracy en validacion y redujo la perdida a 0.1802). En la prueba oficial logro **92.68%**, superando en +2.36% a la CNN inicial.
- **Advertencia de convergencia:** La regresion logistica alcanzo el limite de 300 iteraciones y emitio una advertencia de convergencia (`ConvergenceWarning`), la cual se conserva y documenta como parte del comportamiento del modelo lineal.

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

## Carga y uso de modelos guardados
```python
import joblib, torch
from datos import preparar_foto

# Cargar modelos clasicos
modelos = joblib.load('resultados/modelos_clasicos.joblib')
svm = modelos['svm']

# Cargar pesos de la CNN
# (Para arquitectura ver definicion CNN_Mejorada en fashion_mnist.ipynb)
# cnn_mejorada.load_state_dict(torch.load('resultados/cnn_v2_dobleconv.pt', weights_only=True))
```

## Estructura de archivos
- `fashion_mnist.ipynb`: notebook ejecutable con todo el flujo y graficas reales.
- `datos.py`: modulo de descarga, lectura IDX y preprocesamiento de imagenes.
- `fotos/`: 30 imagenes externas en carpetas `0/` a `9/`, con `procedencia.csv` y `PROCEDENCIA.md`.
- `resultados/`: tablas comparativas (CSV), graficas generadas, pesos de las redes (`.pt`), modelos clasicos (`.joblib`) y reportes de clasificacion.
- `guion_exposicion.md`: guion estructurado para la presentacion de 5 a 10 minutos.
- `PENDIENTES.md`: bitacora de estado y puntos a considerar por el estudiante.
