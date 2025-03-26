import os
import requests
import zipfile
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Criação da pasta temporária para os downloads dos anexos
output_folder = "anexos"
os.makedirs(output_folder, exist_ok=True)

# O arquivo será compactado neste caminho
zip_filename = "testeWebScraping/anexos_compactados.zip"

# Requisição para obter o HTML da página
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Lista para armazenar os arquivos baixados
pdf_files = []

# Encontra todos os links da página
for link in soup.find_all("a"):
    href = link.get("href")

    # Verifica se o link contém Anexo I e Anexo II e filtra somente links que contem .pdf
    if href.endswith(".pdf") and ("Anexo I" in link.text or "Anexo II" in link.text):
        pdf_url = urljoin(url, href)
        pdf_name = os.path.join(output_folder, os.path.basename(pdf_url))
        pdf_files.append(pdf_name)

        # Faz o download dos anexos
        with requests.get(pdf_url, stream=True) as pdf_response:
            with open(pdf_name, "wb") as pdf_file:
                for chunk in pdf_response.iter_content(chunk_size=1024):
                    pdf_file.write(chunk)

        print(f"Baixado: {pdf_name}")

# Compacta os arquivos em um único .zip
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for pdf in pdf_files:
        zipf.write(pdf, os.path.basename(pdf))

print(f"Arquivos compactados em: {zip_filename}")

shutil.rmtree(output_folder)  # Exclui a pasta que não está compactada
