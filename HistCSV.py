#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plot
 
df = pd.read_csv("players_stats.csv")
df.head()
plot.hist(x=df.loc[:, 'Height'], color='#F2AB6D', rwidth=0.85)
plot.title('Histograma alturas jugadores')
plot.xlabel('Alturas')
plot.ylabel('Frecuencia')
plot.show() #dibujamos el histograma

