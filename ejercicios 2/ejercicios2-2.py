#este funcion lka cipie tal cual curso
#creando una funmciomn que nso devuelve los numeros primos

#entre 0 y el argumento que pasamos
# 
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse 
    # #por ningun entre 2 y ese numero -1
   
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y terminba el bucle
        if num%i==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True


#crenado la funcion que devulve una lista con todos los primos
def primos_hasta(num):
    primos = []
    #se le suma + 1 para que tome el ultimo valor ingresado, ejemplo 13 que es primo, tonces si ignreso 13, me lo debe devolver
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(10)

print(resultado)