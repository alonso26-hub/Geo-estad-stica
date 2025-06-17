import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

print("Introduce los datos de la Muestra 1 separados por comas:")
muestra1 = list(map(float, input().split(',')))

print("Introduce los datos de la Muestra 2 separados por comas:")
muestra2 = list(map(float, input().split(',')))

media1 = np.mean(muestra1)
media2 = np.mean(muestra2)
s1 = np.std(muestra1, ddof=1)
s2 = np.std(muestra2, ddof=1)
n1 = len(muestra1)
n2 = len(muestra2)

diff = media1 - media2
se = np.sqrt((s1**2)/n1 + (s2**2)/n2)

df = ((s1**2/n1 + s2**2/n2)**2) / (((s1**2/n1)**2)/(n1-1) + ((s2**2/n2)**2)/(n2-1))
t_crit = stats.t.ppf(0.975, df)

ic_inf = diff - t_crit * se
ic_sup = diff + t_crit * se

print("\n--- RESULTADOS ---")
print(f"Media Muestra 1: {media1:.4f}")
print(f"Media Muestra 2: {media2:.4f}")
print(f"Diferencia de medias: {diff:.4f}")
print(f"Intervalo de confianza al 95%: ({ic_inf:.4f}, {ic_sup:.4f})")

plt.figure(figsize=(8, 4))
plt.errorbar(x=diff, y=0, xerr=[[diff - ic_inf], [ic_sup - diff]], fmt='o', color='blue', ecolor='red', capsize=5)
plt.axvline(x=0, color='gray', linestyle='--', label='Línea de referencia (0)')
plt.title('Intervalo de Confianza del 95% para la Diferencia de Medias')
plt.xlabel('Diferencia de medias')
plt.yticks([])
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
