import pandas as pd #universalmente se le compbra pd a panda 

#imprimo ´para saber el tipo, modulo
#print(type(pd))

#esto en si es un dataframe , la parte del codigo names, no es obligartoria, peor se encarga de agregar encabezados cuando la data recibida no tiene encabezado
#df = pd.read_csv("archivos\\datos.csv"),names=["name","lastname","age"]
df = pd.read_csv("archivos\\datos.csv")
df_2 = pd.read_csv("archivos\\datos.csv")
#print(df)

nombres = df["nombre"]

print(nombres)

#<class 'pandas.core.frame.DataFrame'>
print(type(df))

#TAMBIEN SE PUEDE TRABAJAR CON JUPYTER NOTEBOOK, HERRAMIENTA

#slicing
cadena = "0123456789"
#aqui indico el slicing m el cual con : toma un rango segun el index dfe la posicion
print(cadena[2:7])

#aqui lo muestro ordenado por edad y lo im,primo
#print(df.sort_values("edad"))

#se puede ordenar con un ascending = false , donde en forma automatica esta en true
#decendente false
df_ordenado_decentente = df.sort_values("edad",ascending=False)
df_ordenado_ascendente = df.sort_values("edad")
print(df_ordenado_decentente)

#tenemos la posibilidad de concatenar distintos dataframe
df_concatenado = pd.concat([df,df_2])

print(df_concatenado)

#muestra segun el indice las filas del dataframe, es decir en este casom, si pongo 3 mostrara las filas del 0 al 3
primeras_fila = df.head(3)

#muestra segun el indice las filas del dataframe, es decir en este casom, si pongo 3 mostrara las filas del 0 al 3
ultimas_fila = df.tail(3)

print("--------------primeras filas ------------------------------")
print(primeras_fila)

print("--------------ultimas filas ------------------------------")
print(ultimas_fila)


#accediendo a la cantidad de filñas y columnas con shape, esto devuelve una tupla por po que necesito 2 valores para recibir
filas_totales,columnas_totales = df.shape


#obteniendo data estadistica del datframe:
df_info = df.describe()

print(df_info)


#loc
#accediendo a un elemento especifico con df con loc
#el cual se le indica el indice de fila y el nombre de la columna
elemento_especifico_loc = df.loc[2,"edad"]

print(elemento_especifico_loc)

#iloc pide por indice de columna
elemento_especifico_iloc = df.iloc[2,2]

print(elemento_especifico_iloc)

#aqui ultilizamnos loc para traer todos los apellicos con el nombre de la columna
# el : sinfica que estoy utilziando el slicing pero de todos los valores
apellidos_loc = df.loc[:,"apellido"]

print(f"Apellidos con loc: \n{apellidos_loc}")


apellidos = df.iloc[:,1]

print(f"Apellidos con iloc: \n{apellidos}")



### ejemplos de accedo loc y iloc #################slicing##########################
##ambos funcionan igual

#accediendo a una fila en particular con loc
fila_3 = df.loc[2,:]

print(fila_3)
#accediendo a una fila en particular con iloc
fila_3 = df.iloc[2,:]

print(fila_3)

###fin ejemplos de accedo loc y iloc ########################################

#accediendo a un elemento especifico del df con loc
#elemento_especifico_loc = df.loc[2,"edad"]


#este ejemplo es importante para entender el alcance que tiene loc y iloc importante lo usare mucho
#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(f"traeme los mayor que 30: \n {mayor_que_30}")





print("ejericio ms 1")

accediendo_matias = df.loc[2,:]

print(accediendo_matias)

print("ejericio ms 2")

accediendo_edad = df.loc[1,"edad"]

print(accediendo_edad)