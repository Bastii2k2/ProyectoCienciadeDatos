# 🎵 Sistema Inteligente de Recomendación Musical con Enfoque de Explicabilidad

![Estado del Proyecto](https://img.shields.io/badge/Estado-Fase_Preparaci%C3%B3n_de_Datos-blue)
![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-CRISP--DM-success)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-yellow)

## 📖 Contexto del Proyecto
En el ecosistema actual de plataformas de streaming musical, los usuarios sufren de una "sobrecarga de información". Los sistemas de recomendación comerciales tradicionales operan como **"cajas negras"** y sufren de un fuerte **sesgo de popularidad** (recomendando siempre lo más escuchado). 

Este proyecto propone desarrollar un motor de recomendación musical *Content-Based* (basado puramente en características acústicas como la energía, bailabilidad y tempo). El objetivo no es solo sugerir canciones que suenen matemáticamente similares a una pista semilla, sino **proporcionar explicabilidad** al usuario final, justificando cada recomendación basándose en su firma sonora y fomentando un descubrimiento musical genuino (serendipia).

---

## 📂 Estructura del Repositorio
El proyecto sigue una estructura de directorios estándar para la ciencia de datos, garantizando la organización y reproducibilidad exigida:

```text
├── data/
│   ├── raw/                 # Dataset original crudo (spotify-tracks-dataset.csv)
│   └── processed/           # Dataset limpio, deduplicado y escalado
├── docs/                    # Documentación del proyecto, reportes y DQR
├── notebooks/               # Jupyter Notebooks con el código fuente comentado
│   ├── 01_EDA_y_Visualizacion.ipynb
│   └── 02_Preprocesamiento_Pipeline.ipynb
├── README.md                # Descripción general e instrucciones
└── requirements.txt         # Dependencias del proyecto