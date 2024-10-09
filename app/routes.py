from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintvinicius-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Pagina inicial")
@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contatos")
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="cadastro")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuarios():
    try:
        cpf      = request.form.get("cpf")
        nome     = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados    = {"cpf": cpf, "nome":nome, "telefone": telefone, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro \n+ {e}'

@app.route ('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Algo deu errado \n+ {e}'

@app.route ('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = "" #Coletar id
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '12321312231':
                idCadastro  = codigo
                return codigo

    except Exception as e:
        return f'Algo deu errado \n+ {e}'

@app.route ('/atualizar')

def atualizar():
    try:
        dados = {"nome": "joão"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miHXi41Az4ljED92S.json', data = json.dumps(dados))
        return "atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n+ {e}'


@app.route ('/excluir')
def excluir():
    try:
        requisicao = requests.delete('f{link}/cadastro/-O8miHXi41Az4ljED92S.json',data = json.dumps(dados))
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n+ {e}'
