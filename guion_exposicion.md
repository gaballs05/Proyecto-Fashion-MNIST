# Guion de Exposicion (7 a 10 minutos)
**Proyecto Fashion-MNIST · Gabriel Vallejo Castro**

Este guion contiene la estructura minuto a minuto de la presentacion, notas defensivas sobre las fotos de internet y una guia paso a paso para que cualquier companero del equipo pueda abrir y ejecutar el proyecto en su computadora sin contratiempos.

---

## NOTA IMPORTANTE PARA EL EQUIPO: Justificacion de las fotos de internet

> ### ¿Como abordar el tema de las fotos de internet ante el profesor?
> La consigna original del laboratorio menciona tomar tres fotos por clase con camara propia. En nuestro proyecto utilizamos **30 imagenes de catalogo comercial abierto con licencia MIT** (*Fashion Product Images (Small)*).
>
> **Frase recomendada para decir en la presentacion:**
> > *"Profesor, respecto a las 30 imagenes de prueba externa, decidimos utilizar una muestra curada y reproducible de un catalogo abierto con licencia MIT. Esto nos permitio tres ventajas clave: primero, contar con ejemplos estrictamente correspondientes a las 10 categorias oficiales (diferenciando formalmente entre camisa abotonada y camiseta, sueter cerrado y abrigo, y botines frente a zapatillas); segundo, garantizar fondos claros y neutros para probar el algoritmo de recorte de forma estandarizada; y tercero, asegurar total trazabilidad y reproducibilidad cientifica con identificadores publicos. Reconocemos que la consigna sugeria fotos con camara propia, por lo que documentamos toda la procedencia en `fotos/PROCEDENCIA.md` para someter esta alternativa a su aprobacion."*
>
> **¿Que responder si el profesor insiste en que debian ser fotos propias?**
> > *"Comprendemos totalmente su punto, profesor. Toda la tuberia (`pipeline`) de preprocesamiento en `datos.py` y las carpetas `fotos/0/` a `fotos/9/` estan completamente modularizadas y listas. Si usted lo prefiere, podemos tomar 3 fotos en este momento con el celular, colocarlas en las carpetas y el notebook las recortara y clasificara automaticamente en menos de 5 segundos."*

---

## Guia de Ejecucion Rapida para el Companero de Equipo

Si tu companero va a proyectar desde su propia laptop durante la clase, solo debe seguir estos pasos:

### Opcion A: Usar el repositorio de GitHub (Recomendada)
1. Abrir una terminal (PowerShell en Windows, o Terminal en Mac/Linux).
2. Clonar y entrar a la carpeta:
   ```bash
   git clone https://github.com/gaballs05/Proyecto-Fashion-MNIST.git
   cd Proyecto-Fashion-MNIST
   ```
3. Crear el entorno virtual e instalar dependencias:
   - **En Windows:**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\activate
     python -m pip install -r requirements.txt
     ```
   - **En Mac / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     python3 -m pip install -r requirements.txt
     ```
4. Abrir el notebook para la clase:
   ```bash
   jupyter notebook fashion_mnist.ipynb
   ```

### Opcion B: Usar el archivo ZIP de entrega
1. Descomprimir `Proyecto-Fashion-MNIST-Entrega.zip`.
2. Abrir la terminal dentro de la carpeta descomprimida `Proyecto-Fashion-MNIST/`.
3. Activar el entorno e instalar dependencias con los comandos del paso 3.
4. Ejecutar `jupyter notebook fashion_mnist.ipynb`.

> **CONSEJO CLAVE PARA EXPONER:**
> El notebook en GitHub y en el ZIP **ya viene completamente ejecutado**. Todas las graficas, tablas y salidas ya estan renderizadas en pantalla. **No es necesario reentrenar nada en vivo** frente al grupo. Si el profesor pide correr una celda, tardara solo 2 o 3 segundos porque los modelos ya estan cargados en memoria y en disco.

---

## Estructura Minuto a Minuto de la Exposicion

### 1. Portada y Objetivo (1 minuto)
- **Que decir:**
  > "Buenas tardes profesor y companeros. Mi presentacion aborda la clasificacion automatica de prendas con el dataset Fashion-MNIST. Comparamos cinco familias de algoritmos: Regresion Logistica, SVM, Random Forest, Red Densa MLP y Red Convolucional CNN de PyTorch (tanto en su diseno base como en una version optimizada). Ademas, probamos su capacidad real de generalizacion ante 30 imagenes externas fuera de la distribucion de entrenamiento."
- **Diapositiva:** Titulo, objetivo y lista de los 5 algoritmos.

---

### 2. Dataset y Particion Metodologica (1.5 minutos)
- **Que decir:**
  > "Fashion-MNIST consta de 70,000 imagenes en escala de grises de 28 x 28 divididas en 10 clases de prendas. Dividimos entre 255 para normalizar al rango continuo [0, 1].
  > Desde el punto de vista metodologico, separamos las 60,000 imagenes iniciales en:
  > - 54,000 para entrenamiento.
  > - 6,000 para validacion (usadas exclusivamente para afinar hiperparametros y evitar fuga de informacion).
  > - 10,000 imagenes de prueba oficial, reservadas intactas para la medicion final."
- **Diapositiva:** Malla de 10 ejemplos con sus clases y diagrama de particion (54k train / 6k val / 10k test).

---

### 3. Modelos Tradicionales y Tiempos de Computo (1.5 minutos)
- **Que decir:**
  > "Entrenamos cuatro clasificadores tradicionales sobre las imagenes aplanadas a 784 caracteristicas:
  > - **Regresion Logistica:** Sirve como base lineal (84.28% de accuracy). Emitio una advertencia de convergencia (`ConvergenceWarning`) a las 300 iteraciones; la mantuvimos visible para evidenciar las limitaciones de optimizadores lineales en espacios de alta dimension.
  > - **Random Forest (100 arboles):** Logro 87.44% en solo 9.8 segundos.
  > - **MLP (128 y 64 neuronas):** Obtuvo 88.18% con parada temprana.
  > - **SVM con kernel RBF:** Fue el clasificador clasico mas preciso con 89.59%, pero demoro casi 3 minutos debido al calculo masivo de vectores de soporte."
- **Diapositiva:** Tabla comparativa de precision, F1 macro y tiempos de entrenamiento.

---

### 4. Red Convolucional (PyTorch) y su Mejora (2 minutos)
- **Que decir:**
  > "La red convolucional aprovecha la correlacion espacial 2D de los pixeles mediante filtros locales:
  > - **CNN Inicial (Baseline):** Dos convoluciones sencillas (16 y 32 filtros) alcanzaron 91.70% en validacion y 90.32% en prueba.
  > - **Mejora arquitectonica (evaluada solo en validacion):** Implementamos bloques convolucionales dobles (32x2 y 64x2) tipo VGG, incorporamos normalizacion por lotes (`BatchNorm2d`) para acelerar el aprendizaje y regularizamos con `Dropout` (0.25 en convoluciones y 0.4 en la capa densa) con optimizador Adam y decaimiento de pesos.
  > - **Resultado:** La validacion subio de 91.70% a **93.95%** (reduciendo la perdida a 0.1802). Al evaluar en la prueba oficial independiente, alcanzamos **92.68% de accuracy** y **0.9270 de F1 macro**, superando en +2.36% al modelo inicial."
- **Diapositiva:** Esquema de la CNN Mejorada y comparacion de metricas con el baseline.

---

### 5. Matriz de Confusion y Analisis de Errores (1 minuto)
- **Que decir:**
  > "En la matriz de confusion de la mejor CNN:
  > - Las prendas inferiores y accesorios tienen un desempeno sobresaliente: pantalones (98%), tenis (97%), sandalias (98%) y bolsas (99%).
  > - La prenda mas compleja es la **camisa** (75% de recall), confundiendose habitualmente con camiseta y abrigo. A 28 x 28 pixeles en escala de grises, detalles distintivos como cuellos o botones desaparecen casi por completo."
- **Diapositiva:** Matriz de confusion destacando la fila de camisas frente a camisetas y abrigos.

---

### 6. Evaluacion Externa y Cambio de Distribucion (1.5 minutos)
- **Que decir:**
  > "Probamos los modelos con 30 imagenes de catalogo comercial preprocesadas con el mismo pipeline (escala de grises, resta de fondo por borde y centrado en 28 x 28):
  > - La precision cayo al rango del 16% al 27% (MLP obtuvo 8/30 y CNN Mejorada 7/30).
  > - **¿Por que ocurre esta caida? (Fenomeno de Domain Shift):** En fotos reales de ropa sobre fondo blanco, al binarizar la silueta se crea un bloque solido continuo en el torso que los modelos confunden frecuentemente con vestidos (clase 3) o bolsas (clase 8). Ademas, 30 imagenes es una muestra estadisticamente reducida donde un solo acierto mueve la precision un 3.3%."
- **Diapositiva:** Figura con las fotos antes y despues del recorte (`verificacion_fotos_30.png`) y tabla de resultados externos.

---

### 7. Conclusiones (1 minuto)
- **Que decir:**
  > "En conclusion:
  > 1. La CNN supero a todos los modelos clasicos gracias al aprendizaje de caracteristicas espaciales locales.
  > 2. Tecnicas modernas como BatchNorm y bloques dobles permitieron una mejora cuantitativa solida (+2.36%).
  > 3. La evaluacion externa nos demuestra que la alta precision en un benchmark sintetico no garantiza robustez ante imagenes reales sin tecnicas de adaptacion de dominio y aumento de datos."
- **Diapositiva:** Puntos clave y cierre.

---

## Banco de Preguntas Rapidas del Profesor
1. **¿Por que dividiste entre 255?**
   > Para escalar los datos al rango continuo [0, 1], lo cual previene desbordamientos y permite que el gradiente descienda de forma estable.
2. **¿Por que aplanaste las imagenes para los primeros 4 modelos?**
   > Porque los modelos tradicionales de scikit-learn requieren una matriz 2D de (muestras, caracteristicas) y no procesan tensores espaciales.
3. **¿Por que no usaste la prueba para elegir la mejor CNN?**
   > Porque habria fuga de datos (data leakage). La prueba debe ser un examen ciego final; cualquier decision de diseno debe tomarse exclusivamente con el conjunto de validacion.
4. **¿Por que emitio advertencia la regresion logistica?**
   > Porque el solucionador L-BFGS alcanzo el limite de 300 iteraciones sin llegar a la tolerancia minima. Decidimos documentarla como parte del comportamiento real del modelo.
5. **¿Por que usaron fotos de internet en vez de fotos tomadas por ustedes?**
   > Para asegurar que las 10 clases estuvieran representadas fielmente segun la definicion estricta de Fashion-MNIST y bajo una licencia libre verificable (MIT). Todo el pipeline esta listo si se desea conectar fotos personales.
