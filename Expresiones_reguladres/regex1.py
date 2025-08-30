import re
text = "The quick brown fox jumps over the lazy dog"

#1: busca una cadena donde al princio diga "The" , lo hace con el ^
#2: el .  busca cualquier cosa que no sea salto de linea, 
#2: el * afecta al anterior operador e indica que * → cero o más veces.👉 O sea: “cualquier cosa, repetida todas las veces que quieras (incluido nada)”.
#3: busca que la cadena termine con la palabra dog 
x = re.search("^The.*dog$",text)

if x:
    print("SI")
else:
    print("NO")
    
