
frase = input("Coloca una frase y te calculo cuanto tardaria mauricio en decirla: " )

#creamos una lista con las palabras separadas con un espacio en el split 
palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

print("--------------------------------------------------------")

if cantidad_de_palabras > 15:
    print("No hables tanto rey")
    
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Mauricio lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos")
