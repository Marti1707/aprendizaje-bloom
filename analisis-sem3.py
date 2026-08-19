#Import
import csv

##Funciones
def leer_datos(nombre_archivo):
    datos = [] # crea una lista vacia (sera para guardar la informacion filtrada de cada fila)
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.reader(archivo) # crea objeto lector que itera sobre las filas del csv
        next(lector)  # Salta la cabecera

        #inicia ciclo
        for fila in lector:
            if len(fila) == 3: #comprueba que la fila tenga 3 columnas
                #los siguientes extraeran la fecha, el sitio y la temperatura en texto
                fecha = fila[0]
                sitio = fila[1]
                temp_texto = fila[2]
                
                # se descartan las filas que tienen "MM"
                if temp_texto != "MM":
                    #se agrega un dic a datos, convierte la temperatura a numero flotante
                    datos.append({
                        'date': fecha,
                        'site': sitio,
                        'temperature': float(temp_texto)
                    })
    #devuelve la lista estructurada con los datos procesados
    return datos


# se define la funcion para obtener el promedio de las temperaturas
def promedio(temperaturas):#comprueba si la lista de temperaturas esta vacia, asi se evitan errores al momento de calcular
    if len(temperaturas) == 0:
        return 0.0 #el promedio es 0.0 cuando no hay datos para calcular
    #calcula media aritmetica SUM(suma), LEN(longitud) devuelve la cantidad total de elementos que contiene una coleccion o la cantidad de caracteres de un texto
    return sum(temperaturas) / len(temperaturas)


def temps_de_sitio(datos, sitio):

    temperaturas_filtradas = [] #crea una lista vacia (sera para las temperaturas filtradas)
    # L53,L54,L55 recorre cada registro de temperaturas, si coincide con el sitio, agrega su temperatura a la lista
    for registro in datos:
        if registro['site'] == sitio:
            temperaturas_filtradas.append(registro['temperature'])# .append sirve para agregar un nuevo elemento al final de la lista, en este caso a sitio se le suma la temperatura
    # devuelve la lista con los datos de las temperaturas filtradas.
    return temperaturas_filtradas


def es_alerta(temp, umbral):#se define la logica de alerta
    
    #Devuelve TRUE si la temperatura supera el umbral, de lo contrario FALSE
    return temp > umbral


def agrupar_por_sitio(datos): #funcion para estructurar las temp agrupadas por sitio
    resumen = {}#inicializa un dic vacio donde los nombres de los sitios seran la clave 

    #se recorre cada registro extrayendo el sitio y la temperatura 
    for registro in datos: 
        sitio = registro['site']
        temp = registro['temperature']
        
        # Si el sitio aún no existe como clave en el diccionario, se crea con una lista vacía
        if sitio not in resumen:
            resumen[sitio] = []
            
        # se agrega la temperatura a la lista correspondiente
        resumen[sitio].append(temp)
        
    return resumen#devuelve el dic organizado
## Mision 1
datos_cargados = leer_datos('ocean-temps-2sites.csv') # ejecuta la lectura del archivo real

# Se extraen solo las temperaturas para calcular el promedio general
lista_temperaturas = [d['temperature'] for d in datos_cargados]
# calcula el promedio general de todas las lecturas
promedio_total = promedio(lista_temperaturas)

print("Total de registros válidos:", len(datos_cargados))
print("Promedio general de temperatura:", promedio_total)

## Mision 2: Función para filtrar temperaturas

#se obtienen temperaturas y promedios. L60,L62,L63,L65,L66.
datos_cargados = leer_datos('ocean-temps-2sites.csv')

#MONTEREY
temps_monterey = temps_de_sitio(datos_cargados, 'monterey')
promedio_monterey = promedio(temps_monterey)

#SAN PEDRO
temps_san_pedro = temps_de_sitio(datos_cargados, 'san_pedro')
promedio_san_pedro = promedio(temps_san_pedro)

print("Resultados por sitio")
print("Monterey -> Lecturas:", len(temps_monterey), "| Promedio:", promedio_monterey)
print("San Pedro -> Lecturas:", len(temps_san_pedro), "| Promedio:", promedio_san_pedro)

## Mision 3: Funcion de alerta y conteo de dias

# Defino un umbral fijo de 15.0 °C
UMBRAL = 15.0

# dias de alerta para Monterey, inicializa un contador para monterey y suma +1 por cada temperatura que supere al umbral
alertas_monterey = 0
for t in temps_monterey: #por cada temperatura en monterey
    if es_alerta(t, UMBRAL): #comprueba si la temperatura supera el limite, si cumple con esa condicion es alerta
        alertas_monterey += 1 #por cada alerta +1

# dias de alerta para San Pedro
alertas_san_pedro = 0
for t in temps_san_pedro:
    if es_alerta(t, UMBRAL):
        alertas_san_pedro += 1

print(f"Días de alerta en Monterey: {alertas_monterey}")
print(f"Días de alerta en San Pedro: {alertas_san_pedro}")

## Mision 4 agrupar datos por sitio en diccionario

# Agrupa todas las temperaturas por sitio 
datos_agrupados = agrupar_por_sitio(datos_cargados)

# Ahora se puede iterar sobre el diccionario para calcular promedios y alertas de forma dinámica
UMBRAL = 15.0

print("RESUMEN AGRUPADO POR SITIO")
for sitio, temperaturas in datos_agrupados.items():#recorre cada lista de temperaturas
    prom = promedio(temperaturas)# promedio directo de sitio actual
    
    # se cuentan alertas usando nuestra función es_alerta
    cant_alertas = sum(1 for t in temperaturas if es_alerta(t, UMBRAL))
    
    print(f"Sitio: {sitio.capitalize()}")
    print(f"  - Lecturas: {len(temperaturas)}")
    print(f"  - Promedio: {prom:.2f} °C") # 2f redondea a 2 decimales la unidad °C
    print(f"  - Días de alerta: {cant_alertas}")
    print("-" * 30)