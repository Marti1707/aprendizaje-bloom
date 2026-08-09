import csv
import csv

def leer_datos(nombre_archivo):
    datos = []
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Salta la cabecera (date, site, sea_surface_temp_c)
        
        for fila in lector:
            if len(fila) == 3:
                fecha = fila[0]
                sitio = fila[1]
                temp_texto = fila[2]
                
                # Descartamos las filas que tienen "MM"
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