import requests as rq
import json

countok=0
countnok=0
#criando listas
listalink=[]
listanota=[]

#cabeçalho padrão
headers = {'content-type':'application/json'}
#links de acesso para cadastros notaas
linkdevice1 = 'http://127.0.0.1:5001/cadastronota/2c3ae80aaa6a'
linkdevice2 = 'http://127.0.0.1:5001/cadastronota/2e75e68a936a'
linkdevice3 = 'http://127.0.0.1:5001/cadastronota/2c3ae50a936a'

listalink.append(linkdevice1)
listalink.append(linkdevice2)
listalink.append(linkdevice3)

nota1={'corte':0}
nota2={'corte':1}
nota3={'corte':0}

listanota.append(nota1)
listanota.append(nota2)
listanota.append(nota3)

#teste de post no webservice
for busca in range(0,len(listalink)):
	print('Teste Link Post{} usando json{}'.format(listalink[busca],listanota[busca]))
	dados = rq.post(url=listalink[busca], data=json.dumps(listanota[busca]), headers=headers)
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