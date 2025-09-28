# Ejemplo de abstracción en POO
# La abstracción se refiere a la capacidad de enfocarse en los aspectos esenciales de un objeto
# y ocultar los detalles innecesarios. En este ejemplo, la clase Auto abstrae el concepto de un auto
# y proporciona métodos para interactuar con él sin exponer los detalles internos.


class Auto():
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self.estado = "encendido"
        print("El auto está encendido")
        
    def conducir(self):
        if self.estado == "apagado":
            #aqui se abstrae el detalle de que el auto debe estar encendido para conducir
            self.encender()               
        print("Conduciendo el auto")
        
        
mi_auto = Auto()
mi_auto.conducir()