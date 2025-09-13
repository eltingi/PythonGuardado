#aqui usamos Pascal Case
class Celular:
    #constructor de la clase de sus atributtos
    #__inir__ es un metodo especial
    # python siempre busca este metodo
    def __init__(self,marca,modelo,camara):
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    #metodo
    #todaas las funcioones que estan dentro de una clase se llaman metodo
    #los metodos deben recibir el objeto al cual pertenecen, es por eso que tiene que tener parametro self
    #asi el objeto se autoreferencia
    #sino dan error:Celular.cortar() takes 0 positional arguments but 1 was given
    def llamar(self):
        print(f"Llamando desde un {self.modelo}")
        
    def cortar(self):
        
        print(f"Cortando por lagi desde un {self.modelo}")
        
#lew asigno las propiedades a la clase
celular1 = Celular("Samsung","S24+","48MP")

celular1 = Celular("Xiomi","XPOCO 10","128MP")


#print(celular1) 
#retorna <__main__.Celular object at 0x000001BA6F496FD0>
#el cual representa que es un objeto de Celular, y que viene de __main__
# , haciendo referencia a que viene desde este mismo modulo

print(celular1.marca) 
       
celular1.llamar()
celular1.cortar()
       
        
    