import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

# Dossier de sortie
output_dir = "/Users/robinguichon/Desktop/MattApp/Git/Test"

# ⚠️ Vide entièrement le dossier Test/ puis le recrée (comme demandé précédemment)
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

# Domaine de x
x = np.linspace(-10, 10, 400)

# Trace et enregistre une figure par k
saved = []
for k in range(1, 6):
    y = x**k

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = x^{k}")
    plt.title(f"Courbe de y = x^{k}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    out_path = os.path.join(output_dir, f"x_pow_{k}.png")
    plt.savefig(out_path)
    plt.close()
    saved.append(out_path)

print("✅ Graphiques enregistrés :")
for p in saved:
    print(" -", p)
