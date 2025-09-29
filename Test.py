import numpy as np
import matplotlib.pyplot as plt
import os

# Génération des données
x = np.linspace(-10, 10, 400)

# Création du graphique
plt.figure(figsize=(8, 6))

# Tracer x^k pour k = 1 à 5
for k in range(1, 6):
    y = x**k
    plt.plot(x, y, label=f"y = x^{k}")

plt.title("Courbes de y = x^k pour k = 1 à 5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# Chemin de sauvegarde
output_path = "/Users/robinguichon/Desktop/MattApp/Git/Test/xk_plots.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Sauvegarde
plt.savefig(output_path)

# Affiche
plt.show()

print(f"Graphique sauvegardé dans : {output_path}")
