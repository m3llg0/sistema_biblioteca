from conexao import connect
from funcao import insert
from funcao import update
from funcao import select

mydb = connect()

t = 'A Seleção'
a = 'Kiera Cass'
ano = 2016

t02 = 'Dom Casmurro'
a02 = 'Machado de Assis'
ano = 1899

# insert(mydb, t, a)
update(mydb, a, ano)
select(mydb, t)

mydb.close()