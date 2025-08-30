#esta es uan forma de recorrer csv, no es la mas optima por la cantidad de opciones que ofrecen otras herramientas como pandam ejemplo leer_csv_con_panda.py
#importamos la libreria de csv
import csv

with open("archivos\\datos.csv") as archivito:
    #print(archivito)
    #print(csv.reader(archivito)) #retorna <_csv.reader object at 0x000002807E31D660> , esto es el objeto del archivo
    reader = csv.reader(archivito)
    for row in reader:
        #esto nos devuelve las filas
        print(row)
        
print(type(csv))
#csv es un modulo de csv