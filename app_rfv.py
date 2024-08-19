import pandas as pd
import streamlit as st
from io import BytesIO

# Função para calcular as métricas de RFV
def calcular_rfv(df):
    # Recência (R): Número de dias desde a última compra
    df['Recency'] = (df['DiaCompra'].max() - df['DiaCompra']).dt.days
    
    # Frequência (F): Número de compras
    df['Frequency'] = df.groupby('ID_cliente')['CodigoCompra'].transform('count')
    
    # Valor Monetário (V): Valor total gasto
    df['Monetary'] = df.groupby('ID_cliente')['ValorTotal'].transform('sum')
    
    # Categorizar RFV em 4 categorias (A, B, C, D)
    r_labels = f_labels = m_labels = ['A', 'B', 'C', 'D']
    
    df['R_Score'] = pd.qcut(df['Recency'], q=4, labels=r_labels, duplicates='drop')
    df['F_Score'] = pd.qcut(df['Frequency'], q=4, labels=f_labels, duplicates='drop')
    df['M_Score'] = pd.qcut(df['Monetary'], q=4, labels=m_labels, duplicates='drop')
    
    df['RFV'] = df['R_Score'].astype(str) + df['F_Score'].astype(str) + df['M_Score'].astype(str)
    
    # Estratégia de marketing
    df['Marketing_Strategy'] = df['RFV'].apply(estrategia_marketing)
    
    return df

# Função para definir a estratégia de marketing
def estrategia_marketing(rfv):
    if rfv == 'AAA':
        return 'Manter cliente fiel'
    elif rfv == 'AAD':
        return 'Incentivar mais compras'
    elif rfv == 'DDD':
        return 'Reativar clientes perdidos'
    elif rfv == 'DDA':
        return 'Oferecer promoções para reengajar'
    else:
        return 'Desenvolver estratégia personalizada'

# Função para converter DataFrame em um arquivo Excel na memória
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='RFV Analysis')
    processed_data = output.getvalue()
    return processed_data

# Função para contar os clientes por grupo RFV e incluir a estratégia de marketing
def contar_clientes_por_grupo(df):
    contagem_df = df['RFV'].value_counts().reset_index()
    contagem_df.columns = ['RFV', 'Contagem']  # Renomear as colunas corretamente
    contagem_df['Marketing_Strategy'] = contagem_df['RFV'].apply(estrategia_marketing)
    return contagem_df

# Configuração da aplicação Streamlit
st.title('Análise RFV de Clientes')

# URL do arquivo CSV hospedado no GitHub
csv_url = "https://raw.githubusercontent.com/GiovanoMP/app_rfv/main/dados_input%201.csv"

# Botão para carregar o arquivo CSV
if st.button("Carregar dados do GitHub"):
    df = pd.read_csv(csv_url)
    df['DiaCompra'] = pd.to_datetime(df['DiaCompra'])  # Convertendo a coluna de data
    rfv_df = calcular_rfv(df)
    
    st.dataframe(rfv_df.head())  # Mostra as primeiras linhas do dataframe resultante
    
    # Contagem de clientes por grupo RFV
    contagem_df = contar_clientes_por_grupo(rfv_df)
    st.dataframe(contagem_df)
    
    # Botão para download do arquivo Excel com RFV
    st.download_button(
        label="Download do arquivo Excel com RFV",
        data=convert_df_to_excel(rfv_df),
        file_name='rfv_analysis.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Botão para download do arquivo Excel com contagem de grupos e estratégias
    st.download_button(
        label="Download do arquivo Excel com contagem de grupos",
        data=convert_df_to_excel(contagem_df),
        file_name='rfv_group_counts.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

# Explicação do que foi feito
"""
### Explicação do Código

Este código foi desenvolvido para criar uma aplicação em Streamlit que realiza a análise RFV (Recência, Frequência, Valor) dos clientes com base em um arquivo CSV.

**Objetivo:**
O principal objetivo da análise RFV é segmentar os clientes em grupos, com base em seu comportamento de compra, para que estratégias de marketing específicas possam ser aplicadas a cada segmento.

**O que foi feito:**

1. **Carregamento de Arquivo CSV do GitHub:** O usuário pode carregar o arquivo CSV diretamente do GitHub ao clicar em um botão.

2. **Cálculo das Métricas RFV:**
   - **Recência (R):** Calcula o número de dias desde a última compra de cada cliente.
   - **Frequência (F):** Conta o número de compras feitas por cada cliente.
   - **Valor Monetário (V):** Soma o valor total gasto por cada cliente.

3. **Classificação dos Clientes:** 
   - Utilizamos `pd.qcut` para dividir as métricas RFV em 4 categorias (`A`, `B`, `C`, `D`), onde `A` representa o melhor desempenho em cada métrica e `D` o pior.
   - A combinação dessas categorias é usada para formar um código RFV como `AAA`, `AAB`, etc.

4. **Estratégias de Marketing:** 
   - Aplicamos estratégias de marketing específicas para cada combinação de RFV, como "Manter cliente fiel" para `AAA` ou "Reativar clientes perdidos" para `DDD`.

5. **Download dos Resultados:**
   - Os usuários podem baixar dois arquivos Excel:
     - Um com a análise completa RFV de cada cliente.
     - Outro com a contagem de clientes por grupo RFV e as estratégias de marketing recomendadas para cada grupo.

**Utilização:**
Este código pode ser utilizado para carregar um arquivo CSV específico diretamente do GitHub, realizar a análise RFV e permitir o download dos resultados.
"""
