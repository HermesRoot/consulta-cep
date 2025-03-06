from flask import Flask, request, jsonify
import requests
import re
from flask_cors import CORS  # Importa o CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Função para validar o formato do CEP (apenas números e 8 dígitos)
def validar_cep(cep):
    return bool(re.match(r"^\d{8}$", cep))  # Verifica se o CEP tem 8 dígitos numéricos

# Rota para consultar o CEP
@app.route("/consulta-cep", methods=["GET"])
def consulta_cep():
    cep = request.args.get("cep")
    
    if not cep:
        return jsonify({"erro": "O parâmetro 'cep' é obrigatório."}), 400
    
    if not validar_cep(cep):
        return jsonify({"erro": "CEP inválido. O CEP deve ter 8 dígitos."}), 400

    try:
        response = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
        response.raise_for_status()  # Lança um erro se a resposta for ruim (não 2xx)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": "Erro ao consultar o CEP.", "detalhes": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
