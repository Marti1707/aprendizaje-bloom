# Mision 1
import csv

# define la funcion leer_datos y recibe una variable que es la ruta del archivo que va a procesar
def leer_datos(nombre_archivo):
    datos = [] # crea una lista vacia (sera para guardar la informacion filtrada de cada fila)
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Salta la cabecera
        
        for fila in lector:
            if len(fila) == 3:
                fecha = fila[0]
                sitio = fila[1]
                temp_texto = fila[2]
                
                # se descartan las filas que tienen "MM"
                if temp_texto != "MM":
                    datos.append({
                        'date': fecha,
                        'site': sitio,
                        'temperature': float(temp_texto)
                    })
    return datos


def promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0.0
    return sum(temperaturas) / len(temperaturas)

datos_cargados = leer_datos('ocean-temps-2sites.csv')

# Se extraen solo las temperaturas para calcular el promedio general
lista_temperaturas = [d['temperature'] for d in datos_cargados]
promedio_total = promedio(lista_temperaturas)

print("Total de registros válidos:", len(datos_cargados))
print("Promedio general de temperatura:", promedio_total)

# Mision 2: Función para filtrar temperaturas
def temps_de_sitio(datos, sitio):

    temperaturas_filtradas = []
    for registro in datos:
        if registro['site'] == sitio:
            temperaturas_filtradas.append(registro['temperature'])
    return temperaturas_filtradas

datos_cargados = leer_datos('ocean-temps-2sites.csv')

temps_monterey = temps_de_sitio(datos_cargados, 'monterey')
promedio_monterey = promedio(temps_monterey)

temps_san_pedro = temps_de_sitio(datos_cargados, 'san_pedro')
promedio_san_pedro = promedio(temps_san_pedro)

print("Resultados por sitio")
print("Monterey -> Lecturas:", len(temps_monterey), "| Promedio:", promedio_monterey)
print("San Pedro -> Lecturas:", len(temps_san_pedro), "| Promedio:", promedio_san_pedro)

# Mision 3: Funcion de alerta y conteo de dias

def es_alerta(temp, umbral):
    
    #Devuelve True si la temperatura supera el umbral, de lo contrario False.
    
    return temp > umbral

# Defino un umbral fijo de 15.0 °C
UMBRAL = 15.0

# dias de alerta para Monterey
alertas_monterey = 0
for t in temps_monterey:
    if es_alerta(t, UMBRAL):
        alertas_monterey += 1

# dias de alerta para San Pedro
alertas_san_pedro = 0
for t in temps_san_pedro:
    if es_alerta(t, UMBRAL):
        alertas_san_pedro += 1

print(f"Días de alerta en Monterey: {alertas_monterey}")
print(f"Días de alerta en San Pedro: {alertas_san_pedro}")