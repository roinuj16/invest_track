import pandas as pd

class DividendYieldBase:

    # @TODO: MELHORAR O NOME DESSE METODO
    def format_data_from_dataframe(self, data: list) -> list:
        #Filtra o dataframe para retornar somente os registros com FIIs
        filter = data['Descricao'].str.contains('|'.join(self.ACTIVE_FIIS), case=False)
        filtered = data[filter]

        # Remove o texto que vem na descrição deixando somente o nome do FII
        filtered['Descricao'] = filtered['Descricao'].str.split('-').str[1]

        #Converte a coluna Valor que é um objeto para float64
        filtered['Valor'] = filtered['Valor'].str.replace(',', '.')
        filtered['Valor'] = pd.to_numeric(filtered['Valor'], errors='coerce')

        return filtered