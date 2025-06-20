from pathlib import Path
import streamlit as st 
import pandas as pd 

from utilidades import leitura_de_dados

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']

# FUNCTIONS 
def mostrar_tabela_venda():
    st.sidebar.divider()
    st.sidebar.markdown('### Filtrar Tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas da tabela:', 
                                                  list(df_vendas.columns),
                                                  list(df_vendas.columns))

    col1, col2 = st.sidebar.columns(2)
    filtro_selecao = col1.selectbox('Filtrar coluna',
                                list(df_vendas.columns))

    valor_unico_coluna = list(df_vendas[filtro_selecao].unique())
    valor_filtro = col2.selectbox('Valor filtro',
                              valor_unico_coluna)
    
    filtrar = col1.button('Filtrar')
    limpar  = col2.button('Limpar')

    if filtrar:
         st.dataframe(df_vendas.loc[df_vendas[filtro_selecao] == valor_filtro , colunas_selecionadas])
    elif limpar:
         st.dataframe(df_vendas[colunas_selecionadas])
    else:
         st.dataframe(df_vendas[colunas_selecionadas]) 
         

# BOX PARA SELECAO DA TABELA
st.sidebar.markdown('### Seleção de tabelas')
tab_selecionadas = st.sidebar.selectbox('Selecione a tabela desejada:',['Perfumaria', 'Vendas', 'Genéricos'])

if tab_selecionadas == 'Vendas':
    mostrar_tabela_venda()