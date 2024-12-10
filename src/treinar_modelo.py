import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Tente carregar o arquivo CSV
try:
    # Ler o arquivo com diferentes opções de separador
    df = pd.read_csv("dados_irrigacao.csv", sep=";")  # Substitua por "," se necessário
    
    # Limpar espaços em branco nos nomes das colunas
    df.columns = df.columns.str.strip()
    
    # Exibir as colunas encontradas no arquivo
    print("Colunas encontradas no arquivo:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")
    exit()

# Verificar se todas as colunas necessárias estão presentes
colunas_necessarias = ["Umidade (%)", "Nutrientes_P", "Nutrientes_K", "pH", "Requer_Irrigação"]
for coluna in colunas_necessarias:
    if coluna not in df.columns:
        raise ValueError(f"O arquivo 'dados_irrigacao.csv' deve conter a coluna '{coluna}'.")

# Preprocessamento dos dados
df["Requer_Irrigação"] = df["Requer_Irrigação"].map({"Sim": 1, "Não": 0})
df["Nutrientes_P"] = df["Nutrientes_P"].map({"Baixo": 0, "Médio": 1, "Alto": 2})
df["Nutrientes_K"] = df["Nutrientes_K"].map({"Baixo": 0, "Médio": 1, "Alto": 2})

# Separar features e rótulo
X = df[["Umidade (%)", "Nutrientes_P", "Nutrientes_K", "pH"]]
y = df["Requer_Irrigação"]

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliar o modelo
y_pred = modelo.predict(X_test)
print(f"Acurácia do modelo: {accuracy_score(y_test, y_pred):.2f}")

# Salvar o modelo treinado
with open("modelo_irrigacao.pkl", "wb") as arquivo:
    pickle.dump(modelo, arquivo)

print("Modelo treinado e salvo como 'modelo_irrigacao.pkl'.")
