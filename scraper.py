import json
import random
from datetime import datetime

# --- CONFIGURACIÓN DEL ROBOT ---
def obtener_resultados():
    print("Iniciando búsqueda...")
    
    # NOTA: Ahora mismo genera números de prueba.
    # Cuando me des la web oficial, cambiaré esto para leerla de verdad.
    dia = f"{random.randint(0, 99):02d}"
    noche = f"{random.randint(0, 99):02d}"
    
    # Hora actual
    ahora = datetime.now()
    fecha_formato = ahora.strftime("%d/%m/%Y a las %H:%M")
    
    return {
        "dia": dia,
        "noche": noche,
        "mensaje": "✅ Robot activo (Modo Prueba)",
        "fecha": fecha_formato
    }

# --- GUARDAR DATOS ---
try:
    datos = obtener_resultados()
    with open('datos.json', 'w') as f:
        json.dump(datos, f)
    print("¡Éxito! Datos actualizados.")
except Exception as e:
    print(f"Error: {e}")
