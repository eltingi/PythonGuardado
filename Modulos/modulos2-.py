
#IMPORTANDO FUNCIONES COMO SI EL MODULO ESTUVIERA DENTRO DE LA MISMA CARPETA

import Modulos.saludar

print(Modulos.saludar.saludar("MSSSSS"))


import sys
#un modulo(build-in) es un modulo creado por un tercero, es decir que no esta desarrollado por ti,
#en python y los lenguages existen metodos que son propios ya del lenguage
print(sys) #retorna <module 'sys' (built-in)> , lo que indica que es un modulo (build-in)
print(Modulos.saludar) #retorna que es de typo modulo y que viee desde mi equipo

print(sys.path)


