#Autor:Diego Silva
#Data:19/01/2020
#Descrição:classes reponsavei pelo cadastro de notas

from flask import request
from flask_restful import Resource

notas=[]

class CadastroNotasCorte(Resource):

	def get(self, dispositivo):
		item = next(filter(lambda x: x['dispositivo']==dispositivo, notas),None)
		return {"dispositivo":item}, 200 if item is not None else 404

	def post(self, dispositivo):
		cadastronota = request.get_json()
		if next(filter(lambda x: x['dispositivo'] == dispositivo, notas), None):
			return {'Mensagem':'Já existe noda de serviços apra esse dispositivo'}, 400

		nova_nota={
			'dispositivo':dispositivo,
			'corte':cadastronota['corte']

		}
		notas.append(nova_nota)
		return nova_nota, 201

	def delete(self, dispositivo):
		global notas
		notas = list(filter(lambda x: x['dispositivo'] != dispositivo, notas))
		return {'Mensagem item deletado':'nota'}

class ListaNotas(Resource):
	def get(self):
		return {'Notas':notas}