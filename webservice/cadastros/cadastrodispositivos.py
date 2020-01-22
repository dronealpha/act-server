#Autor:Diego Silva
#Data:18/01/2020
#Descrição:classes reponsavei pelo cadastro de dispostivos

from flask import request
from flask_restful import Resource


#lista de dispositivos/notas
dispositivos=[]

#Cadastro de dispositivos
class CadastroDispositivo(Resource):

	#retorna dispositivo especifico
	def get(self, dispositivo):
		item = next(filter(lambda x: x['dispositivo']==dispositivo, dispositivos),None)
		return {"dispositivo":item}, 200 if item is not None else 404

	#cadastrata dispositivos
	def post(self, dispositivo):
		dadoscadastro = request.get_json()
		if next(filter(lambda x: x['dispositivo'] == dispositivo, dispositivos), None):
			return {'Mensagem':'Dispositivo {} já cadastrado'.format(dispositivo)}, 400

		novo_dispostivo = {
					'dispositivo':dispositivo,
					'data':dadoscadastro['data'],
					'status':dadoscadastro['status'],
					'endereco':dadoscadastro['endereco']
		}
		dispositivos.append(novo_dispostivo)
		return novo_dispostivo, 201

	def delete(self, dispositivo):
		global dispositivos
		dispositivos = list(filter(lambda x: x['dispositivo'] != dispositivo, dispositivos))
		return {'Mensagem item deletado':'Item deleted'}

#classe para listar todos os dispositivos
class ListaDispositivos(Resource):
	def get(self):
		return {'Dispositivos':dispositivos}