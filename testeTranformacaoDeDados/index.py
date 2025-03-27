import pdfplumber
import pandas as pd
import zipfile
import os
import requests


def download_pdf(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF baixado com sucesso: {save_path}")
    else:
        print("Erro ao baixar o PDF")
        exit()


def extract_table_from_pdf(pdf_path):
    data = []
    header = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    cleaned_row = [
                        " ".join(str(cell).splitlines()) if cell else "" for cell in row]
                    if header is None:
                        header = cleaned_row
                        data.append(header)
                    elif cleaned_row != header:
                        data.append(cleaned_row)
    return data


def clean_and_save_data(data, output_csv):
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)  # Remove a linha duplicada do cabeçalho

    # Substituir abreviações
    substitutions = {"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}
    df.replace(substitutions, inplace=True)

    df.to_csv(output_csv, index=False, sep=";")


def compress_csv(csv_filename, zip_filename):
    # Caminho onde o arquivo compactado será salvo
    zip_path = os.path.join(os.path.dirname(__file__), zip_filename)
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))
    os.remove(csv_filename)


def main():
    pdf_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    pdf_filename = "Anexo_I_Rol_2021.pdf"
    csv_filename = "Rol_de_Procedimentos.csv"
    zip_filename = "Teste_{vinicius_chavier}.zip"

    print("Baixando PDF...")
    download_pdf(pdf_url, pdf_filename)

    print("Extraindo dados do PDF...")
    data = extract_table_from_pdf(pdf_filename)
    print("Salvando dados em CSV...")
    clean_and_save_data(data, csv_filename)
    print("Compactando CSV...")
    compress_csv(csv_filename, zip_filename)
    print(f"Processo concluído. Arquivo salvo como {zip_filename}")
    os.remove(pdf_filename)


if __name__ == "__main__":
    main()
