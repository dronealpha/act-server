import requests as rq
import json

countok=0
countnok=0
#criando listas
listajson=[]
listacliente=[]

#links de acesso para cadastros dispositivos
linkuser1 = 'http://127.0.0.1:5001/cliente/redbulldog'
linkuser2 = 'http://127.0.0.1:5001/cliente/viralata'
linkuser3 = 'http://127.0.0.1:5001/cliente/caolouco'

listacliente.append(linkuser1)
listacliente.append(linkuser2)
listacliente.append(linkuser3)


#cabeçalho padrão
headers = {'content-type':'application/json'}

#dados de cadastro dispositivo
user1 =  {
					'senha':'asdf',
					'nome':'Diego',
					'sobrenome':'Silva',
                    'endereco':'vila andrade',
                    'cpfcnpj':'xxxxxxxxxxxxxxxxxxx',
                    'contato1':'asdsaddfasdfasf',
                    'contato2':'asdadsadafdsfds'
		}
user2 = {
					'senha':'asdf',
					'nome':'Marco',
					'sobrenome':'Silva',
                    'endereco':'vila Maua',
                    'cpfcnpj':'xxxxxxxxxxxxxxxxxxx',
                    'contato1':'asdsaddfasdfasf',
                    'contato2':'asdadsadafdsfds'
		}
user3 = {
					'senha':'asdf',
					'nome':'rafael',
					'sobrenome':'lopes',
                    'endereco':'vila mooca',
                    'cpfcnpj':'xxxxxxxxxxxxxxxxxxx',
                    'contato1':'asdsaddfasdfasf',
                    'contato2':'asdadsadafdsfds'
		}

listajson.append(user1)
listajson.append(user2)
listajson.append(user3)

#teste de post no webservice
for busca in range(0,len(listacliente)):
	print('Teste Link Post{} usando json{}'.format(listacliente[busca],listajson[busca]))
	dados = rq.post(url=listacliente[busca], data=json.dumps(listajson[busca]), headers=headers)
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
for busca in range(0,len(listacliente)):
	print('Teste Link get{}'.format(listacliente[busca]))
	dados = rq.get(url=listacliente[busca])
	if(dados.status_code==200):
		countok=countok+1
	else:
		countnok=countnok+1
		print('Erro>>>>>>'+str(dados.status_code))

print('Fim dos testes de cadastro Post\n')
print('\nSucesso:{}'.format(countok))
print('Falha:{}'.format(countnok))

#teste de delete web service
dados = rq.delete(url=listacliente[0])
if(dados.status_code==200):
	print('Teste de delete OK\n')
else:
	print('Erro>>>>>>'+str(dados.status_code))
