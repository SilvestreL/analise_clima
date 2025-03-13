# 🌦️ Projeto: Análise Climática

Este projeto realiza a análise de dados climáticos, gerando estatísticas descritivas e gráficos de visualização dos dados. Além disso, permite gerar relatórios em PDF com as informações extraídas.

## 📁 Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

```
analise_clima/
│-- data/                 # Diretório contendo os arquivos CSV com dados climáticos
│-- graficos/             # Diretório onde os gráficos gerados são salvos
│-- relatorios/           # Diretório onde os relatórios PDF são gerados
│-- scripts/              # Diretório com os códigos Python
│   │-- __init__.py       # Torna o diretório um módulo Python
│   │-- main.py           # Arquivo principal que executa o fluxo completo da aplicação
│   │-- carregar_dados.py # Módulo responsável por carregar os dados
│   │-- estatisticas.py   # Módulo que calcula estatísticas descritivas
│   │-- visualizacoes.py  # Módulo para geração de gráficos
│   │-- gerar_relatorio.py # Módulo para gerar relatórios em PDF
│-- requirements.txt      # Lista de dependências do projeto
│-- venv/                 # Ambiente virtual Python (não é versionado no Git)
```

## 🚀 Como Executar o Projeto
### 1️⃣ Instalar Dependências
Antes de rodar o projeto, certifique-se de ter o Python instalado. Depois, siga os passos abaixo:

```sh
# Criar e ativar o ambiente virtual (Mac/Linux)
python -m venv venv
source venv/bin/activate

# Para Windows
venv\Scripts\activate
```

Instale as dependências:
```sh
pip install -r requirements.txt
```

### 2️⃣ Executar o Projeto
Para rodar o projeto e gerar os gráficos e relatórios:
```sh
python -m scripts.main
```

## 🔍 Descrição dos Módulos

### 📜 `main.py`
O arquivo principal que orquestra a execução do projeto:
1. Carrega os dados.
2. Exibe os primeiros registros.
3. Calcula estatísticas descritivas.
4. Gera gráficos de visualização.
5. Gera um relatório em PDF.

### 📂 `carregar_dados.py`
Responsável por:
- Ler os arquivos CSV localizados na pasta `data/`.
- Tratar os dados, convertendo colunas numéricas corretamente.
- Retornar o DataFrame pronto para análise.

### 📊 `estatisticas.py`
Este módulo realiza o cálculo de estatísticas descritivas:
- Média, Mediana, Moda.
- Quartis.
- Amplitude dos dados.

### 📈 `visualizacoes.py`
Gera gráficos para melhor compreensão dos dados:
- **Histogramas** das variáveis numéricas.
- **Boxplots** para visualizar outliers.
- **Linhas do tempo** para análise temporal.

Os gráficos são salvos na pasta `graficos/`.

### 📄 `gerar_relatorio.py`
Cria um relatório em PDF contendo:
- As estatísticas calculadas.
- Os gráficos gerados.
- O número de dias sem chuva.

Os PDFs são salvos na pasta `relatorios/`.


