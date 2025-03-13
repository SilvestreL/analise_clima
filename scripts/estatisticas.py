import pandas as pd
import numpy as np

def calcular_estatisticas(df):
    """
    Calcula estatísticas descritivas para colunas numéricas de um DataFrame.
    Retorna um dicionário contendo os valores.
    """
    estatisticas = {}

    colunas_numericas = df.select_dtypes(include=[np.number]).columns

    for coluna in colunas_numericas:
        estatisticas[coluna] = {
            "Média": round(df[coluna].mean(), 2),
            "Mediana": round(df[coluna].median(), 2),
            "Moda": df[coluna].mode().values.tolist(),
            "Quartil 25%": round(df[coluna].quantile(0.25), 2),
            "Quartil 75%": round(df[coluna].quantile(0.75), 2),
            "Amplitude": round(df[coluna].max() - df[coluna].min(), 2)
        }

    return estatisticas