import pandas as pd 
import streamlit as st
import plotly.express as px


# CONFIGURACAO DE TELA DO STREAMLIT 
st.set_page_config(page_title="GESTOR DE APOSTAS", layout='wide', page_icon=":rocket:")

st.sidebar.markdown('Desenvolvido por [Olecram-Data](https://google.com/)')

# HEADER 
st.markdown('# Bem-vindo ao Gestor de Vendas e Resultados de sua Farmácia')

st.divider()


# READ DATA
#tabela_vendas = pd.read_excel('datasets/Rel-may-2025-tratado.xlsx', decimal=',')

# WORFLOW 
#st.dataframe(tabela_vendas)

# BOX MULTISELECT 
#columns = list(tabela_vendas.columns)
#select_columns = st.sidebar.multiselect('Escolha abaixo', columns, columns)

# TABELA DE LUCRO 
#tabela_vendas['Lucro'] = tabela_vendas['Venda'] - tabela_vendas['Custo'] * tabela_vendas['Unids']

#st.markdown("# Lista dos Itens Mais Vendidos do mês de maio")
#unid_vendidas = tabela_vendas.nlargest(10, 'Unids')
#rec_unid = px.pie(unid_vendidas, names="Codigo", color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'], values='Lucro')
#st.write(unid_vendidas)
#st.write(rec_unid)







