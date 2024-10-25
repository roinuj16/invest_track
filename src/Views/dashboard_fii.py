import streamlit as st
import plotly.express as px
import pandas as pd

from src.FII.pdf_extract_processor import PdfExtractProcessor
from src.FII.dividend_yield_calculator import DividendYieldCalculator

def display():
    # Carrega os dados
    dy_month, dy_pm = load_data()

    st.title("Dashboard FII")
    left, middle, right = st.columns([0.3, 0.4, 0.4], vertical_alignment="center")

    with left:
        dy_month['Valor'] = dy_month['Valor'].map(lambda x: f"R$ {x:.2f}")
        st.table(dy_month)

    with middle:
        fig_date = px.bar(dy_month, x='Mes', y='Valor')
        middle.plotly_chart(fig_date)

    with right:
        fig = px.pie(dy_pm, values='DY', names='Ativo', title='DY% por Ativo', hole=0.4) 
        st.plotly_chart(fig)


def load_data() -> pd.DataFrame:
    pdf_processor = PdfExtractProcessor()
    pdf_records = pdf_processor.read_pdf_file()

    dy_calculator = DividendYieldCalculator(pdf_records)
    dy_month = dy_calculator.calc_dy_by_month()
    dy_from_pm = dy_calculator.calc_dy_from_pm_relative()

    return dy_month, dy_from_pm