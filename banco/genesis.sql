/*
Autor:Diego Silva
Data:21/01/2020
Descrição:Script para criação de banco
*/

--craindo base de dados
create database act_iot;

--commit
commit;

--carregando base
use act_iot;

--criando tabelas de versão
create table versaosistema(
	versao int not null,
	funcionalidade int not null,
	funcionalidadealterada int not null,
	correcao
)