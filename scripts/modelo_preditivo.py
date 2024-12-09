import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Carregar os dados
dados = pd.read_csv("dados_sensores.csv")

# Separar as variáveis de entrada e saída
X = dados[['Umidade', 'Temperatura', 'Nutrientes']]
y = dados['Irrigacao_Necessaria']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de classificação
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliar o modelo
y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)

print(f"Acurácia do modelo: {acuracia:.2f}")

# Testar com novos dados
novos_dados = pd.DataFrame({
    "Umidade": [50, 85],
    "Temperatura": [27, 33],
    "Nutrientes": [4, 6]
})
predicoes = modelo.predict(novos_dados)
print("Previsões para novos dados:")
print(predicoes)
