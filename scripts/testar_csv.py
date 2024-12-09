import pandas as pd

# Tente carregar o arquivo CSV
try:
    df = pd.read_csv("dados_irrigacao.csv", sep="\t")
    print("Colunas encontradas:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")
