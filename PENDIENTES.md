# Estado del Proyecto y Bitacora de Entrega

## Estado general: Implementacion y pruebas completadas (100%)

Todas las tareas tecnicas, de modelado, evaluacion externa y documentacion han sido implementadas y verificadas con salidas reales reproducibles.

---

## Implementado y verificado

- [x] **Entorno y dependencias:** Entorno virtual `.venv` configurado con Python 3.12 y dependencias instaladas (`torch`, `scikit-learn`, `pandas`, `matplotlib`, `pillow`, `jupyter`, `pyarrow`).
- [x] **Carga y particion reproducible:** 54,000 entrenamiento, 6,000 validacion y 10,000 prueba oficial con semilla 42.
- [x] **Modelos clasicos guardados:** Regresion logistica, SVM, Random Forest y MLP entrenados y guardados con `joblib` en `resultados/modelos_clasicos.joblib` para evitar reentrenamientos costosos.
- [x] **Advertencia de convergencia:** Registrada y documentada la advertencia de `ConvergenceWarning` de la regresion logistica al alcanzar 300 iteraciones.
- [x] **Evaluacion externa completa (30 imagenes):**
  - 30 imagenes seleccionadas (3 distintas por cada una de las 10 clases) de *Fashion Product Images (Small)* (MIT License).
  - Verificacion visual y distinciones criticas atendidas (camiseta vs camisa, sueter vs abrigo, botin vs tenis/sandalias).
  - Preprocesamiento verificado a 28 x 28 en escala de grises [0, 1] y grafica comparativa guardada en `resultados/verificacion_fotos_30.png`.
  - Archivos de procedencia creados: `fotos/procedencia.csv` y `fotos/PROCEDENCIA.md`.
  - Evaluacion ejecutada con los 5 modelos tradicionales y ambas CNNs; tablas guardadas en `resultados/predicciones_fotos.csv` y `resultados/comparacion_fotos.csv`.
- [x] **Mejora de la CNN:**
  - Experimentacion con variantes tecnicas guiadas unicamente por el conjunto de validacion (sin tocar prueba ni imagenes externas).
  - Variante 2 (Doble convolucion por bloque con `BatchNorm2d`, `Dropout` gradual y clasificador regularizado) supero a la referencia en validacion (93.95% vs 91.70%, perdida 0.1802 vs 0.2233).
  - Evaluada la variante final en la prueba oficial: **92.68% de accuracy** y **0.9270 de F1 macro**, superando el 90.32% inicial (+2.36%). Pesos guardados en `resultados/cnn_v2_dobleconv.pt`.
- [x] **Notebook ejecutado en orden:** `fashion_mnist.ipynb` ejecutado de principio a fin con graficas, tablas y matrices de confusion reales integradas.
- [x] **Material de exposicion actualizado:** `guion_exposicion.md` actualizado con los resultados reales de la CNN mejorada y la evaluacion de las 30 imagenes externas.
- [x] **Versionado en Git:** Rama `entrega` creada y lista para publicacion.

---

## Resultados cuantitativos consolidados

### 1. Conjunto oficial (10,000 imagenes de prueba)
| Modelo | Accuracy validacion | Accuracy prueba | F1 macro prueba |
|---|:---:|:---:|:---:|
| Regresion logistica | 86.30% | 84.28% | 0.8421 |
| SVM (RBF) | 90.98% | 89.59% | 0.8956 |
| Random Forest | 88.37% | 87.44% | 0.8730 |
| MLP | 89.20% | 88.18% | 0.8798 |
| CNN Inicial (baseline) | 91.70% | 90.32% | 0.9026 |
| **CNN Mejorada (doble conv + BN)** | **93.95%** | **92.68%** | **0.9270** |

### 2. Fotos externas (30 imagenes de internet)
| Modelo | Aciertos / 30 | Accuracy | F1 macro |
|---|:---:|:---:|:---:|
| Regresion logistica | 6 / 30 | 20.00% | 0.1483 |
| SVM | 5 / 30 | 16.67% | 0.1290 |
| Random Forest | 5 / 30 | 16.67% | 0.0769 |
| MLP | 8 / 30 | 26.67% | 0.1864 |
| CNN Inicial | 5 / 30 | 16.67% | 0.1017 |
| CNN Mejorada | 7 / 30 | 23.33% | 0.1191 |

---

## Pendientes especificos que dependen del estudiante o profesor

1. **Aceptacion de imagenes de internet:** La consigna original del laboratorio pedia fotografias propias tomadas con camara. Las 30 imagenes utilizadas provienen de un catalogo de internet con licencia MIT. El estudiante debe confirmar con el profesor si se acepta esta alternativa justificada o si requiere sustituirlas por fotos personales antes de la evaluacion presencial.
2. **Practica de la exposicion:** Ensayar el guion de presentacion de 5 a 10 minutos (`guion_exposicion.md`), enfocandose en la explicacion del preprocesamiento, por que falla la generalizacion en fotos de catalogo (domain shift y baja resolucion 28x28) y como influyo el uso de BatchNorm y regularizacion en la mejora de la CNN.
3. **Confirmacion de entrega en GitHub:** Verificar la visualizacion de la rama `entrega` o el Pull Request en https://github.com/gaballs05/Proyecto-Fashion-MNIST.
