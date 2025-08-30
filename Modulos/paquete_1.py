import paquete

#nos indica que es un modulo, pero para pytho si tiene la carpeta __init__
print(type(paquete))


#si lanzo el codigo con el ejemplo de mas abajo tirara une excepcion por que no encuentra el atributo de path
#como el enrutamiento no encuentra el path por que es un paquete
#print(paquete.__path__) 

print(paquete.__path__)



