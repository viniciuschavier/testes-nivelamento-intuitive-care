# Teste Transformação de Dados

Esta resolução tem como objetivo extrair dados da tabela **Rol de Procedimentos e Eventos em Saúde** presente no PDF disponibilizado pela ANS (Agência Nacional de Saúde Suplementar). Os dados extraídos são salvos em um arquivo **CSV** e posteriormente compactados em um **arquivo ZIP**.

### 📌 Funcionalidades
- Download automático do PDF diretamente do site da ANS.
- Extração de tabelas contidas no PDF.
- Extração automática das legendas correspondentes a "OD" e "AMB".
- Substituição das abreviações "OD" e "AMB" por suas respectivas descrições.
- Geração do arquivo CSV com separador ponto e vírgula ( ; ).
- Compactação do arquivo CSV em um ZIP salvo na mesma pasta do script.

### 🛠️ Bibliotecas Utilizadas
- `pdfplumber` → Extração de tabelas do PDF.
- `pandas` → Manipulação e formatação dos dados.
- `requests` → Download do PDF via HTTP.
- `zipfile` → Compactação do arquivo CSV.
- `os` → Manipulação de arquivos e diretórios.
- `re` → Expressões regulares para extração das legendas.

### 🚀 Como Executar

### 1️⃣ Instalar dependências
```bash
pip install pdfplumber pandas requests
```
### 2️⃣ Executar o script
```bash
python index.py
```