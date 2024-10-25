import pandas as pd

class DividendYieldBase:
    ACTIVE_FIIS = ['RZTR11', 'PORD11','MXRF11','NCHB11','CPTI11','RECR11','HGLG11','BTCI11','CPTS11','BTLG11']

    # @TODO: MELHORAR O NOME DESSE METODO
    def format_data_from_dataframe(self, data: list) -> list:
        #Filtra o dataframe para retornar somente os registros com FIIs
        filter = data['Descricao'].str.contains('|'.join(self.ACTIVE_FIIS), case=False)
        filtered = data[filter]

        # Remove o texto que vem na descrição deixando somente o nome dos papeis
        filtered['Descricao'] = filtered['Descricao'].str.split('-').str[1]

        #Converte a coluna Valor que é um objeto para float64
        filtered['Valor'] = filtered['Valor'].str.replace(',', '.')
        filtered['Valor'] = pd.to_numeric(filtered['Valor'], errors='coerce')

        return filtered