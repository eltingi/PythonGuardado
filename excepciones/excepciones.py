
#prueba de try catch
def suma_numero_try():
    a = input("Numero 1: ")
    b = input("Numero 2: ")
    #espera un numero en base de 10 es decirt los numeros del 0-9 .
    
    try:
        resultado = int(a) + int(b)
        print(resultado)
    except:
        print("dame un numero")

#suma_numero_try()



#crean funcion para sumar 2 numeros , el cual tendra un bucle while donde si lanza excepcion seguira funcionando 
def suma_dos():
    #iniciando el bucle
    while True:            
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #espera un numero en base de 10 es decirt los numeros del 0-9 .
        #se convierten en enteros y se suman, si no como vienen en texto concatenera XD
        try:
            resultado = int(a) + int(b)    
            #si lanzo excepcion, pedirle que reingrese los datos  
            
            #escept se púeden usar mas de uno ejemplos:   
        except ZeroDivisionError:            
            print("No dividas por cero")  
        #except Exception as ex:            
            #print(ex)
        except ValueError as e:   
            print("dame un numero") 
            print(f"Error: {e}")
        #except :          
            #print("dame un numero")
            #recordar que el else: se ejecuta solo si NO ocurrió ningún error en el try.
            #es decir que si el else se ejecuta no se ejecuta el except, si el except se ejecuta no se ejecuta else
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")
            
    return resultado

print(suma_dos())
