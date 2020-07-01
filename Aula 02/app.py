# Criando Rotas e configurações

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


def ola_mundo():
    return '<p>Olá, Mundo!</p>'


def test_two():
    return '<p>Testando 2</p>'


def titulo():
    return '<h1>Corinthians</h1>'


# outra forma de criar rotas

#                   rota      função    return(nome tem que ser igual a função, ou de alguma def existente)
app.add_url_rule('/world', 'ola_mundo', ola_mundo)
app.add_url_rule('/teste-2', 'test_two', test_two)
app.add_url_rule('/time', 'titulo', titulo)

if __name__ == '__main__':
    app.run(debug=True, port="3000")
    ''' Neste trecho, o debug=True serve como um atualizador de página
    sem ser preciso 'matar' o servidor a cada mudança. Ele já faz esse serviço
    na porta 3000 como descrito em sua sequência pela sintaxe 'por='3000'. '
    '''
