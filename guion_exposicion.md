# Guion de Exposicion (7 a 10 minutos)
**Proyecto Fashion-MNIST · Gabriel Vallejo Castro**

Este guion esta estructurado para una presentacion fluida y clara ante el profesor y companeros de clase, explicando las decisiones tecnicas, los resultados reales y las limitaciones del proyecto.

---

## 1. Portada y Objetivo (1 minuto)
- **Que decir:**
  > "Buenas tardes. Mi proyecto consiste en la clasificacion automatica de prendas de vestir utilizando el conjunto de datos Fashion-MNIST. El objetivo es comparar cinco familias distintas de algoritmos de aprendizaje automatico (Regresion Logistica, SVM, Random Forest, Red Densa MLP y Red Convolucional CNN), seleccionar la mejor opcion de manera metodologica mediante un conjunto de validacion y evaluar su capacidad de generalizacion ante imagenes externas."
- **Diapositiva:** Titulo, autor, asignatura y objetivo general.

---

## 2. Datos, Particion y Normalizacion (1.5 minutos)
- **Que decir:**
  > "Fashion-MNIST contiene 70,000 imagenes en escala de grises de 28 x 28 pixeles distribuidas equitativamente en 10 clases (desde camisetas y pantalones hasta calzado y bolsos). Para garantizar rigor cientifico:
  > - Normalizamos los pixeles dividiendo entre 255 para ubicarlos en el rango continuo de 0 a 1.
  > - Separamos estratificadamente las 60,000 imagenes iniciales en 54,000 para entrenamiento y 6,000 para validacion con semilla fija 42.
  > - Las 10,000 imagenes de la particion oficial de prueba se mantuvieron totalmente aisladas para la evaluacion final sin usarlas para ajustar hiperparametros."
- **Diapositiva:** Malla de 10 ejemplos con sus etiquetas y diagrama de particion (54k train / 6k val / 10k test).

---

## 3. Modelos Tradicionales y Advertencia de Convergencia (1.5 minutos)
- **Que decir:**
  > "Evaluamos cuatro modelos tradicionales de scikit-learn sobre los vectores aplanados de 784 caracteristicas:
  > - **Regresion Logistica:** Sirve como linea base lineal. Obtuvo 84.28% en prueba. Alcanzo el limite de 300 iteraciones emitiendo una advertencia de convergencia (`ConvergenceWarning`), la cual documentamos transparentemente en lugar de ocultarla.
  > - **Random Forest (100 arboles):** Alcanzo 87.44% en solo 9.8 segundos.
  > - **MLP (128, 64 neuronas):** Obtuvo 88.18% con parada temprana.
  > - **SVM con kernel RBF (C=5):** Fue el mejor modelo tradicional con 89.59% y F1 macro de 0.8956, aunque requirio casi 3 minutos de entrenamiento debido al calculo intensivo de vectores de soporte."
- **Diapositiva:** Tabla comparativa de modelos tradicionales (metricas y tiempos).

---

## 4. Red Convolucional (PyTorch) y su Mejora (2 minutos)
- **Que decir:**
  > "A diferencia de los modelos aplanados, la Red Convolucional (CNN) conserva la estructura espacial 2D de la prenda.
  > - **CNN Inicial (Baseline):** Con 2 capas convolucionales simples (16 y 32 filtros), obtuvo 91.70% en validacion y 90.32% en prueba oficial.
  > - **Mejora de la CNN:** Para intentar aproximarnos al objetivo experimental del 97%, planteamos hipotesis arquitectonicas probadas **exclusivamente con el conjunto de validacion**:
  >   1. Bloques dobles de convolucion tipo VGG (32->32 y 64->64) para aumentar el campo receptivo.
  >   2. Normalizacion por lotes (`BatchNorm2d` y `BatchNorm1d`) para estabilizar gradientes y acelerar la convergencia.
  >   3. Regularizacion con Dropout (0.25 tras convoluciones y 0.4 en la densa) mas decaimiento de pesos (`weight_decay=1e-4`).
  > - **Resultado:** La validacion mejoro de 91.70% a **93.95%** (perdida de 0.1802). Al evaluar en la prueba oficial una vez fijada la arquitectura, obtuvimos **92.68% de accuracy** y **0.9270 de F1 macro**, superando a la inicial en +2.36 puntos porcentuales."
- **Diapositiva:** Diagrama arquitectonico de la CNN Mejorada y comparacion de curvas de perdida/accuracy.

---

## 5. Matriz de Confusion y Analisis de Clases (1 minuto)
- **Que decir:**
  > "Analizando la matriz de confusion de la mejor CNN:
  > - Clases con precision casi perfecta (>97-99%): pantalones, tenis, sandalias y bolsas. Tienen geometrias y siluetas muy distintivas.
  > - Clase con mayor dificultad: la **camisa** (75% de recall). El modelo la confunde principalmente con camiseta (clase 0) y abrigo (clase 4). A resolucion de 28 x 28 en escala de grises, la diferencia visual entre cuello camisero, cuello redondo y solapa es minima."
- **Diapositiva:** Matriz de confusion de la CNN Mejorada resaltando las clases camiseta, camisa y abrigo.

---

## 6. Evaluacion Externa (30 imagenes de internet) (1.5 minutos)
- **Que decir:**
  > "Para probar la generalizacion ante imagenes reales fuera de Zalando, recolectamos 30 imagenes (3 por categoria) del catalogo de e-commerce *Fashion Product Images (Small)* bajo licencia libre MIT:
  > - **Aclaracion obligatoria:** La consigna original pedia fotos personales con camara. Esta seleccion de internet es una alternativa reproducible documentada en `fotos/PROCEDENCIA.md`, cuya aceptacion esta pendiente de confirmacion con el profesor.
  > - **Preprocesamiento:** Estimamos el fondo por el borde, restamos el objeto, recortamos la caja delimitadora y centramos la prenda en 28 x 28 negro, igual que en Fashion-MNIST.
  > - **Resultados en las 30 fotos:** El rendimiento cayo a un rango de 16.7% a 26.7% (MLP obtuvo 8/30 y CNN Mejorada 7/30).
  > - **Causas del error (Domain Shift):** Las siluetas de prendas superiores reales al aplanarse a blanco sobre negro generan masas compactas que los modelos confunden con vestidos (clase 3) o bolsas (clase 8). Ademas, 30 imagenes es una muestra estadisticamente pequena donde cada muestra pesa 3.3%."
- **Diapositiva:** Imagenes externas antes y despues del preprocesamiento, y tabla de predicciones en las 30 fotos.

---

## 7. Conclusiones y Trabajo Futuro (1 minuto)
- **Que decir:**
  > "En conclusion:
  > 1. La CNN demostro superioridad frente a los metodos clasicos gracias a la extraccion de caracteristicas espaciales locales, logrando 92.68% en prueba oficial.
  > 2. Las tecnicas de modernizacion (BatchNorm, bloques dobles y regularizacion) aportaron una mejora medible y solida (+2.36%).
  > 3. La evaluacion externa nos ensena que un modelo entrenado en un entorno controlado como Fashion-MNIST sufre una caida drastica al aplicarse a fotos de catalogo real sin tecnicas de adaptacion de dominio.
  > 4. Como trabajo futuro, se requeriria entrenamiento con aumento de datos masivo (rotaciones, cambios de escala, iluminacion sintetica) para cerrar la brecha con el mundo real.
  > Quedo atento a sus preguntas. Muchas gracias."

---

## Posibles Preguntas del Profesor y Como Responderlas
1. **¿Por que dividiste los pixeles entre 255?**
   > *Respuesta:* Para normalizar los datos al intervalo [0, 1]. Esto facilita el descenso de gradiente en redes neuronales y optimizadores convexos, evitando que caracteristicas con valores numericos grandes dominen la funcion de perdida.
2. **¿Por que no usaste el conjunto de prueba para afinar la CNN?**
   > *Respuesta:* Porque violariamos la independencia del conjunto de prueba. Si usamos prueba para decidir la arquitectura o las epocas, estariamos cometiendo fuga de informacion (data leakage) y el resultado final seria optimista e irreal. Todo se decidio unicamente con el conjunto de validacion.
3. **¿Por que la regresion logistica emitio una advertencia de convergencia?**
   > *Respuesta:* El optimizador L-BFGS alcanzo el limite de 300 iteraciones sin cumplir el criterio de tolerancia de gradiente. La conservamos para documentar que en problemas de 784 variables y 10 clases, los clasificadores lineales requieren mas iteraciones o escalado adicional para converger plenamente.
4. **¿Por que fallo tanto en las 30 fotos externas?**
   > *Respuesta:* Por el cambio de distribucion (domain shift). Las imagenes de Fashion-MNIST fueron capturadas y preprocesadas por Zalando con un protocolo especifico de silueta y centrado. Las fotos externas de catalogo, aunque esten en fondo blanco, tienen sombras, proporciones corporales y detalles que al reducirse a 28x28 producen siluetas que los modelos interpretan como vestidos o bolsas. Ademas, 30 imagenes es una muestra pequena.
5. **¿Por que usaste imagenes de internet en vez de fotos tomadas por ti?**
   > *Respuesta:* Se utilizo un dataset abierto (Fashion Product Images) bajo licencia MIT para contar con ejemplos de alta calidad, estandarizados y con procedencia verificable para las 10 categorias exactas de Fashion-MNIST. Reconocemos que la consigna pedia fotos propias, por lo que esta alternativa fue documentada rigurosamente para someter su aceptacion a su criterio.
