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

@app.route('/listarIndividual', methods=['GET', 'POST'])
def listarPorCpf():
    if request.method == 'GET':
        return render_template('listar.html', titulo="Listar Usuário")

    if request.method == 'POST':
        try:
            cpf = request.form.get("cpf")

            requisicao = requests.get(f'{link}/cadastro/.json')
            dicionario = requisicao.json()

            usuario_encontrado = None
            for codigo in dicionario:
                if dicionario[codigo]['cpf'] == cpf:
                    usuario_encontrado = dicionario[codigo]
                    break

            if not usuario_encontrado:
                return f"CPF {cpf} não encontrado."

            return usuario_encontrado

        except Exception as e:
            return f"Algo deu errado: {e}"

@app.route ('/listar')
def listar():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '12321312231':
                idCadastro  = codigo
                return codigo

    except Exception as e:
        return f'Algo deu errado \n+ {e}'


@app.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    if request.method == 'GET':
        return render_template('atualizar.html', titulo="Atualizar Usuário")

    if request.method == 'POST':
        try:
            cpf = request.form.get("cpf")
            novo_nome = request.form.get("nome")
            novo_telefone = request.form.get("telefone")
            novo_endereco = request.form.get("endereco")


            requisicao = requests.get(f'{link}/cadastro/.json')
            dicionario = requisicao.json()

            idCadastro = None
            for codigo in dicionario:
                if dicionario[codigo]['cpf'] == cpf:
                    idCadastro = codigo
                    break

            if not idCadastro:
                return f" CPF {cpf} não encontrado.",

            dados_atualizados = {
                "nome": novo_nome,
                "telefone": novo_telefone,
                "endereco": novo_endereco
            }
            requisicao_atualizacao = requests.patch(f'{link}/cadastro/{idCadastro}.json',
                                                    data=json.dumps(dados_atualizados))

            if requisicao_atualizacao.status_code == 200:
                return "Atualizado com sucesso!"
            else:
                return f"Erro ao atualizar: {requisicao_atualizacao.text}"

        except Exception as e:
            return f"Algo deu errado: {e}"


@app.route ('/excluir')
def excluir():
    try:
        requisicao = requests.delete('f{link}/cadastro/-O8miHXi41Az4ljED92S.json',data = json.dumps(dados))
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n+ {e}'
