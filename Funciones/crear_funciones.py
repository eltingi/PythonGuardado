
#aqui tenemos ejemplops de funciones

#funciones normales
def saludar():
    print("Holaaaaa maaaaan")


saludar()

#funcion que tenga parametros
def saludar_con_parametro(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"                                        
    elif (sexo == "hombre"):
        adjetivo = "Corneton"
    else:
        adjetivo = "maquina"
        
    print(f"Hola {nombre} , mi {adjetivo} ¿que sucede realmente?")
    
saludar_con_parametro("Master","hombreadada")

#funcion 
def crear_contraseña(num):
    listado_de_caracteres = "asjdasjkdaskjlf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c2]}{listado_de_caracteres[c3]}{num*3}"
    print(contraseña)
    
#funcion con retorno
def crear_contraseña_retorna(num):
    listado_de_caracteres = "asjdasjkdaskjlf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c2]}{listado_de_caracteres[c3]}{num*3}"
    return contraseña

#funcion con retorno de tupla
def crear_contraseña_retorna_tupla(num):
    listado_de_caracteres = "asjdasjkdaskjlf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c2]}{listado_de_caracteres[c3]}{num*3}"
    return (contraseña)
    
    
#funcion con retorno de multiples valores
def crear_contraseña_retorna_mul_valores(num):
    listado_de_caracteres = "asjdasjkdaskjlf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{listado_de_caracteres[c1]}{listado_de_caracteres[c2]}{listado_de_caracteres[c3]}{num*3}"
    return (contraseña,num)

    
mi_clave = crear_contraseña_retorna(23)

print(f"Esta es la clave retorno string: {mi_clave}")
    
mi_clave_tupla = crear_contraseña_retorna_tupla(23)

print(f"Esta es la clave retorno tupla: {mi_clave_tupla}")

#FORMA SEPARADA NO TAN OPTIMO EN ESPACION
mi_clave_mul_valores_1 = crear_contraseña_retorna_mul_valores(23)[0]
mi_clave_mul_valores_2 = crear_contraseña_retorna_mul_valores(23)[1]

#FORMA MAS OPTIMA EN ESPACION
#DESEMPAQUETANDO LA FUNCIONM
mi_clave_mul_valores_1,mi_clave_mul_valores_2 = crear_contraseña_retorna_mul_valores(23)

#MUESTRO LA DATA 
print(f"Esta es la clave retorno multi valores CLAVE: {mi_clave_mul_valores_1}")
print(f"Esta es la clave retorno multi valores NUM: {mi_clave_mul_valores_2}")


    
    