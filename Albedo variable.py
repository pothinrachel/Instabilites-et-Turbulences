import numpy as np
import matplotlib.pyplot as plt

# Constantes ajustées
epsilon = 0.62  # émissivité de la surface terrestre
sigma_b = 5.67e-8  # constante de Stefan-Boltzmann
I_0 = 1361  # Constante solaire (en W/m^2)

a_1 = 0.3 #on fixe a_1 à l'albedo actuel de la Terre
b1_values = np.linspace(0.0001, 0.005, 500) #on fait varier b1, nous donne la sensibilité de l'albedo à la température


# fonction qui donne les états de base càd T*
def T(a_1, b_1):
    m = - I_0 * b_1 / (4 * epsilon * sigma_b)
    n = - I_0 * (1 - a_1) / (4 * epsilon * sigma_b)
    discriminant = m**2 - 4 * n
    T_pos = None
    T_neg = None
    if discriminant >= 0: #condition pour pouvoir calculer x1 et x2
        x1 = (m + np.sqrt(discriminant)) / 2
        x2 = (m - np.sqrt(discriminant)) / 2
        if x1 >= 0 : #condition pour pouvoir calculer T+
            T_pos = np.sqrt(x1)
        if x2 >= 0 : #condition pour pouvoir calculer T-
            T_neg = np.sqrt(x2)
    return T_pos, T_neg
        
# fonction qui nous donne sigma en fonction de T*
def sigma(T):
    return -4 * epsilon * sigma_b * T**3 + I_0 * b_1 / 2 * T

T_stable = []
T_instable = []
albedo_stable = []
albedo_instable = []

for b_1 in b1_values:
    T_pos, T_neg = T(a_1, b_1) # Calculer T* et sigma pour chaque valeur de b_1
    if T_pos is not None:
        sigma_pos = sigma(T_pos)
        #étude de la stabilité en étudiant le signe de sigma
        if sigma_pos < 0:
            albedo_pos = a_1 - b_1 * T_pos**2
            T_stable.append(T_pos)
            albedo_stable.append(albedo_pos)
        else :
            albedo_pos = a_1 - b_1 * T_pos**2
            T_instable.append(T_pos)
            albedo_instable.append(albedo_pos)
            

            
    if T_neg is not None:
        sigma_neg = sigma(T_neg)
        if sigma_neg < 0:
            albedo_neg = a_1 - b_1 * T_neg**2
            T_stable.append(T_neg)
            albedo_stable.append(albedo_neg)
        else :
            albedo_neg = a_1 - b_1 * T_neg**2
            T_instable.append(T_neg)
            albedo_instable.append(albedo_neg)

# Convertir les résultats en tableaux numpy
T_stable = np.array(T_stable)
T_instable = np.array(T_instable)
albedo_stable = np.array(albedo_stable)
albedo_instable = np.array(albedo_instable)

m = - I_0 * b_1 / (4 * epsilon * sigma_b)

# Tracer T* en fonction de l'albédo
plt.figure(figsize=(12, 8))
plt.plot(albedo_stable, T_stable, 'b', lw=1.5, label='Stable')
plt.plot(albedo_instable, T_instable, 'r', lw=1.5, label='Instable')

plt.xlabel('Albedo $\\alpha$')
plt.ylabel('Température $\\bar{T}$ (K)')
plt.title(f"Diagramme de bifurcation avec $a_1 = {a_1}$ fixe et $b_1$ variable")
plt.legend()
plt.grid(True)
#plt.savefig('Albedo variable.png')
plt.show()