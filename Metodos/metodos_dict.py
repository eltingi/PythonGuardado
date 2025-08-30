
diccionario = {
    "nombre" : "Mabri",
    "apellido" : "Sanchez",
    "Edad" : 34,
    "nick" : "Acaricia nalgas"
}

#iterar
#

#keys, trae todas las keys , que son los nombres que le dimos a cada valor 
llave = diccionario.keys()


#["NOMBRE"] al llamarlo con los corchetes se llama elk valor indicando el nombre de la key
#pero si no se encuentra tirara una excepcion (error)
clave = diccionario["apellido"]


#GET : metodo que peude acceder a la propiedad particular de un objeto
#Aqui se trae el valor segun el nombre de la key, pero si no lo encuentra no devuelve nada y no lansza excepcion
#
clave = diccionario.get("nombressss")

#clear
#eliminar todo del diccionario
#diccionario.clear()

#pop elimina un elemento deñ diccopmnarop
diccionario.pop("nombre")


#obteniendo un elemento dict_iems iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

