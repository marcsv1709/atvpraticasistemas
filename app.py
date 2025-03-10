from flask import Flask, request, jsonify
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

with open('config.json', 'r') as arquivo_config:
    config = json.load(arquivo_config)
nome_banco = config.get('banco_dados', 'banco_padrao.db')


def inicializar_banco():
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL,
            data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexao.commit()
    conexao.close()
    print(f"[INFO] Banco de dados '{nome_banco}' inicializado com sucesso!")


def salvar_no_banco(login, senha):
    conexao = sqlite3.connect(nome_banco)
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (login, senha) VALUES (?, ?)', (login, senha))
    conexao.commit()
    conexao.close()


@app.route('/status', methods=['GET'])
def verificar_status():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return jsonify({
        'status': 'Servidor online e funcionando!',
        'data_hora': agora,
        'mensagem': 'Envie seu login e senha para a rota /api/autenticar'
    }), 200


@app.route('/api/login', methods=['POST'])
def receber_dados():
    dados = request.get_json()

    login = dados.get('login')
    senha = dados.get('senha')

    if not login or not senha:
        return jsonify({
            'erro': 'Dados incompletos. Envie o login e a senha corretamente.',
            'exemplo': {'login': 'seu_login', 'senha': 'sua_senha'}
        }), 400

    salvar_no_banco(login, senha)

    resposta = {
        'mensagem': 'Dados recebidos com sucesso!',
        'dados_recebidos': {
            'login': login,
            'senha': senha
        },
        'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(resposta), 200


if __name__ == '__main__':
    inicializar_banco() 
    app.run(host='0.0.0.0', port=5000, debug=True)
