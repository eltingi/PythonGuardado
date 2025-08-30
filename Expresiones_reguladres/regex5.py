import re
text = "Esta es un ejemplo de una página web: https://www.ejemplo.cl muy wena"

#bloque 1
#1: ?  -> el signo de ? sirve para indicar si encuentra la palabra la cual en este caso es https, la acepta, y si no la encuentra tambien
#2: a-z -> busca de la letra "a" a la "z" minuscula
#3: A-Z ->  busca de la letra "A" a la "Z" mayuscula
#4: 0-9 -> busca del 0 al 9 numeros
#4: . -> busca todo loq ue no sea un espacio en linea

#bloque 2
#+\.
#1: +  -> EN TODO LO ANTERIOR []+  si encuentras al menos 1 concidencia de los caracteres que quiero validar esta true, si no hay ninguan false
#2: \. -> busca que tenga un punto

#bloque 3
#[a-zA-Z]{2,}
#1: a-z -> busca de la letra "a" a la "z" minuscula
#2: A-Z ->  busca de la letra "A" a la "Z" mayuscula
#{2,} -> que tenga 2 o mas caracteres




patron = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.findall(patron,text)

print(resultado)