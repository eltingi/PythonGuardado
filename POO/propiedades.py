
#las propiedades son una forma de encapsular atributos y metodos
#de una clase, de forma que se pueda acceder a ellos como si fueran atributos

#getters,setters y deleters
#los getters son metodos que permiten obtener el valor de un atributo privado

#esta es forma para que a nivel de programacion no se pueda modificar un atributo
#pero si se pueda acceder a su valor a traves de un metodo getter
#y si se quiere modificar a traves de un metodo setter

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    #esto es una muestra de como se realiza en otros lenguajes de programacion
    #getter
    @property
    def get_nombre(self):
        return self.__nombre    
    
    @property
    def nombre(self):
        return self.__nombre    
    
    #setter
    @nombre.setter
    def nombre(self,nombre):    
        self.__nombre = nombre
    
    #lo generado con decoradores, no es una sobre carga de metodos, es una forma de encapsular  
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
       

mabri = Persona("Mauriii",30)

#este es un ejemplo de excepcion que se genera al intentar modificar un atributo privado
#property 'nombre' of 'Persona' object has no setter
#mabri.nombre = "Mauricio"


print(mabri.nombre)

#print(mabri.get_nombre)

mabri.nombre = "Mauricio"

print(mabri.nombre)

del mabri.nombre

#si quiero revisar el atributo eliminado, em dara una excepcion
#'Persona' object has no attribute '_Persona__nombre'
#print(mabri.nombre)


