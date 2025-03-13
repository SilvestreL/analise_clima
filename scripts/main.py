import sys
import os
import pandas as pd
from scripts.carregar_dados import carregar_dados
from scripts.estatisticas import calcular_estatisticas
from scripts.visualizacoes import plot_histograma, plot_boxplot, plot_linhas
from scripts.gerar_relatorio import gerar_relatorio 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def main():
    print("🚀 Ambiente configurado corretamente!")
    print("🔍 Preparando para carregar os dados...\n")

    caminho_arquivo = "data/dados_A303_D_2025-01-01_2025-02-24.csv"

    try:
        df = carregar_dados(caminho_arquivo)
        print(df.head())

        print("\n🔍 Contagem de dias sem chuva:")
        dias_sem_chuva = (df["PRECIPITACAO TOTAL, DIARIO (AUT)(mm)"] == 0).sum()
        print(f"🌦️ {dias_sem_chuva} dias sem chuva registrados")

        print("\n📊 Calculando estatísticas...\n")
        estatisticas = calcular_estatisticas(df)

        for coluna, valores in estatisticas.items():
            print(f"📌 Estatísticas para {coluna}:")
            for chave, valor in valores.items():
                print(f"   {chave}: {valor}")
            print("-" * 40)

        print("\n📈 Gerando e salvando gráficos...\n")
        df["Data Medicao"] = pd.to_datetime(df["Data Medicao"], format="%d/%m/%Y")

        colunas_numericas = df.select_dtypes(include=["float64"]).columns
        for coluna in colunas_numericas:
            plot_histograma(df, coluna)
            plot_boxplot(df, coluna)
            plot_linhas(df, coluna, "Data Medicao")

        # ✅ Adicionando geração do relatório em PDF
        print("\n📄 Gerando relatório em PDF...\n")
        gerar_relatorio(df, estatisticas)

    except Exception as e:
        print(f"⚠️ Erro: {e}")

if __name__ == "__main__":
    main()