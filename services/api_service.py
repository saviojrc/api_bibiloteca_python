from flask import Flask, jsonify, request

from util.file_util import FileUtil

file_util = FileUtil()
livros = file_util.get_payload()['livros']

app = Flask(__name__)


class APIService:
    @staticmethod
    @app.route('/api/v1/livros', methods=['GET'])
    def get_livros():
        if (len(livros)>0):
            return jsonify(livros), 200
        else:
            return jsonify({'message': 'Nenhum livro encontrado'}), 404

    @staticmethod
    @app.route('/api/v1/livros/<int:codigo>', methods=['GET'])
    def obter_livro_por_id(codigo: int):
        livro = next((livro for livro in livros if livro['codigo'] == codigo), None)
        if livro:
            return jsonify(livro), 200
        elif isinstance(codigo, int):
            return jsonify({'message': 'O código deve ser um número'}), 400
        else:
            return jsonify({'message': 'Livro não encontrado'}), 404

    @staticmethod
    @app.route('/api/v1/livros/<int:codigo>', methods=['PUT'])
    def alterar_livro_por_codigo(codigo: int):
        livro_alterado = request.get_json()
        for indice, livro in enumerate(livros):
            if livro.get('codigo') == codigo:
                livros[indice].update(livro_alterado)
                return jsonify(livros[indice]), 200
            else:
                return jsonify({'message': 'Livro não encontrado'}), 404

    @staticmethod
    @app.route('/api/v1/livros', methods=['POST'])
    def incluir_novo_livro():
        novo_livro = request.get_json()
        livros.append(novo_livro)
        return jsonify(novo_livro), 201

    @staticmethod
    @app.route('/api/v1/livros/<int:codigo>', methods=['DELETE'])
    def excluir_livro_por_codigo(codigo: int):
        for indice, livro in enumerate(livros):
            if livro.get('codigo') == codigo:
                livros.pop(indice)
                return jsonify({'message': 'Livro excluído com sucesso'}), 200
            else:
                return jsonify({'message': 'Livro não encontrado'}), 404


app.run(port=5000, debug=True, host='localhost')
