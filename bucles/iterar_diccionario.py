
diccionario = {
    "nombre": "Mauri",
    "apellido": "SAN",
    "dinero": 1,
    3: True    
}

print(diccionario)

#estas 2 formas mostraran lo mismo
for key in diccionario:
    print(key)
    
for value in diccionario:
    print(value)
    
#para iterar un diccionario necesitamos recorrer sus items

for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"El indice es {key} y el valor es {valor}")