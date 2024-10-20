import os
from src.calc_dy import Calculate_dy

if __name__ == "__main__":

    files_dir = 'statements/btg'

    for filename in os.listdir(files_dir):
        file_name, _ = os.path.splitext(filename)
        pdf_path = os.path.join(files_dir, filename)

        calculate_dy = Calculate_dy(pdf_path)
        result = round(calculate_dy.calc_dy(), 2)

        print(f'O DY recebido em {file_name} foi: R$ {result}')



