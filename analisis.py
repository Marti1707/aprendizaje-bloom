## Mision 3
# Libreria para procesar archivos CSV.
import csv

# crea un lector, toma el archivo que se acaba de abrir y lo prepara para ir dividiendo cada linea por sus comas.
with open('ocean-temps.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo)
    # lee la primera fila del archivo. (sirve para saltar primera linea)
    cabecera = next(lector_csv)
    
## repasar que es un for loop.
# For loop es una estructura de codigo que sirve para repetir un grupo de acciones de forma automatica.

# fila es una variable que guarda informacion.
    for fila in lector_csv:
        temperatura_texto = fila[1]


        
        # La temperatura es distinta de MM.
        if temperatura_texto != "MM":
            # Si no es MM con (float) transformamos a número decimal.
            temperatura = float(temperatura_texto)

            # temperatura ya convertida.
            print("Temperatura válida:", temperatura)
        

## Mision 4

# Variables acumuladoras (inician en cero).
# 1.variable para ir sumando las temperaturas.
suma_total = 0.0
# cantidad de lecturas válidas que se procesan.
cuenta_valida = 0
# variable para calcular el maximo
temp_max = None
temp_min = None
promedio = None
# Crear lector que prepara el archivo.
with open('ocean-temps.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo)
    cabecera = next(lector_csv)
    
    for fila in lector_csv:
        temperatura_texto = fila[1]
        
        # Filtro: solo procesamos si NO es "MM".
        if temperatura_texto != "MM":
            temperatura = float(temperatura_texto)
            
            # 2. Acumulamos la temperatura y sumamos 1 al contador.
            suma_total = suma_total + temperatura
            cuenta_valida = cuenta_valida + 1
            # Calculamos el maximo
            if temp_max is None or temperatura > temp_max:
                temp_max = temperatura
            # Calculamos el minimo
            if temp_min is None or temperatura < temp_min:
                temp_min = temperatura
           
           
# 3. Calculamos el promedio fuera del bucle
    promedio = suma_total / cuenta_valida

print("Suma total de datos:", suma_total)
print("Cantidad de datos válidos:", cuenta_valida)
print("Promedio de temperatura:", promedio)
print("Temperatura maxima:", temp_max)
print("Temperatura minima:", temp_min)