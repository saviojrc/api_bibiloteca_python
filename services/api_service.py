from flask import Flask, jsonify
from util.file_util import FileUtil

file_util = FileUtil()
livros = file_util.get_payload()

app = Flask(__name__)


class APIService:
    @staticmethod
    @app.route('/api/v1/livros', methods=['GET'])
    def get_livros():
        return jsonify({'livros': livros})



    @staticmethod
    @app.route('/api/v1/livros/<int:id>', methods=['GET'])
    def obter_livro_por_id(id: int):
        for livro in livros:
            if livro.get("id") == id:
                return jsonify({'livro': livro})


app.run(port=5000, debug=True, host='localhost')
