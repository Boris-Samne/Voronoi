import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définir la fonction f(x, y) = x^2 - y^2
def f(x, y):
    return x**2 - y**2

# Créer une grille de points (x, y)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calculer les valeurs de z
z = f(x, y)

# Créer la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface
ax.plot_surface(x, y, z, cmap='viridis')

# Ajouter des étiquettes aux axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')

# Ajouter un titre
ax.set_title('Représentation de la fonction f(x, y) = x^2 - y^2')

# Afficher la figure
plt.show()
