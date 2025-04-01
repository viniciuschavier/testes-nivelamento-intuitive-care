# 📌 Testes de Nivelamento Intuitive Care

Este repositório contém as resoluções de quatro testes de nivelamento, cada um focado em uma área específica: **Web Scraping, Transformação de Dados, Banco de Dados e API**. Cada teste está armazenado em uma pasta separada, contendo seu próprio README com explicações detalhadas.

## 📂 Estrutura do Projeto

```
/
├── TesteWebScraping/             # Teste 1 - Web Scraping
│   ├── README.md
│   ├── index.py
│   ├── anexos/
│   ├── anexos_compactados.zip
│
├── TesteTransformacaoDeDados/    # Teste 2 - Transformação de Dados
│   ├── README.md
│   ├── index.py
│   ├── dados_extraidos.csv
│   ├── Teste_{vinicius_chavier}.zip
│
├── TesteBancoDeDados/            # Teste 3 - Banco de Dados
│   ├── README.md
│   ├── index.sql
│
├── TesteAPI/                     # Teste 4 - API
│   |── node_modules/
│   |── public/
│       ├── favicon.ico
│       ├── index.html
│   |── src/
│       ├── assets/
│       ├── components/
│       │   ├── ResultadoBusca.vue  # Componente Vue para exibição de resultados
│       ├── servidor/               # Backend em Python
│       │   ├── index.py
│       ├── App.vue
│       ├── main.js
│   |── .gitignore
│   |── babel.config.js
│   |── jsonfig.json
│   |── package-lock.json
│   |── package.json
│   |── postman_collection.json      # Coleção do Postman para testar a API
│   |── README.md
│   |── vue.config.js
│
├── README.md                      # README geral
```

## 📝 Descrição dos Testes

### **1️⃣ Teste de Web Scraping**
Desenvolvido em **Python**, esta resolução acessa a página da ANS, baixa os arquivos **Anexo I e II** em formato PDF e os compacta em um arquivo ZIP.

📌 Mais detalhes: [`TesteWebScraping/README.md`](testeWebScraping/README.md)

### **2️⃣ Teste de Transformação de Dados**
Esta resolução extrai informações do **Anexo I** baixado no Teste 1, converte a tabela "Rol de Procedimentos e Eventos em Saúde" para CSV e compacta o arquivo.

📌 Mais detalhes: [`TesteTransformacaoDeDados/README.md`](testeTransformacaoDeDados/README.md)

### **3️⃣ Teste de Banco de Dados**
Inclui scripts **SQL** para criar e estruturar tabelas no **PostgreSQL**, importar dados dos repositórios públicos da ANS e realizar consultas analíticas sobre despesas de operadoras de planos de saúde.

📌 Mais detalhes: [`TesteBancoDeDados/README.md`](testeBancoDeDados/README.md)

### **4️⃣ Teste de API**
Desenvolvimento de uma interface web usando **Vue.js** e um backend em **Python** para consulta de operadoras de planos de saúde. A API contém uma rota para busca textual nos cadastros.

📌 Mais detalhes: [`TesteAPI/README.md`](testeAPI/testeapi/README.md)

## 🚀 Como Executar o Projeto

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/viniciuschavier/testes-nivelamento-intuitive-care.git
cd teste-nivelamento-intuitive-care
```

2️⃣ **Leia os READMEs individuais** de cada teste para instruções específicas.

## 🏗️ Tecnologias Utilizadas
- **Python** (Web Scraping, Processamento de Dados, Backend da API)
- **SQL** (PostgreSQL)
- **Vue.js** (Frontend da API)
- **Postman** (Testes de API)
