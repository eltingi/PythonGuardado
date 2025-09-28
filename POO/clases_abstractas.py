
#ayuda IA:

#una clase abstracta es una clase que no puede ser instanciada, es decir, no se pueden crear objetos de esa clase
#pero si se pueden crear clases que hereden de esa clase abstracta y esas clases si pueden ser instanciadas
#para crear una clase abstracta en python se utiliza el modulo abc (abstract base class)

#implementacion es Implementación es el proceso de transformar un diseño, especificación o plan en algo real y funcional.


#abstractmethod, es un decorador que se utiliza para indicar que un método es abstracto,
# es decir, que no tiene una implementación en la clase base 
# y debe ser implementado en las clases derivadas.

#cuando aseguro que una clase es abstracta, estoy asegurando que esa clase no puede ser instanciada
#y que las clases que hereden de esa clase deben implementar los 
# métodos abstractos definidos en la clase base.

#uno se asegura del polimorfismo, ya que todas las clases que hereden de la clase abstracta
#deben implementar los métodos abstractos, y por lo tanto, se puede utilizar el mismo

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.sexo}")
  
# ahorea no puedo crear un objeto de la clase Persona ya que da error de excepcion      
#yo = Persona("Mauricio",30,"Masculino")
#pero si puedo crear una clase que herede de Persona y esa clase si puede ser instanciada
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    #este metodo debe estar si o si por que es abstracto en la clase base  
    def hacer_actividad(self):
        print(f"Estoy estudiando en {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    #este metodo debe estar si o si por que es abstracto en la clase base  
    def hacer_actividad(self):
        print(f"Estoy trabajando en {self.actividad}")
        

mauri  = Estudiante("Mauricio",30,"Masculino","Estudiar")
mauri.presentarse()
mauri.hacer_actividad()

otro_man = Trabajador("Juan",40,"Masculino","Trabajando en una empresa genial")
otro_man.presentarse()
otro_man.hacer_actividad()




