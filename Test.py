import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# Liste des dossiers où sauvegarder les figures
output_dirs = [
    "/Users/robinguichon/Desktop/MattApp/Git/Test",
    "/Users/robinguichon/Desktop/MattApp/Git/Test1",
    "/Users/robinguichon/Desktop/MattApp/Git/Test2",
    "/Users/robinguichon/Desktop/MattApp/Git/Test3"
]

# ⚠️ Vide chaque dossier avant de recréer
for d in output_dirs:
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d, exist_ok=True)

# Domaine de x
x = np.linspace(-10, 10, 400)

# Trace et enregistre une figure par k, dans chaque dossier
for k in range(1, 6):
    y = x**k

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = x^{k}")
    plt.title(f"Courbe de y = x^{k}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Sauvegarde dans chaque dossier
    for d in output_dirs:
        out_path = os.path.join(d, f"x_pow_{k}.png")
        plt.savefig(out_path)

    plt.close()

print("✅ Graphiques enregistrés dans Test, Test1, Test2 et Test3")
