
# Invest Track
> Projeto em desenvolvimento

Invest Track é um projeto desenvolvido em Python, projetado para ajudar na organização e gerenciamento da minha carteira de investimentos pessoal. Este projeto serve como uma aplicação prática dos conhecimentos adquiridos durante meus estudos de programação e análise de dados, com foco em finanças pessoais.

## Objetivo
O principal objetivo do Invest Track é fornecer uma maneira simples e eficaz de rastrear e gerenciar meus investimentos em renda variável(FIIs e AÇÕES), me permitindo visualizar o desempenho de minha carteira, calcular rendimentos e tomar decisões informadas sobre meus investimentos.

## Funcionalidades
- **Cálculo de Dividendos(DY) mensal para fundos imobiliários(FIIs)**:


## Tecnologias Utilizadas
- Python
- Pandas
- Pdfplumber


## Instalação e uso

1. Clone este repositório:
```bash
git clone https://github.com/roinuj16/invest_track.git
```
2. Navege até o diretório do projeto:
```bash
cd invest_track
```
3. Instale as dependências necessárias:
```bash
pip install pandas pdfplumber
```
4. Crie um diretório na raíz do projeto onde será adicionado os extratos:
```bash
mkdir nome_do_seu_diretorio
```
  - **Observações:** 
    - O código espera que os arquivos dos extratos tenham o nome do mês com a extensão `.pdf`. Por exemplo `Janeiro.pdf`.
    - O arquivo PDF precisa ter informações de Data, Descrição e valor
5. Acesse o arquivo `main.py` e na variável `files_dir` adicione o caminho onde foi adicionado os extratos
```bash
files_dir = 'seu_diretorio'
```
6. Execute o projeto:
```bash
python main.py
```