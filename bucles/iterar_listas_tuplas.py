
#recorriendo listas (todo esto sirve tambien para tuplas)

animales = ["perro", "gato", "pez", "loro"] 


#recorro la lista de animales 
for animal in animales:
    print(f"{animal} es un animal")
    

print("-------------------")

numeros = [56,11,23,213,42]   


#recorro la lista de numeros
for numerito in numeros:
    print(f"el numero es: {numerito * 10}")   
    
    
#recorro mas de 1 lista a la vez
for numero,animal in zip(numeros,animales):
    print(f"el numero es: {numero} y el animal es: {animal}")   
    
#recorro segun un rango de 2 numeros
for num in range(5,10):
    print(num)
    
    
#recorro segun un rango de 0 a 10 numeros
for num in range(10):
    print(num)
    
#FORMA NO OPTIMA PARA RECORRER LISTA (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    

#forma correcta.
#funcion enumarate

for num in enumerate(numeros):
    
    #retorna una tupla con el indice y el valor
    #print(num)
    #ejemplo 
    #(0, 56)
    #(1, 11)
    #(2, 23)
    #(3, 213)
    #(4, 42)   
    
    #retorno el tipo de dato y en este caso corresponde a una tupla
    #print(type(num))
    
    #aqui le digo cual es el dato de la tupla que quiero retrornar 0 indice 1 valor
    indice = num[0]
    valor = num[1]
    
    print(f"El indice es :{indice} y el valor es {valor} ")
    
    
    #usando el else
    for numero in numeros:
        print(f"ejecutaldo el ultimo bucle, valor actual {numero}")
    #usando el else , al terminar el bucle entrara al else, 
    else:
        print("El bucle termino")
        
        
