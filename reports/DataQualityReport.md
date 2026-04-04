# Reporte de Calidad de Datos (Data Quality Report - DQR)

**Dataset:** Spotify Tracks Dataset
**Objetivo:** Evaluar el estado, consistencia y viabilidad de los datos crudos antes de la fase de modelado, identificando riesgos y ejecutando planes de mitigación.

### 1. Completitud (Completeness)
* **Diagnóstico:** El dataset presenta un nivel de completitud excepcional. De las más de 114.000 filas iniciales, se detectó únicamente **1 fila** con valores nulos (específicamente en las variables categóricas de texto `artists`, `album_name` y `track_name`). Las variables numéricas acústicas (energía, tempo, bailabilidad, etc.) cuentan con un 100% de completitud.
* **Impacto:** Riesgo nulo. La falta de datos es estadísticamente insignificante y no afectará el entrenamiento de los modelos espaciales.

### 2. Unicidad (Uniqueness)
* **Diagnóstico:** Se identificó un problema crítico de duplicidad semántica en la base de datos. Aunque la columna `track_id` sugería valores únicos, el análisis combinado de las columnas `track_name` y `artists` reveló que más de **24.000 canciones estaban duplicadas**. Esto es un comportamiento nativo de la API de Spotify, la cual asigna IDs distintos a la misma pista si esta aparece en su versión *Single*, dentro de un *Álbum* o en una *Recopilación*.
* **Impacto:** Alto. De no tratarse, un modelo basado en contenido podría recomendar la misma canción exacta múltiples veces al usuario en el Top-K, degradando drásticamente la experiencia de descubrimiento.

### 3. Validez y Consistencia (Validity & Consistency)
* **Diagnóstico de Variables Acústicas:** Las variables continuas entregadas por la API (`danceability`, `energy`, `valence`, etc.) son válidas y respetan estrictamente su rango teórico (generalmente de 0.0 a 1.0).
* **Diagnóstico de Etiquetas (Anomalía de Géneros):** Se detectó una inconsistencia grave en la columna categórica `track_genre`. Durante el Análisis Exploratorio, géneros masivos a nivel global como `latin` o `latino` mostraron una popularidad media cercana a cero. Esto demuestra que la etiqueta de género provista es inconsistente y en muchos casos arbitraria, agrupando éxitos latinos bajo etiquetas más generales como `pop` o `dance`.
* **Impacto:** Medio-Alto. Esta anomalía justifica y valida la decisión arquitectónica de **no** basar el sistema de recomendación en la etiqueta de texto `track_genre`, sino en el cálculo de distancias matemáticas sobre las variables acústicas puras.

### 4. Precisión y Valores Atípicos (Accuracy & Outliers)
* **Diagnóstico:** En la variable `duration_ms`, se observó que la norma de la industria se agrupa rígidamente entre los 3 y 4 minutos. Sin embargo, existen valores atípicos válidos de pistas que superan los 8 o 10 minutos (asociados a géneros como música clásica o jazz). Adicionalmente, variables como `tempo` (BPM) y `loudness` (decibelios) manejan escalas numéricas absolutas muy superiores a las demás características acústicas.
* **Impacto:** Alto para el modelado. Si se utilizara algoritmos basados en distancias (como K-Nearest Neighbors), las variables con escalas mayores (como el tempo) dominarán el cálculo, opacando a las variables de rango pequeño (0 a 1).

## Plan de Acción y Mitigación (Pipeline de Preprocesamiento)

Para asegurar la calidad óptima del dataset antes de la fase de modelado, se ejecutó el siguiente pipeline de transformaciones:

1. **Eliminación de Nulos:** Se eliminó la única fila que presentaba valores faltantes.
2. **Deduplicación Semántica:** Se aplicó un filtro de unicidad conservando solo la primera aparición basada en la llave compuesta `[track_name, artists]`, reduciendo el dataset a pistas genuinamente únicas.
3. **Escalado Espacial:** Se aplicó la transformación matemática `MinMaxScaler` a las variables acústicas continuas. Esto comprimió todas las magnitudes (incluyendo `tempo` y `loudness`) a un rango equitativo entre **0 y 1**, garantizando que el algoritmo espacial calcule las distancias sin sesgos de escala geométrica.