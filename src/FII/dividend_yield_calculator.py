import pandas as pd
import os

from src.FII.dividend_yield_base import DividendYieldBase

# @TODO: Melhorar as constants pra não deixar classe engessada
class DividendYieldCalculator(DividendYieldBase):
    COLUMNS_LABELS = ['Data', 'Descricao', 'Valor']
    MONTH_PT_BR = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 
                   'Outubro', 'Novembro', 'Dezembro']

    def __init__(self, data: list) -> None:
        self.df_property_funds = self.__prepare_dy_list(data)

    def calc_dy_by_month(self) -> float:
        df_fii_funds = self.df_property_funds
        df_fii_funds['Data'] = pd.to_datetime(df_fii_funds['Data'], format='%d/%m/%Y')

        # Criado uma nova coluna Ano_Mes para fazer o agrupamento e retornando a Data para fazer o sort correto.
        df_fii_funds['Ano_Mes'] = df_fii_funds['Data'].dt.strftime('%Y-%m')
        result = df_fii_funds.groupby('Ano_Mes').agg({
            'Valor': 'sum',
            'Data': 'first',
        }).reset_index()

        # Criando uma nova coluna com o nome do mês em português
        result['Mes'] = result['Data'].dt.month.apply(lambda x: self.MONTH_PT_BR[x - 1])

        return result[['Mes', 'Valor']]
    
    def calc_dy_from_pm_relative(self):
        base_dir = os.path.dirname(__file__) 
        file_path = os.path.join(base_dir, '..', '..', 'data', 'fundos_imobiliarios.csv')
        
        data = pd.read_csv(file_path)
        data['DY'] = ((data['DY'] / data['Quantidade']) / data['PM']) * 100
        data['DY'] = round(data['DY'], 2)

        return data[['Ativo', 'DY']]

    def __prepare_dy_list(self, data: list):
        df_data = pd.DataFrame(data, columns=self.COLUMNS_LABELS)

        return self.format_data_from_dataframe(df_data)
