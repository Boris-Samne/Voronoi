import numpy as np  # Importation de la bibliothèque NumPy pour les calculs numériques
import matplotlib.pyplot as plt  # Importation de Matplotlib pour la visualisation
import math  # Importation de la bibliothèque mathématique standard de Python

# Nombre de points
num_points = 10  # Définir le nombre de points aléatoires à générer

# Générer des points aléatoires
points = np.random.rand(num_points, 2)  # Générer 'num_points' points aléatoires dans un plan 2D (chaque coordonnée entre 0 et 1)

# Paramètres de la grille
grid_size = 500  # Définir la taille de la grille, c'est-à-dire le nombre de points de la grille dans chaque dimension (x et y)

# Générer une grille de points
x = np.linspace(0, 1, grid_size)  # Générer 'grid_size' points uniformément répartis entre 0 et 1 pour l'axe x
y = np.linspace(0, 1, grid_size)  # Générer 'grid_size' points uniformément répartis entre 0 et 1 pour l'axe y
X, Y = np.meshgrid(x, y)  # Créer une grille de coordonnées en combinant x et y
grid_points = np.c_[X.ravel(), Y.ravel()]  # Aplatir les matrices X et Y en une liste de points 2D

# Calculer les distances et trouver l'indice du point le plus proche
# Pour chaque point de la grille, calculer la distance euclidienne à chaque point aléatoire
distances = np.sqrt(((grid_points[:, None, :] - points[None, :, :]) ** 2).sum(axis=2))
# Trouver l'indice du point aléatoire le plus proche pour chaque point de la grille
closest_points = np.argmin(distances, axis=1)

# Reshaper l'indice des points les plus proches à la forme de la grille
voronoi_cells = closest_points.reshape(grid_size, grid_size)  # Reshape la liste des indices pour qu'elle corresponde à la grille 2D

# Visualiser le diagramme de Voronoï
plt.imshow(voronoi_cells, extent=(0, 1, 0, 1), origin='lower', cmap='tab20')  # Afficher les cellules de Voronoï avec une palette de couleurs
plt.scatter(points[:, 0], points[:, 1], color='red')  # Ajouter les points aléatoires sur le diagramme en rouge
plt.title("Diagramme de Voronoï")  # Ajouter un titre au diagramme
plt.show()  # Afficher le diagramme
