import pandas as pd
import pdfplumber
import re

class Calculate_dy:
    ACTIVE_FIIS = ['RZTR11', 'PORD11','MXRF11','NCHB11','CPTI11','RECR11','HGLG11','BTCI11','CPTS11','BTLG11']
    COLUMNS_LABELS = ['Data', 'Descricao', 'Valor']

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def calc_dy(self) -> float:
        pdf_data = self._extract_data_from_pdf()
    
        # Transforma dados do PDF em DataFrame pandas
        data = pd.DataFrame(pdf_data, columns=self.COLUMNS_LABELS)
        fiis_list = self.get_fii_from_dataframe(data)

        return fiis_list['Valor'].sum()
    
    def _extract_data_from_pdf(self) -> list:
        with pdfplumber.open(self.file_path) as pdf:
            transactions = []
            for page in pdf.pages:
                text = page.extract_text()
                # regex para pegar data, descrição e valor
                transaction_pattern = r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(-?\d+,\d{2})"
                transactions += re.findall(transaction_pattern, text)

        return transactions
    
    def get_fii_from_dataframe(self, data: pd.DataFrame):

        #Filtra o dataframe para retornar somente os registros com FIIs
        filter = data['Descricao'].str.contains('|'.join(self.ACTIVE_FIIS), case=False)
        filtered = data[filter]

        #Converte a coluna Valor que é um objeto para float64
        filtered.loc[:, 'Valor'] = filtered['Valor'].str.replace(',', '.')
        filtered.loc[:, 'Valor'] = pd.to_numeric(filtered['Valor'], errors='coerce')

        return filtered