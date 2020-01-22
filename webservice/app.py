#Autor:Diego Silva
#Data:18/01/2020
#Descrição:script para cadastro de dipostitivos

#biblioteca flask e flask_restful para tabalhar com micro serviços
from sys import path
path.append('/cadastros')
from flask import Flask 
from flask_restful import Api
from cadastros.cadastrodispositivos import CadastroDispositivo, ListaDispositivos
from cadastros.cadastronotas import CadastroNotasCorte, ListaNotas
from cadastros.cadastrousuario import Cliente, ListaCliente

#instantciando objetos
app = Flask(__name__)
api = Api(app)

#adicionando recursos
api.add_resource(CadastroDispositivo, '/cadastrodispositivo/<string:dispositivo>')
api.add_resource(ListaDispositivos, '/listadispositivos')
api.add_resource(CadastroNotasCorte, '/cadastronota/<string:dispositivo>')
api.add_resource(ListaNotas,'/listanotas')
api.add_resource(Cliente,'/cliente/<string:usuario>')
api.add_resource(ListaCliente, '/listacliente')
if __name__ == '__main__':
	app.run(port=5001, debug=True)



