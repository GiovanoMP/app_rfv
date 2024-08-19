# Análise RFV de Clientes

Este repositório contém uma aplicação desenvolvida em Streamlit para realizar a análise RFV (Recência, Frequência, Valor) dos clientes com base em um arquivo CSV. A análise RFV é uma técnica utilizada para segmentar os clientes em diferentes grupos, de acordo com seu comportamento de compra, permitindo a aplicação de estratégias de marketing personalizadas para cada segmento.

## Funcionalidades

- **Carregamento de Arquivo CSV**: A aplicação carrega automaticamente um arquivo CSV específico hospedado no GitHub para realizar a análise RFV.
- **Cálculo de Métricas RFV**: O código calcula as métricas de Recência, Frequência e Valor, e classifica os clientes em quatro categorias (A, B, C, D) para cada métrica.
- **Classificação de Clientes**: Os clientes são classificados em grupos como `AAA`, `AAB`, etc., com base na combinação das categorias RFV.
- **Estratégias de Marketing**: São sugeridas estratégias de marketing específicas para cada grupo RFV.
- **Download dos Resultados**: Os resultados da análise podem ser baixados em dois arquivos Excel: um com a análise completa RFV e outro com a contagem de clientes por grupo RFV e as estratégias de marketing recomendadas.

## Como Utilizar

Você pode acessar a aplicação diretamente na web através do link:

[https://app-rfv-rdft.onrender.com/](https://app-rfv-rdft.onrender.com/)

Ao acessar a aplicação, basta clicar no botão "Carregar dados do GitHub" para carregar o arquivo CSV hospedado e visualizar os resultados da análise RFV.

## Estrutura do Repositório

- `app_rfv.py`: Código principal da aplicação Streamlit.
- `requirements.txt`: Lista de dependências necessárias para rodar a aplicação.
- `README.md`: Este arquivo, contendo informações sobre o projeto.

## Executando Localmente

Se você deseja rodar a aplicação localmente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/GiovanoMP/app_rfv.git
   cd app_rfv
