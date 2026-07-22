
import csv

with open('ocean-temps.csv', mode='r') as archivo:
    lector_csv = csv.reader(archivo)
    cabecera = next(lector_csv)
    
#repasar que es un for loop

    for fila in lector_csv:
        temperatura_texto = fila[1]


        
        # La temperatura es distinta de MM
        if temperatura_texto != "MM":
            # Si no es MM con (float) transformamos a número decimal
            temperatura = float(temperatura_texto)

            # temperatura ya convertida
            print("Temperatura válida:", temperatura)
        
