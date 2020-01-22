#Autor:Diego Silva
#Data:21/01/20
#Descricao:Serviço para cadastro de clientes

from flask import request
from flask_restful import Resource

#criando lista para armazena dados
usuarios = []

class Cliente(Resource):

    def get(self, usuario):
        usuario = next(filter(lambda x: x['usuario']==usuario, usuarios),None)
        return {"dispositivo":usuario}, 200 if usuario is not None else 404

    def post(self, usuario):
        dadoscadastro = request.get_json()
        if next(filter(lambda x: x['usuario'] == usuario, usuarios), None):
            return {'Mensagem':'Usuario {} já cadastrado'.format(usuario)}, 400

        novo_usuario = {
					'usuario':usuario,
					'senha':dadoscadastro['senha'],
					'nome':dadoscadastro['nome'],
					'sobrenome':dadoscadastro['sobrenome'],
                    'endereco':dadoscadastro['endereco'],
                    'cpfcnpj':dadoscadastro['cpfcnpj'],
                    'contato1':dadoscadastro['contato1'],
                    'contato2':dadoscadastro['contato2']
		}

        usuarios.append(novo_usuario)
        return novo_usuario, 201

class ListaCliente(Resource):

    def get(self):
        return  {'usuarios':usuarios}