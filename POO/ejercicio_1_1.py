class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El mamifero esta amamantando")
        
    
ave = Ave()

animal_mamifero = Mamifero()

animal_mamifero.comer()


    