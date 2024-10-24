import pdfplumber
import re
import os

class PdfExtractProcessor:
    ACTIVE_FIIS = ['RZTR11', 'PORD11','MXRF11','NCHB11','CPTI11','RECR11','HGLG11','BTCI11','CPTS11','BTLG11']
    COLUMNS_LABELS = ['Data', 'Descricao', 'Valor']
    FILE_PATH = 'statements/btg'

    def read_pdf_file(self) -> list:
        result_list = []
        for filename in os.listdir(self.FILE_PATH):
            pdf_path = os.path.join(self.FILE_PATH, filename)
            result_list += self._extract_data_from_pdf(pdf_path)
        
        return result_list  

    def _extract_data_from_pdf(self, file_path: str) -> list:
        with pdfplumber.open(file_path) as pdf:
            transactions = []
            for page in pdf.pages:
                text = page.extract_text()
                # regex para pegar data, descrição e valor
                transaction_pattern = r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+(-?\d+,\d{2})"
                transactions += re.findall(transaction_pattern, text)

        return transactions
    
