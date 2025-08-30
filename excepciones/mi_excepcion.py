#cr4ando mi propia excepcion pérsonalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Wow, cometiste el siguiente error: {err}")
        
#lanzando el error propio
try:
    #palabra clave para lanzar errores
    raise MiExcepcion("comom te equivocas")
except:
    print("Holii")
    

