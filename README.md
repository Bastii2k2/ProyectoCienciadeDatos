# 🎵 Sistema Inteligente de Recomendación Musical con Enfoque de Explicabilidad

![Estado del Proyecto](https://img.shields.io/badge/Estado-Fase_Preparaci%C3%B3n_de_Datos-blue)
![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-CRISP--DM-success)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-yellow)

## 📖 Contexto del Proyecto
En el ecosistema actual de plataformas de streaming musical, los usuarios sufren de una "sobrecarga de información" al navegar por catálogos de millones de pistas. Además, los sistemas de recomendación comerciales tradicionales presentan dos problemas críticos:
1. Operan como **"cajas negras"**, donde el usuario ignora por qué se le recomienda una canción.
2. Sufren de un **sesgo de popularidad**, recomendando frecuentemente los mismos éxitos masivos y limitando el descubrimiento.

Este proyecto, desarrollado en el marco de la asignatura de **Ciencia de Datos Avanzado**, aplica la metodología **CRISP-DM** para construir un motor de recomendación musical *Content-Based*. Utilizando características acústicas puras (energía, bailabilidad, tempo, etc.), el sistema no solo sugiere canciones matemáticamente similares, sino que proporciona **explicabilidad** técnica al usuario final para fomentar un descubrimiento musical genuino y transparente.

---

## 📂 Estructura del Repositorio
El proyecto está estructurado para separar claramente los datos, el código y la documentación, asegurando su escalabilidad:

```text
├── data/
│   ├── raw/                 # Dataset original crudo (spotify-tracks-dataset.csv)
│   └── processed/           # Dataset limpio, deduplicado y escalado
├── models/                  # Modelos ML entrenados
├── reports/                 # Data Quality Report y Formulación de Problemática
├── notebooks/               # Jupyter Notebooks documentados paso a paso
│   ├── 01_EDA_Spotify.ipynb
│   └── 02_Preprocesamiento.ipynb
├── README.md                # Descripción e instrucciones de ejecución
└── requirements.txt         # Listado estricto de dependencias