import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
calificacion = np.array([50, 55, 60, 62, 65, 70, 74, 78, 85, 90])

pendiente, intercepto, r_value, p_value, std_err = stats.linregress(horas_estudio, calificacion)

def modelo_lineal(x):
    return pendiente * x + intercepto
predicciones = modelo_lineal(horas_estudio)

print("Ecuación de la recta:")
print(f"y = {pendiente:.2f}x + {intercepto:.2f}")
print(f"Coeficiente de correlación (R): {r_value:.2f}")

plt.scatter(horas_estudio, calificacion, color='blue', label='Datos reales')
plt.plot(horas_estudio, predicciones, color='red', label='Regresión lineal')
plt.xlabel('Horas de estudio')
plt.ylabel('Calificación')
plt.title('Regresión Lineal: Horas de estudio vs Calificación')
plt.legend()
plt.grid(True)
plt.show()
