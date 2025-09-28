class MiClase:
    def metodo(self, funcion):
        def wrapper():
            print("Hola antes por decorador")
            return funcion()
        return wrapper


mauri = MiClase()

@mauri.metodo
def funcion_a_decorar():
    print("Hola soy la funcion a decorar")


funcion_a_decorar()