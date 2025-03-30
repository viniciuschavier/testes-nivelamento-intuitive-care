# Teste API Python com Vue.js

Esta resolução consiste em uma interface web desenvolvida em Vue.js que interage com um servidor Flask para buscar informações de operadoras de saúde a partir de um arquivo CSV da ANS (Agência Nacional de Saúde Suplementar).

📌 **Tecnologias Utilizadas**

* **Frontend:** Vue.js, Bootstrap, Axios
* **Backend:** Flask, Pandas, Flask-CORS
* **Base de Dados:** CSV disponível no site da ANS

🚀 **Como Executar o Projeto**

**1️⃣ Backend (Flask)**

* **Instale as dependências necessárias:**

    ```bash
    pip install flask pandas flask-cors
    ```

* **Execute o servidor Flask:**

    ```bash
    python testeAPI\testeapi\src\servidor\index.py
    ```

    O backend será iniciado em `http://localhost:5000`.

**2️⃣ Frontend (Vue.js)**

* **Acesse a pasta do frontend e instale as dependências:**

    ```bash
    npm install
    ```

* **Execute o servidor Vue.js:**

    ```bash
    npm run serve
    ```

    O frontend será iniciado em `http://localhost:8080`.

📄 **Endpoints da API**

* `GET /buscar_operadoras?termo=<busca>`
    * **Parâmetro:** `termo` texto inserido no input.
    * **Resposta:** JSON com uma lista de dicionários, onde cada dicionário representa uma operadora encontrada. Se nenhuma operadora for encontrada, retorna um JSON com uma mensagem de erro.

**Link da coleção no postman**
* **https://viniciuschavier.postman.co/workspace/Vinicius-Chavier's-Workspace~dd2d9508-75da-431e-8a7e-33fd6d760766/collection/43597106-eedcfe61-9857-45ef-ae5e-1f2cf7ba4cc8?action=share&creator=43597106**