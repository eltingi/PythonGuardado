

frutas = ["banana","manzana","kiwi","frutilla","palta","naranja" ]
numeros = [1,2,4,56,7]
#continue
#evitando que continue por el for, por una condicion y conbtinue
for fruta in frutas:
    if fruta == "manzana":
        continue    
    print(f" voy por una: {fruta}")

print("-----------------")  


#break
#evitar que el bucle siga ejecutandoce
for fruta in frutas:
    print(f" voy por una: {fruta}")
    if fruta == "frutilla":
        break #no ejecuta el else
else:
    print("terminado")
   
#recorrer una cadena de textO, ESTE LO REALIZA POR CARACTER
cadena = "Mauricio"

for letra in cadena:
    print(letra)
    
#recorrer en uan sola linea de codigo
numeros_dulicados_una_linea = [x*2 for x in numeros]
print(numeros_dulicados_una_linea)
    
#nomalmente:
numeros_dulicados = list()
for numero in numeros:
    numeros_dulicados.append(numero*2)
    
#print(numeros_dulicados)    


