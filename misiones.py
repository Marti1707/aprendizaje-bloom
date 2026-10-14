import json
import urllib.request


def pedir_sst(lat, lon):
    url = f"https://marine-api.open-meteo.com/v1/marine?latitude={lat}&longitude={lon}&hourly=sea_surface_temperature&start_date=2026-08-01&end_date=2026-08-07&timezone=auto"
    try:
        respuesta = urllib.request.urlopen(url)
        contenido = respuesta.read().decode("utf-8")
        datos = json.loads(contenido)
        return datos.get("hourly", {}).get("sea_surface_temperature", [])
    except Exception as e:
        print(f"Error al consultar la API para lat={lat}, lon={lon}: {e}")
        return []


def riesgo(sst_prom, umbral):
    if sst_prom is None:
        return "desconocido"
    if sst_prom > umbral:
        return "elevado"
    else:
        return "normal"


sitios = {
    "Monterey": {"lat": 36.79, "lon": -122.47},
    "San Pedro": {"lat": 33.62, "lon": -118.32},
}

for nombre, coords in sitios.items():
    temps_raw = pedir_sst(coords["lat"], coords["lon"])

    # filtrado de 544los valores nulos 
    temps = [t for t in temps_raw if t is not None]

    if not temps:
        print(f"--- {nombre} ---")
        print("No hay datos suficientes para calcular estadísticas.\n")
        continue

    promedio = sum(temps) / len(temps)
    maximo = max(temps)
    estado_riesgo = riesgo(promedio, 18.0)

    print(f"--- {nombre} ---")
    print(f"Promedio: {promedio:.2f} °C")
    print(f"Máximo: {maximo:.2f} °C")
    print(f"Riesgo: {estado_riesgo}\n")