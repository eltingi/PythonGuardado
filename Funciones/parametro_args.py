


#utilizar parametro *arg
#utilizando operador * como argumento (*args)

def suma(nombre,*numeros):
    return f"{nombre} ,  la suma de los numeros es: {sum(numeros)}"


resultado = suma("MS",1,2,4,5,6,2,8)
print(resultado)


