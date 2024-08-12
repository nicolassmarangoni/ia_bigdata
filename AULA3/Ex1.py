import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

dados_x = np.linspace(0,10,10)
dados_y = dados_x * dados_x

plt.figure(figsize=(10, 5), facecolor='gray')
ax = plt.axes()
ax.set_facecolor('white')
plt.plot(dados_x, dados_y,
         color='red', linewidth=2,  # Adicionei um valor para linewidth
         marker='o', linestyle='--',  # 'dashed' substituído por '--' para linha tracejada
         markeredgecolor='black')
plt.show()