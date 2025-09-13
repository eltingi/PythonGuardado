class Estudiante:
    def __init__(self,nombre_p,edad_p,grado_p ):
        self.nombre = nombre_p        
        self.edad = edad_p
        self.grado = grado_p
        
        #todos los m etodos deben tener el self
    def estudia(self):
        print(f"Hola estoy estudiando")
            
            
nombre = input("Digame su nombre :")
edad = input("Edad papito lindo:")
grado = input("Dime tu grado :")

estudiante_1 = Estudiante(nombre,edad,grado)

print(f"""
      Datos del estudiante: \n\n
      Nombre: {estudiante_1.nombre} \n
      Edad: {estudiante_1.edad} \n
      Grado: {estudiante_1.grado} \n     
      
      """)

#Estudiante1 = Estudiante("Mauricio",23,10)





while True:
    estudiar = input("Dime:")
    if (estudiar == "1"):
        estudiante_1.estudia()
 
 