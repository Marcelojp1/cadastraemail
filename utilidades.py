from pathlib import Path
import streamlit as st 
import pandas as pd 

# ESTA FUNCAO VAI PERMITIR LOAD EM TODAS AS PAGINAS SEM AO ATUALIZAR CAIR OS DATAFRAMES 

def leitura_de_dados():
    if not 'dados' in st.session_state:
        pasta_datasets = Path(__file__).parent / 'C:\\Users\\Leonardo\\Desktop\\Gestor-Apostas\\datasets'

        df_vendas = pd.read_excel(pasta_datasets / 'Rel-may-2025-tratado.xlsx')
        #tabela_vendas = pd.read_excel('datasets/Rel-may-2025-tratado.xlsx', decimal=',')

        dados = {'df_vendas': df_vendas}

        st.session_state['dados'] = dados