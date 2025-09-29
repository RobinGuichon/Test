import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# Dossier de sauvegarde
output_dir = "/Users/robinguichon/Desktop/MattApp/Git/Test"

# Supprime tout le dossier Test s'il existe, puis le recrée vide
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

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

# Chemin de sauvegarde de l’image
output_path = os.path.join(output_dir, "xk_plots.png")

# Sauvegarde
plt.savefig(output_path)

# Affiche
plt.show()

print(f"✅ Dossier vidé et nouveau graphique sauvegardé dans : {output_path}")
