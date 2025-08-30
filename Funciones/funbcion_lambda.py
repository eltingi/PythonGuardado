



numeros = [1,2,3,4,5,6,7,8,9,10]

#funcion lambda para multiplicar x*2
multiplicar_por_dos = lambda x : x*2

#lo mismo pero en uan funcion
def multiplicar_por_dos_funcion(x):
    return x*2

print(multiplicar_por_dos(5))

print(multiplicar_por_dos_funcion(5))

#-------------------------
#funcion normal
def es_par(num):
    if(num%2 == 0):
        return True

#usando una funcion filter con una funcion comun
numero_pares = filter(es_par,numeros)

print(f" usando funcion normal: {list(numero_pares)}")


#usando lo mismo pero en lambda
numero_pares = filter(lambda numero:numero%2 == 0,numeros)

print(f" usando funcion lambda: {list(numero_pares)}")



