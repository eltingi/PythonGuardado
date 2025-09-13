class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        def hablar(self):
            print("Hola raton con cola")
        
#aquoi se herada de la clase persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        #con super  podemos definir las propiedades de la clase heredada
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
        
    #si se crea una def con un nomrbe igual a la del padre, se toamra la de la clase hija
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        #con super  podemos definir las propiedades de la clase heredada
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
        
        


     
def saludar_1():
    #pass no hace nada , es apra dejar funciones sin hacer nada
    pass


roberto = Empleado("Roberto",23,"Chileno")

print(roberto.nombre)