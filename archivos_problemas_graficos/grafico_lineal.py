import pandas as pd

#para instalar pip -m install matplotlib
import matplotlib.pyplot as plt
#para instalar, en el CMD
#pip install seaborn
import seaborn as sns

#aca guardamos el dataframe
df = pd.read_csv("archivos_problemas_graficos\\saltos.csv")

#crea el grafico de linea segun la grafica 
sns.lineplot(x="fecha",y="saltos",data=df)

#creando un punto en el grafico
plt.plot("01-12",99,"o")

#muestra el grafico visualmente
plt.show()
#print(df)
