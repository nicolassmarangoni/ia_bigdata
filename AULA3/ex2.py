import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dado_x = np.linspace(0, 10, 10)
dados_y = dado_x * 2  


plt.figure(figsize=(10, 5), facecolor='gray')
ax = plt.axes()
ax.set_facecolor('white')
plt.plot(dado_x, dados_y, color='red', linewidth=2, marker='o', linestyle='--', markeredgecolor='black')
plt.xlabel("Eixo X")  
plt.ylabel("Eixo Y")  
plt.title("Exemplo Matplotlib", fontsize=12)


plt.rcParams.update({'font.size': 15})
plt.figure(figsize=(12, 12))  


linhas, colunas = 2, 2 

plt.subplot(linhas, colunas, 1)
plt.plot(dado_x, 'r--')
plt.title("Gráfico 1")

plt.subplot(linhas, colunas, 2)
plt.plot(dado_x ** 2, 'b-.')
plt.title("Gráfico 2")

plt.subplot(linhas, colunas, 3)
plt.plot(dado_x / 2, 'c-.')
plt.title("Gráfico 3")

plt.tight_layout()  

plt.show()  
