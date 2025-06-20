from PIL import Image
import pandas as pd 
import streamlit as st
import plotly.express as px

from utilidades import leitura_de_dados

leitura_de_dados()

st.markdown('## RESULTADO DIÁRIO' )

st.divider()

df_vendas = st.session_state['dados']['df_vendas']

def escolher_opcao():
    st.sidebar.divider()
    st.sidebar.markdown('Filtrando Opções')
    # BOX PARA PEGAR TODOS OS CAMPOS DO DATAFRAME 
    pegando_colunas = st.sidebar.multiselect('Selecione a colunar desejada', 
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
         st.dataframe(df_vendas.loc[df_vendas[filtro_selecao] == valor_filtro , pegando_colunas])
    elif limpar:
         st.dataframe(df_vendas[pegando_colunas])
    else:
         st.dataframe(df_vendas[pegando_colunas]) 
    

st.sidebar.markdown('### Escolhendo opções')
campo_selecionado = st.sidebar.selectbox('Escolha uma opção:', ['A', 'B', 'C'])

if campo_selecionado == 'B':
    escolher_opcao()



#imagem = Image.open("C:\\Users\\Leonardo\\Desktop\\Gestor-Apostas\\img\\pie2.png")
#st.image(imagem, caption="Gráfico")
