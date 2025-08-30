
#arreglo , (se pueden modificar)
lista = ["Mauricio","matias sanchez",True,23]

print("lista")
print(lista)

#numero de corchete muestra el elemento que se encuentra en el indice indicado
print("lista [1]:")
print(lista[1])

#la tupla (no se puede modificar)
tupla = ("Mauricio","matias sanchez",True,23)
print("tupla [0]")
print(tupla[0])

#creando un conjunto SET, el conjunto no almacena datos duplicados(no tira error por eso), y no se pueden acceder aq los datos a travesd de indice
conjunto = {"Mauricio","matias sanchez",True,"conjunto",23,"matias sanchez"}
print("conjunto")
print(conjunto)


#Creando un diccionario (dict), uno es el que identifica como se llama el indice

#la estructura del diccionario es  la key (la clave) es como se le llama al indice, 
# key : valor
# para otra key se separan por ,
diccionario = {
    'Nombre' : "Mauricio",
    'Apellido' : "Sanchez",
    'Esta_emocionado' : True,
    'Altura' : 30,
    'Nombre_2' : "sdsds" 
}

print("Diccionario: ")
print( diccionario)

print( diccionario["Esta_emocionado"])

