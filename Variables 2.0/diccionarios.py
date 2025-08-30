#creando diccionarios con dic()
diccionario = dict(nombre = "lucas" , apellidos = "dalto")

#las listas no pueden ser claves por que son mutables y usamos frozenset para meter conjuntos

diccionario = {frozenset(["MS","LINDO"]): "resultado"}

#prueba de diccionacio retorna: {'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido'}
#itera el primer elemento y lo descompone dandole valor apellido a cada clave
#diccionario= dict.fromkeys("nombre","apellido")

#creo una lista donde cada clave queda con valor none
#diccionario = dict.fromkeys(["nombre","apellido"])
diccionario = dict.fromkeys(["nombre","apellido","fecha nacimiento"])
#print(diccionario["nombre"])

#creo un diccionario donde cada clave que con valor "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")



print(diccionario)