import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita o CORS para todas as rotas

# Carrega os dados do CSV uma vez ao iniciar o servidor
df = pd.read_csv('https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv',
                 delimiter=';', encoding='UTF-8')

# Cria a rota '/buscar_operadoras' para buscar operadoras


@app.route('/buscar_operadoras', methods=['GET'])
def buscar_operadoras():
    # Pega o termo da requisição e converte para minúsculas
    termo = request.args.get('termo', '').lower()

    # Faz a conversão das colunas para string e verifica se contem o termo em qualquer coluna
    resultados = df[df.apply(lambda row: row.astype(
        str).str.lower().str.contains(termo).any(), axis=1)]

    # Substitui os valores NaN por "None"
    resultados = resultados.fillna(value="None")

    # Se não encontrar resultados para o termo, retorna uma mensagem de erro
    if resultados.empty or termo == "":
        return jsonify({"erro": "Nenhuma operadora encontrada para o termo informado."}), 404

    # Retorna os resultados encontrados como JSON
    return jsonify(resultados.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
