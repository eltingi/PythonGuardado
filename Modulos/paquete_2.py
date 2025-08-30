
#si existe un modulo con el mismo nombre que el paquete, siempre se le da prioridad al paquete
#recordar que en la carpeta debe existir el : __init__.py
import paquete.saludar_malo

print(paquete.saludar_malo.saludar_mal("Mauri"))

print(paquete.saludar_malo.saludar_mal("Mauri"))
#print(paquete.saludar_malo("Mauriii"))

