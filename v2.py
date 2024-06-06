import numpy as np
import math
import matplotlib.pyplot as plt

# Nombre de points
num_points = 10

# Génération de points aléatoires
points = np.random.rand(num_points, 2) * 100  # points dans un carré de 100x100

# Taille de la grille
grid_size = 500

# Initialisation de la grille
grid = np.zeros((grid_size, grid_size))

# Calcul des distances pour chaque point de la grille
for i in range(grid_size):
    for j in range(grid_size):
        min_dist = float('inf')
        min_index = -1
        for k in range(num_points):
            dist = math.sqrt((i - points[k, 0])**2 + (j - points[k, 1])**2)
            if dist < min_dist:
                min_dist = dist
                min_index = k
        grid[i, j] = min_index

# Affichage du diagramme de Voronoï
plt.imshow(grid, cmap='tab20', extent=(0, 100, 0, 100))
plt.scatter(points[:, 0], points[:, 1], color='red')
plt.title("Diagramme de Voronoï")
plt.show()