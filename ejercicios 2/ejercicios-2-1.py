
#falto el profesor y los alumnos armaran la clase

#perdir el nombre y la edad de los compaeros que vinieron hoy a clases

compañeros = []


def obterner_compañeros(cantidad):
    for i in range(cantidad):
        nombre = input("ingrese el nombre del compañero")
        edad = int(input("ingrese la edad del compañero"))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    #esto crea un iterable ordenada por el parametro 1 que es edad   , es decir que deja primero al mas pequeño y al ulñtimo al ma s grande 
    compañeros.sort(key=lambda x:x[1])
    
    #auqi necesito tomar el primero de la lista
    #ejemplo ("ms,23"),("ss,11") .
    #en este caso el primero es ms,23, por eso es el primer [0]
    # , ahora el segundo es para ingresar al dato 0, que corresponde a nombre
    asistente = compañeros[0][0]
    
    #aqui necesito ingresar al ultimo registro de la lksta, que corresponde al preofesor (segun logica de programa soliciotado)
    #se ingresa -1, ya que le indica que se devuelve al listado del array que seria el ultimo
    profesor = compañeros[-1][0]

    #retornamos una tupla
    return asistente,profesor

asistente,profesor = obterner_compañeros(2)

print(f"El asistente es: {asistente} y el profesor es {profesor}")
