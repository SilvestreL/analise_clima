import matplotlib.pyplot as plt
import os

# Criar pasta para salvar os gráficos
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

def plot_histograma(df, coluna):
    plt.figure(figsize=(8, 5))
    plt.hist(df[coluna], bins=10, color="royalblue", alpha=0.75, edgecolor="black")
    plt.title(f"Histograma de {coluna}", fontsize=14)
    plt.xlabel(coluna, fontsize=12)
    plt.ylabel("Frequência", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(f"{output_dir}/histograma_{coluna}.png", dpi=300)
    plt.show()

def plot_boxplot(df, coluna):
    plt.figure(figsize=(5, 6))
    plt.boxplot(df[coluna], vert=True, patch_artist=True, boxprops=dict(facecolor="skyblue"))
    plt.title(f"Boxplot de {coluna}", fontsize=14)
    plt.ylabel(coluna, fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig(f"{output_dir}/boxplot_{coluna}.png", dpi=300)
    plt.show()

def plot_linhas(df, coluna, data_coluna):
    plt.figure(figsize=(10, 5))
    plt.plot(df[data_coluna], df[coluna], marker="o", linestyle="-", color="green", markersize=4)
    plt.title(f"Variação de {coluna} ao longo do tempo", fontsize=14)
    plt.xlabel("Data", fontsize=12)
    plt.ylabel(coluna, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig(f"{output_dir}/linha_{coluna}.png", dpi=300)
    plt.show()