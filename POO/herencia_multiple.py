class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        def hablar(self):
            print("Hola raton con cola")
        
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
    def mostrar_habilidad_return(self):
        return f"Mi habilidad es: {self.habilidad}"

#ejemplo de herencia multiple 
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,salario,empresa,habilidad):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        return f"{super().mostrar_habilidad()}"
    
    def presentarse_mas_completo(self):
        print (f"Hola man yo soy {self.nombre} y {super().mostrar_habilidad_return()}")


     
def saludar_1():
    #pass no hace nada , es apra dejar funciones sin hacer nada
    pass


roberto = EmpleadoArtista("Roberto",23,"Chileno",200000,"Empresita","Saltar")




roberto.presentarse()

roberto.presentarse_mas_completo()


#metodos para saber la isntancia y subclase

cristiano = Artista("Cantar")

#herencia pregunta si la clase hereda de otra clase
herencia = issubclass(EmpleadoArtista,Artista)
#true
herencia_2 = issubclass(EmpleadoArtista,Persona)
#true
herencia_3 = issubclass(Persona,EmpleadoArtista)
#false

#instancia regunta si el objeto petenece a una clase segunsu herencia
instancia = isinstance(roberto,EmpleadoArtista)
instancia_2 = isinstance(roberto,Artista)
instancia_3 = isinstance(cristiano,Persona)


print("HERENCIA: \n")
print(herencia)
print(herencia_2)
print(herencia_3)

print("instancia: \n")
print(instancia)
print(instancia_2)
print(instancia_3)