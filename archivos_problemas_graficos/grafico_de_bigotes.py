import pandas as pd

#para instalar pip -m install matplotlib
import matplotlib.pyplot as plt
#para instalar, en el CMD
#pip install seaborn
import seaborn as sns

#aca guardamos el dataframe
df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#crea el grafico segun la grafica 
sns.boxplot(x="categoria",y="valor",data=df)


#muestra el grafico visualmente
plt.show()
#print(df)

