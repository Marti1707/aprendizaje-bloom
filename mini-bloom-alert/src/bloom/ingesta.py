import json
import urllib.error
import urllib.request


def pedir_sst(lat, lon):
    url = (
        "https://marine-api.open-meteo.com/v1/marine"
        f"?latitude={lat}&longitude={lon}&hourly=sea_surface_temperature"
    )
    try:
        with urllib.request.urlopen(url, timeout=10) as respuesta:
            contenido = respuesta.read().decode("utf-8")
            datos = json.loads(contenido)
            return datos.get("hourly", {}).get("sea_surface_temperature", [])
    except urllib.error.URLError as e:
        print(f"Error de red/conexión al consultar la API ({lat}, {lon}): {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error al procesar la respuesta JSON de la API ({lat}, {lon}): {e}")
        return []
    except Exception as e:
        print(f"Error inesperado al consultar la API ({lat}, {lon}): {e}")
        return []