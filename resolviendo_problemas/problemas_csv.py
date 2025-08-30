#cambiando el tipo de datos de una columna

import pandas as pd
#optengo el dataframe
df = pd.read_csv("resolviendo_problemas\\datos.csv")
print(df)

#convirtiendo a string un valor de una columna numero
#aqui estamos convirtiendo todos los datos de la columna
df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))
print(df["edad"][0])

#eliminando las filas con datos faltantes
#aqui se le puede agregar o decir si quiero eliminar no solo la fila con datos faltantes, tamboien una columna entera si llega a faltar un dato, es muy especifico este ultimo caso si
df = df.dropna()


#eliminado filas repetidas
print(df)
df = df.drop_duplicates()
print("Datos duplicados eliminados\n")
print(df)

#creando un nuevo CSV cone ld ataframe resuelto limpio
df.to_csv("resolviendo_problemas\\datos_2.csv")






