lista = list(["Hola","mauri",34,True])

#len devuelve cantidad de elementos a la lista
cantidad_elementos = len(lista)

#append: agregando un elemento a la lista
lista.append("listaagregadocampo")

#insert: agregando un elemento a la lista en un indice especifico
lista.insert(1,"inserta ")

#extend: agrega varios elementos a  la lista al mismo tiempo

lista.extend(["Primer extend 1","Segundo extend 2"])

#pop:  elimnando un elementos de la lista, segun un indice

print(len(lista))

lista.pop(0)

#eliminando un elemento de la lsta con -1 , indica que queire el ultimo, -2 el ante ulñtimo
lista.pop(-2)


#REMOVE, remueve un elemento de la lista por su valor
lista.remove("mauri")

print(len(lista))



#clear: elimina todos los elemetnos de la lista.
lista.clear()


#sort ordena la lista segun valor y tipo de valor asecendente (si usamos el parametyro reverse=true lo ordena en reversa(desendente))
lista2 = list([2,3,56,23,4])
lista2.sort()
print(lista2)


lista3 = list([2,3,56,23,4])
lista3.sort(reverse=True)
print(lista3)


#invirtiendo los elementos de una lista., los cambia de lado
lista_reverse = list([2,3,56,23,4])

lista_reverse.reverse()



#index, para verificar si un elemento se enceutnra en la lista, y devuelve su index
lista_para_index = list([2,3,56,23,4])

elemento_buscado = lista_para_index.index(56)

print(elemento_buscado)



