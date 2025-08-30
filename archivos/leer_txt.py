
#ruta se escribe con los \\
#le damos la codificacion utf8 para las tildes
#usando open para abrir un archivo con una codificacion universal (UTF-8) a "archivos"
archivo_sin_leer = open("archivos\\text_en_txt.txt",encoding="UTF-8")

#UNA VES SE LEE ELK ARCHIVO CON EL .read() , no se puede volver a leer el archivo 
# es por eso que en el ejemplo de linea_array_vacio , querda el array vacion
#archivo = archivo_sin_leer.read()
#SI APLICO ESTE CODIGO DEJARA UN ARRAY VACION
#linea_array_vacio =  archivo_sin_leer.readlines()

#una sola linea
#una_linea = archivo_sin_leer.readline()
#print(f"una linea: {una_linea}" )
#guarda linea por linea, dejandolo en una lista
lineas = archivo_sin_leer.readlines()
print(type(lineas))
print(lineas)