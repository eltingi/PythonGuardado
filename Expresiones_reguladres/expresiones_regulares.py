import re

texto = '''Hola maestro. esta es la cadena 1. como estas mi capitan
Esta es la 222 linea de texto.
Esta es la 2 linea de texto.
eses
Y Esta es la final linea 333444 definitiva mi capitan'''

#search encuentra considencias t me devuelve un dato de tipo match
#encuentra solo 1
#resultado = re.search("Hola",texto)

#findall me retorna una lista con los datos encontrados el atributo flags=re.IGNORECASE  para ingnorar las mayusculas
#resultado = re.findall("Esta",texto)
#busqueda simple
#resultado = re.findall("Esta",texto,flags=re.IGNORECASE)

#\d  -> busca digitos numericos del: 0 - 9
#resultado = re.findall(r"\d",texto)

#\D  -> busca TODO MENOS digitos numericos del: 0 - 9
#resultado = re.findall(r"\D",texto)

#\w  -> busca CARACTERES ALFANUMERICOS [a-z A-Z 0-9 _]
#python incluye el "_" como alfanumerico
#resultado = re.findall(r"\w",texto)

#\W  -> busca TODO MENOS CARACTERES ALFANUMERICOS [a-z A-Z 0-9 _]
#python incluye el "_" como alfanumerico
#ejemplo mostrara las , . espacios ,\n
#resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios tabs saltos en linea
#resultado = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios tabs saltos en linea
#resultado = re.findall(r"\S",texto)

#\n -> busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\. -> busca TODO MENOS saltos en linea
#resultado = re.findall(r".",texto)

#\ -> cancelar caracteres especiales y buscando los puntos: "." 
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero seguido de un punto y un espacio
#resultado = re.findall(f"\d\.\s",texto)

#acento cincunflejo
#^ -> BUSCA EL COMIENZO DE UNA LIONEA
#buscar el comienzo de una linea
#este solo para mostrar el ingnore case
#resultado = re.findall(r"^Hola",texto,flags=re.IGNORECASE)

#flags=re.M activa la multilinea, es decir que busca al principio de cada linea

#ejemplos:
#resultado_multilinea = re.findall(r"^Esta",texto,flags=re.M)
#print(resultado_multilinea)

#resultado = re.findall(r"^Hola",texto)
#print(resultado)
#fin ejemplos

# $ -> busca el final de una linea
#resultado = re.findall(r"capitan$",texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
# este en el caso de la cedana 333444 , como estoy buscando de a 3, me va a mostrar ejemplos 222 , 333, 444.
#es decir que encuentra en toda la cadena la cantidad de caracteres juntos definidos
#resultado = re.findall(r"\d{3}",texto)

#{n,m} -> al menos n, como maximo m
#este busca segun al cantidad entre 1 y 4 , es decir que en el caso de 333444, quedara en 3334 , 44
#resultado = re.findall(r"\d{1,4}",texto)

##{n,m} -> al menos n, como maximo m 
#ejemplo 2
# en este caso , cuando encuentrew al menos 2 "es" , recien me devolvera 1 , ejemplo texto: "eses"
#los conchetes sirven para aplicar la cantidad de veces que debe estar el texto junto
#resultado = re.findall(r"(es){2}",texto)


# | -> busca una cosa o la otra, si encuentra ambas mostrara ambas
resultado = re.findall(r"\d{2,4}|Hola",texto)
print(resultado)

