import re

email = "ejemplo@ejemplo.cl"

#primer bloque [a-zA-Z0-9._%+-]
#caracteres validos
#1: a-z -> busca de la letra "a" a la "z" minuscula
#2: A-Z ->  busca de la letra "A" a la "Z" mayuscula
#3: 0-9 -> busca del 0 al 9 numeros
#4: . -> busca todo loq ue no sea un espacio en linea
#5: _ -> busca que tega _
#6: % -> comodin , todo lo que encuentre antes o despues lo valida (comfirmando info)
#7: +- -> si encuentras al menos 1 concidencia de los caracteres que quiero validar esta true, si no hay ninguan false
#7: en cambio el * dejaba pasr todo si encuentra o no

#SEGUNDO BLOQUE
#+@
#1: +  -> EN TODO LO ANTERIOR []+  si encuentras al menos 1 concidencia de los caracteres que quiero validar esta true, si no hay ninguan false
#2: @ -> busca el textop como tal

#tercer bloque [a-zA-Z0-9._%+-]
#caracteres validos
#1: a-z -> busca de la letra "a" a la "z" minuscula
#2: A-Z ->  busca de la letra "A" a la "Z" mayuscula
#3: 0-9 -> busca del 0 al 9 numeros
#4: . -> busca todo loq ue no sea un espacio en linea
#5: _ -> busca que tega _
#6: % -> comodin , todo lo que encuentre antes o despues lo valida (comfirmando info)
#7: +- -> si encuentras al menos 1 concidencia de los caracteres que quiero validar esta true, si no hay ninguan false
#7: en cambio el * dejaba pasr todo si encuentra o no

#cuarto bloque
#+\.
#1: +  -> EN TODO LO ANTERIOR []+  si encuentras al menos 1 concidencia de los caracteres que quiero validar esta true, si no hay ninguan false
#2: \. -> busca el texto "."

#quinto bloque:
#[a-zA-Z]{2,}

#1: a-z -> busca de la letra "a" a la "z" minuscula
#2: A-Z ->  busca de la letra "A" a la "Z" mayuscula
#{2,} -> que al menos tenga 2 caracteres , luego de la coma no tiene nada por que no tienelimites

#patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#comando match me valida si se esta cumpliento mi patron en una cadena de texto
resultado = re.match(patron,email)

if resultado:
    print("Correo weno")
else:
    print("Correo malo")

