import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy

estados = ('São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo')
indice = numpy.arange(len(estados))
numeros = [5406, 4271, 11473, 234]
plt.bar(indice, numeros, color='coral')
plt.xticks(indice, estados)
plt.ylabel('Número de incêndios')
plt.title('Número de incêndios florestais na região sudeste do Brasil no ano de 2017')
plt.show()

labels = 'Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'
sizes = [234, 11473, 4271, 5406]
colors = ['lightgrey', 'red', 'orange', 'coral']
plt.title('Porcentagem de incêndios na região sudeste do Brasil no ano de 2017')
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.show()

fig, gnt = plt.subplots()
plt.title('Número de incêndios florestais em São Paulo no ano de 2017')
gnt.set_ylim(0, 220)
gnt.set_xlim(0, 3000)
gnt.set_xlabel('Número de incêndios')
gnt.set_ylabel('Meses')
gnt.set_yticks([20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240])
gnt.set_yticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', ' '])
gnt.grid(True)
gnt.broken_barh([(0, 28)], (15, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 107)], (35, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 103)], (55, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 41)], (75, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 43)], (95, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 217)], (115, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 802)], (135, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 981)], (155, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 2868)], (175, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 179)], (195, 10), facecolors =('tab:red'))
gnt.broken_barh([(0, 37)], (215, 10), facecolors =('tab:red'))
plt.show()


estados = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'SE', 'SC', 'ES', 'MG', 'RJ', 'SP', 'DF', 'GO', 'MT']
regioes = ['Norte', 'Norte', 'Norte','Norte', 'Norte', 'Norte', 'Norte', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste','Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Sul', 'Sudeste', 'Sudeste','Sudeste', 'Sudeste', 'Centro-Oeste', 'Centro-Oeste', 'Centro-Oeste']
incendios = [7042, 1465, 14798, 59771, 10614, 1101, 20997, 159, 8249, 2555, 2861, 4757, 522, 9478, 75, 2354, 234, 11473, 4271, 5406, 410, 8705, 42303]
df = pd.DataFrame(dict(estados=estados,regioes=regioes,incendios=incendios))
df["all"] = "all"
fig = px.treemap(df,path=[regioes,estados],values=incendios)
fig.show()
