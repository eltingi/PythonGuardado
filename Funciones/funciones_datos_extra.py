
#se crea funcion con 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword arguments
frase_resultado = frase(adjetivo= "Pulento",nombre= "MS",apellido="SAN")

print(frase_resultado)


#se crea funcion con 3 parametros la cual deja cpor defecto un valor en un parametro.
def frase_nueva(nombre,apellido,adjetivo = "Maquina"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword arguments
frase_resultado = frase_nueva(nombre= "MS",apellido="SAN")

print(frase_resultado)