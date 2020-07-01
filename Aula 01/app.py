# Aula 01 - Instalando Flask
''' pip install flask ... lembre-se de instalar o ambiente virtual. Em
consequência disso, todo os plugins para cada apalicação com flask'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/teste')
def teste():
    return 'Teste'


if __name__ == '__main__':
    app.run()
