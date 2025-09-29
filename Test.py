import numpy as np
import matplotlib.pyplot as plt
import os

# Génération des données
x = np.linspace(-10, 10, 400)   # 400 points entre -10 et 10
y = x**2

# Création du graphique
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="y = x^2")
plt.title("Courbe de y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Chemin complet pour sauvegarder l'image
output_path = "/Users/robinguichon/Desktop/MattApp/Git/Test/x2_plot.png"

# Crée le dossier si jamais il n'existe pas
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Sauvegarde l'image
plt.savefig(output_path)

# Affiche la courbe
plt.show()

print(f"Graphique sauvegardé dans : {output_path}")
