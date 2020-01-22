import requests as rq
import json

countok=0
countnok=0
#criando listas
listajson=[]
listadevice=[]

#links de acesso para cadastros dispositivos
linkdevice1 = 'http://127.0.0.1:5001/cadastrodispositivo/2c3ae80a936a'
linkdevice2 = 'http://127.0.0.1:5001/cadastrodispositivo/2e75e80a936a'
linkdevice3 = 'http://127.0.0.1:5001/cadastrodispositivo/2c3ae49a936a'

listadevice.append(linkdevice1)
listadevice.append(linkdevice2)
listadevice.append(linkdevice3)

#cabeçalho padrão
headers = {'content-type':'application/json'}

#dados de cadastro dispositivo
device1 = { 'data':'05/02/2015',
			'status':'0',
			'endereco':'Rua catuti, 21 vila andrade'}
device2 = { 'data':'05/02/2015',
			'status':'0',
			'endereco':'Rua catuti, 21 vila andrade'}
device3 = { 'data':'05/02/2015',
			'status':'0',
			'endereco':'Rua catuti, 21 vila andrade'}

listajson.append(device1)
listajson.append(device1)
listajson.append(device1)

#teste de post no webservice
for busca in range(0,len(listadevice)):
	print('Teste Link Post{} usando json{}'.format(listadevice[busca],listajson[busca]))
	dados = rq.post(url=listadevice[busca], data=json.dumps(listajson[busca]), headers=headers)
	if(dados.status_code == 201):
		countok=countok+1
	else:
		countnok=countnok+1
		print('Erro>>>>>>'+str(dados.status_code))

print('Fim dos testes de cadastro Post\n')
print('\nSucesso:{}'.format(countok))
print('Falha:{}'.format(countnok))

countnok=0
countok=0

#teste de get web service
for busca in range(0,len(listadevice)):
	print('Teste Link get{}'.format(listadevice[busca]))
	dados = rq.get(url=listadevice[busca])
	if(dados.status_code==200):
		countok=countok+1
	else:
		countnok=countnok+1
		print('Erro>>>>>>'+str(dados.status_code))

print('Fim dos testes de cadastro Post\n')
print('\nSucesso:{}'.format(countok))
print('Falha:{}'.format(countnok))

#teste de delete web service
dados = rq.delete(url=listadevice[0])
if(dados.status_code==200):
	print('Teste de delete OK\n')
else:
	print('Erro>>>>>>'+str(dados.status_code))
