def decorador(funcion):
    def funcion_modificada():
        print("Antes de la funcion")
        funcion()
        print("Despues de la funcion")
    return funcion_modificada

def saludo():
    print("Hola mundito lindo  :D")
    
#aqui creamos la funcion decorada
saludo_decorado = decorador(saludo)
#aqui ejecutamos esta funcion decorada
saludo_decorado()

print("-------------- aqui ejecutamos el decorador con @ -------------------\n")


#otra forma de usar el decorador, es decir la opcion original optimizada
#de esta forma podemos realizar validaciones previas a uan funcion en particula: ejemplo autorizacion sobre permisos de usuario oy otros.
@decorador  #esto es igual a saludo = decorador(saludo)
def saludo2():
    print("Hola mundito lindo 2 :D")     
    
saludo2()