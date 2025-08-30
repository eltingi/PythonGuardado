#se una with open
#es importante la ruta correcta para no dar excepcion

#al usar with open no es necesario cerrar el archivo 
with open("archivos\\text_en_txt.txt",encoding="UTF-8") as archivito:
    contenido = archivito.read()
    print(contenido)


