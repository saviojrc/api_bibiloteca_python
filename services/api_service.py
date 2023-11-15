from flask import Flask, jsonify
from util.file_util import FileUtil

file_util = FileUtil()
livros = file_util.get_payload()['livros']

app = Flask(__name__)


class APIService:
    @staticmethod
    @app.route('/api/v1/livros', methods=['GET'])
    def get_livros():
        return jsonify(livros), 200

    @staticmethod
    @app.route('/api/v1/livros/<int:codigo>', methods=['GET'])
    def obter_livro_por_id(codigo: int):
        livro = next((livro for livro in livros if livro['codigo'] == codigo), None)
        if livro:
            return jsonify(livro), 200
        else:
            return jsonify({'message': 'Livro não encontrado'}), 404


app.run(port=5000, debug=True, host='localhost')
