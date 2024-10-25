import streamlit as st
import warnings
warnings.filterwarnings('ignore') #Ignorar alertas
from PIL import Image

from src.Views import dashboard_fii

def main() -> None:
    st.set_page_config(layout='wide')
    logo = Image.open('assets/logo.jpg')
    st.sidebar.image(logo, use_column_width=True)
    st.sidebar.title("Invest Track")

    
    # @TODO: Criar a lógica para trocar de dashboard. Ideia para lógica abaixo.
    # Criar no sidebar um componente para poder selecionar o Dashboard.
    # option = st.sidebar.selectbox("Selecione a página", ["Dashboard FII", "Dashboard Ações"])

    # if option == "Dashboard FII":
    #     dashboard_fii.display()
    # elif option == "Dashboard Ações":
    #     dashboard_stock.display()

    dashboard_fii.display()

if __name__ == "__main__":
    main()



