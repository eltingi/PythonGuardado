#build in , se llama la utilizacion de las funciones ya creadas dentro del lenguage de programacion python




#encontrado el numero mas grande mayor de uyna lista

numeros = [5,12,124,2]

numero_mas_alto = max(numeros)

#print(f"{numero_mas_alto}  alto")

numero_mas_pequeno = min(numeros)

#print(f"{numero_mas_pequeno} bajo")


#redondeando decimales
numero = round(15.4342342352,2) 

print(numero)

#bool , tranforma boleado cualquier tipo de dato
resultado_bool = bool("")

resultado_bool_2 = bool("hola")
#retornar false -> vacion,false ,none \true -> distinto a 0 ,cadena, datos no vacion

print(resultado_bool)
print(resultado_bool_2)

#all
#retorna true, si todos los valores son verdaderos
resultado_all = all([1,"hola",["MS","XS"]])

print(f"{resultado_all} resultado_all" )


#SUM
#suma todos los valores q tiene un iterable, siempre y cuando tenga solo numeros
# , si tiene otro dato tirara error (excepcion)

suma_total = sum(numeros)

print(suma_total)


