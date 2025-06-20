from pathlib import Path
import streamlit as st 
import pandas as pd 

# CHAMANDO A FUNCAO PARA FZ OS LOADS DE PAGINAS 
from utilidades import leitura_de_dados

leitura_de_dados()

st.markdown('# Adicionando, Removendo e atualizando dados da tabela ')

df_vendas = st.session_state['dados']['df_vendas']

st.dataframe(df_vendas)