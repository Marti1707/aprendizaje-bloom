import json #sirve para interpretar el texto JSON que responde la API.
import urllib.request #nos permite conectarnos a internet y hacer peticiones HTTP a la web.


# 1. Función para consultar la API (recibe dos entradas)
def pedir_sst(lat, lon): 
    #f me permitira remplazar {lat} y {lon} con los numeros de cordenadas de cada ciudad
    url = f"https://marine-api.open-meteo.com/v1/marine?latitude={lat}&longitude={lon}&hourly=sea_surface_temperature&start_date=2026-08-01&end_date=2026-08-07&timezone=auto"

    respuesta = urllib.request.urlopen(url) #Abre la conexion a internet
    contenido = respuesta.read().decode("utf-8") #lee los datos crudos descargados del servidor y los convierte en texto en formato uft-8
    datos = json.loads(contenido) #Toma ese texto con formato JSON y lo transforma en un diccionario de python sobre el cual podremos navegar.

    return datos["hourly"]["sea_surface_temperature"] #Entra al diccionario datos,busca dentro de "hourly" y extrae unicamente las temperaturas 


# 2. Función para evaluar el riesgo
def riesgo(sst_prom, umbral):
    if sst_prom > umbral:
        return "elevado"
    else:
        return "normal"


# 3. Coordenadas de los sitios (Misión 4)
sitios = {
    "Monterey": {"lat": 36.79, "lon": -122.47},
    "San Pedro": {"lat": 33.62, "lon": -118.32},
}

# 4. Ejecución del análisis
for nombre, coords in sitios.items():
    temps = pedir_sst(coords["lat"], coords["lon"])

    promedio = sum(temps) / len(temps)
    maximo = max(temps)
    estado_riesgo = riesgo(promedio, 18.0)

    print(f"---{nombre}---")
    print(f"Promedio: {promedio:.2f} °C")
    print(f"Máximo: {maximo:.2f} °C")
    print(f"Riesgo: {estado_riesgo}\n")