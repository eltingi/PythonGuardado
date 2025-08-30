cadena1 = "Hola mauricio"
cadena2 = "Se puede"

#DIR #FUNCION
#Devuelve la lista de atributos validos del objeto pasado.


#METODOS:

#UPPER - Convierte a mayuscula print(cadena1.upper())
#LOWER - CONVIERTE A MINUSCULA print(cadena1.lower())
#CAPITALIZE PRIMERA EN MAYUSCULA print(cadena1.capitalize())

#print(cadena1.capitalize())

#find buscamos una cadena en otra
#devuelve el indix en donde se encuentra, si no encuentra nada devuelve -1

busqueda_find = cadena1.find("c")

#inde buscamos una cadena en otra cadena, pero si no hay coincidencia lanza excepcion (error)
#devuelve el indix en donde se encuentra

busqueda_index = cadena1.index("c")



#iSNUMERIC

cadena3 = "Se puede 2"
cadena4 = "33"


es_numerico = cadena4.isnumeric()


#alfanumerico devuelve si una cadena corresponde a un valor alfanumerico, letras (sin espacion ni caracteres especiales).
cadena5 = "Hdfdfdf"
es_alfanumerico = cadena5.isalpha()



#count buscamos una cadena en otro cadena . deuvlkev ela cantidad de veces que coincida
#busca el texto tal cuual si la poalabra bsucada esta dentro de otra palabra la cuenta igual

cadena6 = "Hola mucho gusto me gusta programar"


cuenta_texto = cadena6.count("mucho")


#LEN,(funcion) contamos cuantos caracteres tiene una cadena

cadena7 = "Hola mucho gusto me gusta programar"

cuenta_len = len(cadena7)

#startsswith, verifica como comienza una cadena, si corresponde devuelve true
cadena8 = "Hola mucho gusto me gusta programar"

star_bol = cadena8.startswith("Hola mucho")
        #print(cadena7.endswith("Hola mucho"))


#startsswith, verifica como termina una cadena , si corresponde devuelve true
cadena9 = "Hola mucho gusto me gusta programar"

star_bol = cadena9.endswith("programar")
        #print(cadena9.endswith("programar"))


#replace: emplaza un pedazo de la cadena dada, por otra dada
cadena10 = "wena compare como estamos"
cadena_nueva = cadena10.replace("wena","Hola")  # retorna"Hola compare como estamos"

#print(cadena_nueva)


#split nos devuelve una lista

cadena11 = "wena compare como estamos"
cadena_separada = cadena11.split(" ")

#print(cadena_separada)
#print(cadena_separada[1])
