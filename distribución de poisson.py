import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
lambda_poisson = 2
x = np.arange(0, 15)
pmf = poisson.pmf(x, lambda_poisson)
plt.figure(figsize=(8,5))
plt.bar(x, pmf, color='skyblue', edgecolor='black')
plt.title(f'Distribución de Poisson (λ={lambda_poisson})')
plt.xlabel('Número de eventos')
plt.ylabel('Probabilidad')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()