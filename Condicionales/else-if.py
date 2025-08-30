ingreso_mensual =  12000


#if normales

if ingreso_mensual > 10000:
    print("Estas")
elif ingreso_mensual > 100:
    print("Estas bien en latinoamerica")    
else:
    print("muy mal")  
    
    
#if dentro de otro if ( IF ANIDADOS)
ingreso_mensual =  11111

if ingreso_mensual > 10000:
    print("Sobre 10000")
    if ingreso_mensual > 11000:
        print("Estas mas bien q 10000")
elif ingreso_mensual > 100:
    print("Estas bien en latinoamerica")    
else:
    print("muy mal")  