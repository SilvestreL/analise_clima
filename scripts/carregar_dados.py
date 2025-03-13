import pandas as pd

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de um arquivo CSV ignorando metadados iniciais.
    Retorna um DataFrame do Pandas formatado.
    """
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    # Encontrar a primeira linha vazia para identificar onde começam os dados reais
    indice_inicio = next((i + 1 for i, linha in enumerate(linhas) if linha.strip() == ""), 10)

    # Carregar o CSV ignorando as linhas de metadados e ajustando o separador
    df = pd.read_csv(caminho_arquivo, skiprows=indice_inicio, sep=";", encoding="utf-8")

    # Convertendo valores numéricos corretamente
    df.columns = df.columns.str.strip()
    colunas_numericas = df.columns[1:]  # Ignorar a coluna de Data
    for coluna in colunas_numericas:
        df[coluna] = df[coluna].astype(str).str.replace(",", ".").astype(float)

    return df