class Persona: 
    def __init__(self,nombre,correo,nick):
        self.nombre = nombre
        self.correo = correo
        self.nick = nick
        
    def presentacion(self):
        print(f"""
              Hola soy la persona:{self.nombre} 
              Me gusta llamarme {self.nick}
              """)
        


Personita = Persona("Mauricio","@","MS")

Personita.presentacion()
        
    
        