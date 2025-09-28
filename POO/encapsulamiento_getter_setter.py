class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    #esto es una muestra de como se realiza en otros lenguajes de programacion
    #getter
    def get_nombre(self):
        return self.__nombre
    #setter
    def set_nombre(self,nombre):    
        self.__nombre = nombre
        
      
                
mabri = Persona("Mauriii",30)


print(mabri.get_nombre())


