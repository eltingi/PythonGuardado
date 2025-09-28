#srp es: Single Responsibility Principle
#cada clase debe tener una unica razon para cambiar

class TanqueDeCombustible():
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
    def obtener_combustible(self):
        return self.combustible   
        
class Auto():
    def __init__(self,tanque):
        self.tanque = tanque
        self.posicion = 0

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("El auto se movio perfectamente")            
        else:
            print("No hay suficiente combustible para mover el auto en ls distancia solicitada")
            
    def obtener_posicion(self):
        return self.posicion

tanque = TanqueDeCombustible()
auto = Auto(tanque)

print(auto.obtener_posicion())
auto.mover(10)
print(auto.obtener_posicion())
auto.mover(20)
print(auto.obtener_posicion())
auto.mover(200)
print(auto.obtener_posicion())
