from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import pandas as pd

def gerar_relatorio(df, estatisticas, caminho_pdf="relatorios/relatorio_clima.pdf"):
    """
    Gera um relatório em PDF contendo as estatísticas e gráficos.
    """
    # Criar diretório para armazenar os relatórios
    os.makedirs("relatorios", exist_ok=True)

    # Criar o canvas do PDF
    c = canvas.Canvas(caminho_pdf, pagesize=letter)
    largura, altura = letter

    # Título do relatório
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, altura - 50, "Relatório de Análise Climática")

    # Estatísticas
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, altura - 80, "📊 Estatísticas Climáticas:")

    altura_atual = altura - 100  # Ajuste para a posição inicial

    for coluna, valores in estatisticas.items():
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, altura_atual, f"📌 {coluna}")
        altura_atual -= 15

        c.setFont("Helvetica", 10)
        for chave, valor in valores.items():
            c.drawString(70, altura_atual, f"- {chave}: {valor}")
            altura_atual -= 12

        altura_atual -= 10  # Espaço entre colunas

    # Adicionar imagens dos gráficos
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, altura_atual, "📈 Gráficos Gerados:")
    altura_atual -= 20

    caminho_graficos = "graficos/"
    arquivos_graficos = sorted(os.listdir(caminho_graficos))

    for i, imagem in enumerate(arquivos_graficos):
        if imagem.endswith(".png"):
            caminho_imagem = os.path.join(caminho_graficos, imagem)
            if altura_atual < 150:  # Nova página se não houver espaço suficiente
                c.showPage()
                altura_atual = altura - 50

            c.drawImage(caminho_imagem, 50, altura_atual - 150, width=500, height=150)
            altura_atual -= 180  # Ajuste de espaço

    # Salvar o PDF
    c.save()
    print(f"📄 Relatório salvo em: {caminho_pdf}")