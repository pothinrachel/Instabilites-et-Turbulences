import numpy as np
import matplotlib.pyplot as plt

# Constantes
epsilon = 0.62  # émissivité de la surface terrestre
sigma_b = 5.67e-8  # constante de Stefan-Boltzmann
I_0 = 1361  # Constante solaire (en W/m^2)

# fonction qui donne les états de base càd T*
def T(a):
    return ((I_0*(1 - a)) / (4 * epsilon* sigma_b)) ** 0.25

# fonction qui nous donne sigma enfonction de T*
def sigma(T):
    return -4 * epsilon* sigma_b * T**3

albedo = np.linspace(0, 1, 500)  # l'albedo constant varie entre 0 et 1
T_values = []
sigma_values = []

# on calcule T* et sigma pour chaque valeur de l'albedo
for a in albedo:
    T_eq = T(a)
    T_values.append(T_eq)
    sigma_values.append(sigma(T_eq))

# on convertit les résultats en tableaux
T_values = np.array(T_values)
sigma_values = np.array(sigma_values)

# on définit les conditions de stabilité
stable = sigma_values < 0
instable = sigma_values > 0

#on trace T* en fonction de l'albedo

plt.figure(figsize=(12, 8))
plt.plot(albedo[stable], T_values[stable], 'b', lw=1.5, label='Stable')
plt.plot(albedo[instable], T_values[instable], 'r', lw=1.5, label='Instable')

plt.xlabel('Albedo $\\alpha$')
plt.ylabel('Température $\\bar{T}$ (K)')
plt.title("Diagramme de bifurcation de la température d'équilibre en fonction de l'albedo")
plt.legend()
plt.grid(True)
#plt.savefig('Albedo constant')
plt.show()

