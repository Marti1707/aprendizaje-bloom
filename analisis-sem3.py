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

print("--- RESULTADOS POR SITIO ---")
print("Monterey -> Lecturas:", len(temps_monterey), "| Promedio:", promedio_monterey)
print("San Pedro -> Lecturas:", len(temps_san_pedro), "| Promedio:", promedio_san_pedro)