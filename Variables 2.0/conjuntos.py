
#en el set van datos que no se pueden modificar
#una list siempre es mutable se puede acceder y modificar

conjunto = set(["dato 1 ","dato2",3])

#metiendo un conjunto en otro conjunto, no se pueden meter list, ni diuccionarios por que es unhashable
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

#print(conjunto2)

#teoria de conjuntos 
#revisa si la data de 1 conjunto se encuentra en el otro, porm lo que seria un subconjunto
#es decir conjunto4 es un subconjunto de conjunto3 ya que tiene todo los valores del conjunto 3.

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#dos formas validas de verificar si es un subconjunto
resultado =  conjunto4.issubset(conjunto3)
resultado =  conjunto4 <= conjunto3


#dos formas validas de verificar si es un superjunto
resultado =  conjunto4.issuperset(conjunto3)
resultado =  conjunto4 > conjunto3

#verificar si hay algun datoq ue sea distinto , si todo es distinto es true , si no false
resultado = conjunto4.isdisjoint(conjunto3)

print(resultado)