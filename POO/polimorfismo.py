class Gato():
    def sonido(self):
        return "Miau"
    
    
class Perro():
    def sonido(self):
        return "Guau"

#aqui aplico polimorfismo
#aqui recibe por parametro el objeto
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(perro)

#aqui si cambio a perro igual toma el metodo, este es otro tipo de polimorfismo
print(gato.sonido())

