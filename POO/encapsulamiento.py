class clasesita:
    def __init__(self):
        #con un _ indica alos programadores que esa propiedad es privada, pero si se puede acceder
        self._privado = "Hola"
        #con dos __ indicaque que es muy pirvado y no se puede acceder haciendo un objeto, se necesita setters y getters
        self.__muyprivado = "Privado"
        
    def __hablar(self):
        print("Hola muy privado")
        
                
        
objeto = clasesita()
print(objeto._privado)
#print(objeto.__muyprivado)