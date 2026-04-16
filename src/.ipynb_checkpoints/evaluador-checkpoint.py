import time
import numpy as np
from scipy.spatial.distance import cosine

def evaluar_modelo_recomendacion(nombre_modelo, vector_semilla, vectores_recomendados, tiempo_inicio, tiempo_fin):
    """
    Evalúa la calidad de las recomendaciones basándose en los KPIs del proyecto.
    """
    print(f"\n=== EVALUACIÓN DEL MODELO: {nombre_modelo} ===")
    
    # KPI 3: Latencia (Tiempo de inferencia)
    latencia = tiempo_fin - tiempo_inicio
    print(f"⏱️ KPI Latencia: {latencia:.4f} segundos")
    
    # KPI 1: Distancia Acústica Promedio (Coherencia del sonido)
    distancias = []
    
    # Si estamos evaluando un modelo, necesitamos asegurarnos de que la métrica sea consistente
    # Usamos la distancia del coseno para todos como estándar de evaluación
    for idx, fila in vectores_recomendados.iterrows():
        # Scipy calcula la distancia del coseno (1 - similitud)
        dist = cosine(vector_semilla.values[0], fila.values)
        distancias.append(dist)
        
    distancia_promedio = np.mean(distancias)
    
    print(f"📏 KPI Distancia Acústica Promedio: {distancia_promedio:.4f}")
    
    # Evaluación contra el Criterio de Éxito (< 0.05)
    if distancia_promedio < 0.05:
        print("✅ Resultado: ÉXITO (Recomendaciones altamente coherentes)")
    else:
        print("⚠️ Resultado: FALLO (Recomendaciones demasiado dispersas acústicamente)")
        
    print("===========================================\n")
    
    return latencia, distancia_promedio