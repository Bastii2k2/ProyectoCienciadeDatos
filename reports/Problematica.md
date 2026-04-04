# Formulación de la Problemática y Contexto Organizacional

### Contexto y Proceso Organizacional
En el ecosistema actual de plataformas de streaming musical (como Spotify, Apple Music, etc.), los usuarios tienen acceso a catálogos con millones de pistas. El proceso organizacional clave en este entorno es la retención y el engagement del Usuario, el cual se logra facilitando el descubrimiento de contenido relevante y personalizado.

### La Problemática
El acceso ilimitado a catálogos masivos ha generado un fenómeno de "sobrecarga de información", dificultando que los oyentes encuentren nueva música afín a sus gustos. Para mitigar esto, las plataformas utilizan sistemas de recomendación; sin embargo, estos presentan dos grandes fallas estructurales:

1. **Modelos de "Caja Negra":** Numerosos sistemas operan sin transparencia. El usuario recibe una recomendación, pero ignora completamente qué atributos musicales (ritmo, energía, positividad) originaron dicha sugerencia.
2. **Sesgo de Popularidad y "Filtro Burbuja":** Los algoritmos comerciales clásicos (como el filtrado colaborativo) tienden a recomendar lo más escuchado o a encerrar al usuario en un solo género musical, limitando el descubrimiento genuino (serendipia).

### Pregunta Analítica
> *¿Es posible desarrollar un sistema de recomendación musical basado puramente en contenido (características acústicas) que no solo sugiera pistas altamente similares, sino que proporcione explicabilidad matemática al usuario final, superando el sesgo de popularidad de los modelos tradicionales?*

# Objetivos del Proyecto (Enfoque SMART)

### Objetivo General
Desarrollar un motor inteligente de recomendación musical basado en similitud de contenido (Content-Based), enfocado en la explicabilidad de los atributos acústicos y el fomento del descubrimiento musical genuino.

### Objetivos Específicos
* **O1:** Preprocesar y estandarizar un dataset de Spotify de ~114.000 registros, ejecutando limpieza de valores nulos, eliminación de duplicados semánticos y aplicando transformaciones de escalado a 9 variables acústicas continuas.
* **O2:** Diseñar y entrenar algoritmos de recomendación espacial que permitan calcular, agrupar y sugerir canciones basándose estrictamente en métricas de distancia sobre sus firmas acústicas.
* **O3:** Desarrollar un módulo de explicabilidad que, por cada recomendación generada, calcule y exponga al usuario final las 3 variables acústicas principales (ej. energy, tempo) que justifican la similitud matemática con la pista semilla.
* **O4:** Evaluar comparativamente el rendimiento de los algoritmos candidatos mediante métricas de similitud estricta (Precision@K) y coherencia de sonido (Distancia Acústica Promedio) en la fase final de evaluación del ciclo CRISP-DM.

### KPIs y Criterios de Éxito
Para evaluar el éxito del proyecto, nos alejaremos de las métricas de clasificación tradicionales, ya que estamos resolviendo un problema de recomendación espacial.

### KPI 1: Distancia Acústica Promedio (Métrica Principal de Calidad)

**Descripción:** Mide la distancia matemática euclidiana media entre las características acústicas de la canción semilla y las recomendaciones generadas.

**Criterio de Éxito:** El algoritmo seleccionado debe lograr una distancia acústica promedio inferior a 0.05 (en variables normalizadas de 0 a 1), demostrando que las canciones recomendadas mantienen una coherencia sonora casi idéntica a la original.

### KPI 2: Tasa de Explicabilidad del Sistema

**Descripción:** Mide el porcentaje de recomendaciones entregadas que incluyen una justificación técnica comprensible para el usuario.

**Criterio de Éxito:** El 100% de las recomendaciones (Top-K) deben mostrar al usuario final la tríada de atributos matemáticos que generaron el cruce (ej. "Recomendada por su similitud en: loudness, danceability y energy").

### KPI 3: Tasa de Latencia / Tiempo de Inferencia (Requisito No Funcional)

**Descripción:** Mide el tiempo que tarda el sistema en procesar una canción semilla y devolver la lista del Top-K de recomendaciones.

**Criterio de Éxito:** El sistema debe ejecutar el cálculo de distancias y la generación de explicabilidad en menos de 2 segundos por consulta (medido en el entorno de desarrollo local), asegurando una experiencia de usuario fluida.