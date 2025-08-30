import re

text = "la fecha es 23/06/2021 y el telefono es 1231232154125412 23/06/2021 23/06/2021"

#patron a buscar
patron = r"\d{2}/\d{2}/\d{4}"

#texto que remplazara el patron buscado
remplazo = "Fecha oculta"

#sub
#remplaza todas las aparicionbes del patron en la cadena de texto
nuevo_texto = re.sub(patron,remplazo,text)

# imprimir el resultado
print("Texto modificado: ", nuevo_texto)