import pandas as pd

#para instalar pip -m install matplotlib
import matplotlib.pyplot as plt
#para instalar, en el CMD
#pip install seaborn
import seaborn as sns

#aca guardamos el dataframe
df = pd.read_csv("archivos_problemas_graficos\\ms_ingresos.csv")

#crea el grafico de linea segun la grafica 
sns.barplot(x="fuente",y="ingresos",data=df)


total_ingresos = df["ingresos"].sum()

#mostramos total
print(f"El total de ingresos es de : ${total_ingresos} USD")
#muestra el grafico visualmente
plt.show()
#print(df)
