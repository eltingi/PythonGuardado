import re

text = "remplazando todas las vocales por el asterisco"

#como se pone en [] busca cada caracter por separado , en esta caso a,e,i,o,u
#si fuera "aeiou" buscaria la palabra como tal
new_text = re.sub("[aeiou]","*",text)

print(new_text)

