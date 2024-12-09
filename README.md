# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Chatbot Solubio

## Grupo 67

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/company/inova-fusca">João Vitor Lopes Beiro</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Thyego Brandão</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gabriel Alves Costa</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Vinícius Zeller Matias</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

### Projeto Fase 4 - Sistema de Irrigação Inteligente ###
Este repositório contém a implementação da **Fase 4** do projeto **FarmTech Solutions**, que visa aprimorar um sistema de irrigação automatizado, incorporando a inteligência preditiva utilizando **Scikit-learn**, uma interface interativa com **Streamlit**, otimização de código no **ESP32** e integração com um sistema de monitoramento visual em tempo real.

### Descrição do Projeto ###
O objetivo desta fase é aprimorar a aplicação desenvolvida na **Fase 3**, trazendo novas funcionalidades e melhorias na utilização de recursos já apresentados nas fases anteriores.

### Funcionalidades Implementadas: ###
- **Modelo Preditivo com Scikit-learn**: Um modelo preditivo foi desenvolvido para prever a necessidade de irrigação, baseado em dados históricos de umidade e nutrientes do solo.
- **Interface de Visualização com Streamlit**: Um dashboard interativo foi criado com Streamlit, permitindo a visualização em tempo real dos dados do sistema de irrigação, incluindo gráficos da variação da umidade, níveis de nutrientes e previsões de irrigação.
- **Otimização no ESP32**: O código C/C++ do ESP32 foi otimizado para melhor uso de memória e desempenho, com ajustes em tipos de dados e variáveis.
- **Exibição de Dados no Display LCD**: Um display LCD conectado ao ESP32 exibe em tempo real as métricas de umidade, temperatura e status da irrigação.
- **Monitoramento com Serial Plotter**: Utilização do Serial Plotter para monitorar a variação de umidade do solo em tempo real durante a simulação.

### Estrutura do Repositório ###
- **ESP32**: Código C/C++ que gerencia os sensores, controla a irrigação, e exibe informações no display LCD.
- **Python**: Código Python que utiliza **Scikit-learn** para criar um modelo preditivo e **Streamlit** para criar uma interface interativa de monitoramento.
- **Banco de Dados**: Melhorias na estrutura do banco de dados para registrar e consultar dados históricos de umidade, temperatura, e previsão de irrigação.

### Requisitos ###

- **Arduino IDE** para o código do ESP32.
- **Python 3.x** com as bibliotecas:
  - `scikit-learn`
  - `streamlit`
  - `pyserial`
- **Wokwi** para simulação do ESP32 (opcional).


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


