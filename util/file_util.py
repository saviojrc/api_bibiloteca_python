import os
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, '../payload/data.json')


class FileUtil:

    ## Metodo que carrega o aquivo data.json da pasta payload
    ## para o formato json e com o encoding utf-8
    def get_payload(self):
        import json
        with open(path) as json_file:
            data = json.load(json_file, encoding='utf-8')
            return data

