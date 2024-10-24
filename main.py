import os
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings('ignore') #Ignorar alertas
import plotly.express as px

from src.FII.pdf_extract_processor import PdfExtractProcessor
from src.FII.dividend_yield_calculator import DividendYieldCalculator

def main() -> None:
    pdf_processor = PdfExtractProcessor()
    list_pdf_data = pdf_processor.read_pdf_file()

    dy_calculator = DividendYieldCalculator(list_pdf_data)
    dy_month = dy_calculator.calc_dy_by_month()

    
    __create_view(dy_month)

def __create_view(data: pd.DataFrame) -> None:
    st.set_page_config(layout='wide')
    
    month = st.sidebar.selectbox('Selecione o mês', ['All'] + list(data['Mes'].unique()))

    if month != 'All':
        data_filtered = data[data['Mes'] == month]
    else:
        data_filtered = data

    col1, col2,  = st.columns([1, 2])

    with col1:
        st.write("**Tabela de Valores por Mês**") 
        st.dataframe(data_filtered)

    fig_date = px.bar(data_filtered, x='Mes', y='Valor', title='DY recebido por mês')
    col2.plotly_chart(fig_date)

if __name__ == "__main__":
    main()



