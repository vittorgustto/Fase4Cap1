import serial
import time
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Configuração da porta serial
ser = serial.Serial('COM3', 115200)  # Substitua 'COM3' pela sua porta serial
time.sleep(2)  # Atraso para garantir que a conexão seja estabelecida

# Função para ler os dados do ESP32 via Serial
def ler_dados_esp32():
    try:
        if ser.in_waiting > 0:
            linha = ser.readline().decode('utf-8').strip()
            if linha:
                try:
                    # Tenta carregar a linha como JSON
                    dados = json.loads(linha)
                    return dados
                except json.JSONDecodeError:
                    return None
    except Exception as e:
        st.error(f"Erro ao ler os dados do ESP32: {e}")
        return None

# Função para mostrar gráficos
def mostrar_grafico(umidades, temperaturas):
    fig, ax = plt.subplots()
    ax.plot(umidades, label='Umidade (%)', color='blue')
    ax.plot(temperaturas, label='Temperatura (°C)', color='red')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Valores')
    ax.set_title('Monitoramento de Umidade e Temperatura')
    ax.legend()
    st.pyplot(fig)

# Função Streamlit para o painel
def painel_monitoramento():
    st.title("Sistema de Monitoramento de Umidade e Temperatura")

    # Variáveis para armazenar os dados coletados
    umidades = []
    temperaturas = []

    st.write("Monitoramento de dados do sensor em tempo real")

    # Leitura contínua de dados do ESP32
    while True:
        dados = ler_dados_esp32()
        if dados:
            umidade = dados.get("umidade")
            temperatura = dados.get("temperatura")

            # Adiciona os dados à lista
            umidades.append(umidade)
            temperaturas.append(temperatura)

            # Exibe os dados na interface Streamlit
            st.write(f"Umidade: {umidade}% | Temperatura: {temperatura}°C")

            # Exibe o gráfico com os dados coletados
            mostrar_grafico(umidades, temperaturas)

        time.sleep(2)  # Atraso entre as leituras

if __name__ == "__main__":
    painel_monitoramento()
