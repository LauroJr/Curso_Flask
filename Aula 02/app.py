# Criando Rotas e configurações

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


def teste():
    return '<p>Testando 1</p>'


def teste2():
    return '<p>Testando 2</p>'


# outra forma de criar rotas

app.add_url_rule('/test', 'teste', teste)
app.add_url_rule('/testt', 'teste2', teste)

if __name__ == '__main__':
    app.run(debug=True, port="3000")
    ''' Neste trecho, o debug=True serve como um atualizador de página
    sem ser preciso 'matar' o servidor a cada mudança. Ele já faz esse serviço
    na porta 3000 como descrito em sua sequência pela sintaxe 'por='3000'. '
    '''
