import numpy as np  # Importation de la bibliothèque NumPy pour les calculs numériques
import matplotlib.pyplot as plt  # Importation de Matplotlib pour la visualisation

# Nombre de points aléatoires à générer
num_points = 10

# Générer des points aléatoires dans un espace 2D
points = np.random.rand(num_points, 2)

# Définir la taille de la grille pour la visualisation
grid_size = 500

# Créer une grille de points couvrant l'espace 2D de 0 à 1
x = np.linspace(0, 1, grid_size)  # Points uniformément répartis sur l'axe x
y = np.linspace(0, 1, grid_size)  # Points uniformément répartis sur l'axe y
X, Y = np.meshgrid(x, y)  # Créer une grille de coordonnées en combinant x et y
grid_points = np.c_[X.ravel(), Y.ravel()]  # Aplatir les matrices X et Y en une liste de points 2D

# Calculer les distances entre chaque point de la grille et les points aléatoires
# Utiliser la distance euclidienne pour mesurer les distances
distances = np.sqrt(((grid_points[:, None, :] - points[None, :, :]) ** 2).sum(axis=2))

# Trouver l'indice du point aléatoire le plus proche pour chaque point de la grille
closest_points = np.argmin(distances, axis=1)

# Reshaper l'indice des points les plus proches à la forme de la grille
voronoi_cells = closest_points.reshape(grid_size, grid_size)

# Visualiser le diagramme de Voronoï
plt.imshow(voronoi_cells, extent=(0, 1, 0, 1), origin='lower', cmap='tab20')  # Afficher les cellules de Voronoï
plt.scatter(points[:, 0], points[:, 1], color='red')  # Ajouter les points aléatoires sur le diagramme en rouge
plt.title("Diagramme de Voronoï")  # Ajouter un titre au diagramme
plt.show()  # Afficher le diagramme
