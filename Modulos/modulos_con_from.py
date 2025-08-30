
#aqui llamamos solamente a la funcion especifica y no me traigo el modulo entero
#tambiemn podemos renombrar (dar alias) a los metodo llamados
from modulo_saludar import saludar as saludale,saludar_mal 

#creamos las variable cpon los saludos
saludo = saludale("MS 2") #metodo saludar de modulo_saludar
print(saludo)

#prueba de otro modo
saludo = saludar_mal("MS 2")
print(saludo)


print(m_s