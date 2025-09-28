#metodos especiales 
#por ejemplo

class Persona:
    # __init__ es un metodo especial que se ejecuta automaticamente al crear una instancia de una clase
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    # __str__ es un metodo especial que se ejecuta automaticamente al imprimir una instancia de una clase
    # y debe retornar un string
    def __str__(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"
    #def __len__(self):
    #    return self.edad
    
    # def __del__(self):
    #     print(f"El objeto {self.nombre} ha sido eliminado")
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)

mauri = Persona("Mauricio",30)
print(mauri) #esto llama al metodo __str__ , el cual retorna un string y le indica al objeto como mostrarse en pantalla

repre = repr(mauri)
resultado = eval(repre) #eval ejecuta el string como si fuera codigo python
print(repr(mauri)) #esto llama al metodo __repr__ , el cual retorna un string y le indica al objeto como mostrarse en pantalla de forma mas tecnica
#lo mismo
print(repr(resultado))

#print(len(mauri)) #esto llama al metodo __len__ 


print("------__add__---sobrecarga de operadores-----")

ana = Persona("Ana",25)
otra_persona = mauri + ana  #esto llama al metodo __add__

print(otra_persona)

