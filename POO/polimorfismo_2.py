#aqui se aplica polimorfismo , como python es un lenguaje de tipado dinamico, en si es polimorfismo
#ya que independiente del tipo de dato se interpreta el item 
#en los ejemplos se manda lista y luego una cadena de texto




def recorrer(elemento):
    for item in elemento:
        print(f"El elemento actual es: {item}")
        
        
lista = [1,2,3,4,5,6]
lista2 = ["Hola","Chao","Bye"]
lista3 = "Mauricio"

recorrer(lista)
recorrer(lista2)
recorrer(lista3)

