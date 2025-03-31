# Teste de Web Scraping

Esta resolução realiza o **web scraping** da página da ANS para baixar os arquivos **Anexo I e Anexo II** em formato PDF. Após o download, os arquivos são compactados em um **arquivo ZIP** dentro da pasta `testeWebScraping/`.

### 📌 Funcionalidades
- Acessa a página da [ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Localiza e baixa os arquivos **Anexo I** e **Anexo II**
- Salva os PDFs temporariamente na pasta `testeWebScraping/anexos/`
- Compacta os arquivos baixados em `testeWebScraping/anexos_compactados.zip`
- Remove a pasta temporária após a compactação

### 🛠️ Bibliotecas Utilizadas
- `Requests` → Fazer requisições HTTP
- `BeautifulSoup4`  →  Extrair informações do HTML
- `Zipfile` → Compactar arquivos
- `Shutil` → Manipulação de arquivos e diretórios

### 🚀 Como Executar

#### 1️⃣ Instalar dependências
```bash
pip install requests beautifulsoup4
```

#### 2️⃣ Executar o script
```bash
python index.py
```