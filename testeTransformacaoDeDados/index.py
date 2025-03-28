import pdfplumber
import pandas as pd
import zipfile
import os
import requests
import re


def download_pdf(url, save_path):  # Função para fazer download do pdf
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF baixado com sucesso: {save_path}")
    else:
        print("Erro ao baixar o PDF")
        exit()


def extract_table_from_pdf(pdf_path):  # Função para extrair os dados da tabela

    data = []  # Armazena os dados das tabelas nessa lista
    header = None  # Armazena o cabeçalho da tabela

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()  # Extrai as tabelas do arquivo pdf
            for table in tables:
                for row in table:
                    cleaned_row = [
                        # Corrige quebras de linhas da tabela
                        " ".join(str(cell).splitlines()) if cell else "" for cell in row]
                    if header is None:
                        header = cleaned_row
                        data.append(header)
                    elif cleaned_row != header:  # Garante que o cabeçalho não fique duplicado
                        data.append(cleaned_row)
    return data


def extract_legends(pdf_path):  # Função para extrair as legendas do pdf
    legends = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    # Verifica se a linha contém as legendas "OD" ou "AMB" e captura o texto associado a elas
                    match_od = re.search(
                        r"^\b(OD)\b:\s*([A-Za-zÀ-ú\s.]+)(?=\s*[A-Z]{3,}|\s*$)", line, re.IGNORECASE)
                    match_amb = re.search(
                        r"^\b(AMB)\b:\s*([A-Za-zÀ-ú\s.]+)(?=\s*[A-Z]{3,}|\s*$)", line, re.IGNORECASE)

                    if match_od:
                        legends["OD"] = match_od.group(2).strip()
                    if match_amb:
                        legends["AMB"] = match_amb.group(2).strip()

                    # Retorna as legendas assim que encontradas
                    if "OD" in legends and "AMB" in legends:
                        return legends


# Função para salvar os dados em csv
def clean_and_save_data(data, output_csv, legends):
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)  # Remove a linha duplicada do cabeçalho

    # Substitui as legendas "OD" e "AMB" pelos seus valores
    df.replace(legends, inplace=True)

    df.to_csv(output_csv, index=False, sep=";")


# Função para compactar o arquivo csv em zip
def compress_csv(csv_filename, zip_filename):
    # Caminho onde o arquivo compactado será salvo
    zip_path = os.path.join(os.path.dirname(__file__), zip_filename)

    # Cria o arquivo zip
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona o csv no arquivo zip
        zipf.write(csv_filename, os.path.basename(csv_filename))

    os.remove(csv_filename)  # Remove o arquivo csv que não esta compactado


def main():
    try:
        pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  # URL do pdf
        pdf_filename = "Anexo_I_Rol_2021.pdf"
        csv_filename = "Rol_de_Procedimentos.csv"
        zip_filename = "Teste_{vinicius_chavier}.zip"

        print("Baixando PDF...")
        download_pdf(pdf_url, pdf_filename)

        print("Extraindo dados do PDF...")
        legends = extract_legends(pdf_filename)
        data = extract_table_from_pdf(pdf_filename)

        print("Salvando dados em CSV...")
        clean_and_save_data(data, csv_filename, legends)

        print("Compactando CSV...")
        compress_csv(csv_filename, zip_filename)

        print(f"Processo concluído. Arquivo salvo como {zip_filename}")
    except Exception as e:
        print(f"Erro durante o processo: {e}")

    finally:
        if os.path.exists(pdf_filename):
            os.remove(pdf_filename)


if __name__ == "__main__":
    main()
