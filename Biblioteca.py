from conexao import connect


def inserir(mydb, id_livro, titulo, autor, ano_pub, status):
    mycursor = mydb.cursor()
    sql = "INSERT INTO livros (id_livro, titulo, autor, ano_pub, status) VALUES (%s, %s, %s, %s, %s)"
    val = (id_livro, titulo, autor, ano_pub, status)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Inserido com Sucesso.")
    mycursor.close()

def atualizar(mydb):
    print('')
    print('Atualizando: ')
    print('1. Atualizar título')
    print('2. Atualizar autor')
    print('3. Atualizar ano de publicação')
    print('4. Atualizar tudo')
    op = str(input('Digite a opção desejada: '))
    print('')

    if op == '4':
       mycursor = mydb.cursor()
       id01 = int(input('Digite o id do livro desejado: '))
       t01 = str(input('Digite o novo título: '))
       a01 = str(input('Digite o novo autor: '))
       ano01 = str(input('Digite o novo ano de publicação: '))

       sql = "UPDATE livros SET titulo=%s, autor=%s, ano_pub=%s WHERE id_livro=%s"
       val = (t01, a01, ano01, id01)
       
       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Atualizado com Sucesso.")
       mycursor.close()

    elif op == '1':
        mycursor = mydb.cursor()
        id01 = int(input('Digite o id do livro desejado: '))
        t01 = str(input('Digite o novo título: '))

        sql = "UPDATE livros SET titulo=%s WHERE id_livro=%s"
        val = (t01, id01)

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()

    elif op == '2':
        mycursor = mydb.cursor()
        id01 = int(input('Digite o id do livro desejado: '))
        a01 = str(input('Digite o novo autor: '))

        sql = "UPDATE livros SET autor=%s WHERE id_livro=%s"
        val = (a01, id01)

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()
        
    elif op == '3':
       mycursor = mydb.cursor()
       id01 = int(input('Digite o id do livro desejado: '))
       ano01 = int(input('Digite o novo ano de publicação: '))

       sql = "UPDATE livros SET ano_pub=%s WHERE id_livro=%s"
       val = (ano01, id01)

       mycursor.execute(sql, val)
       mydb.commit()
       print(mycursor.rowcount, "Atualizado com Sucesso.")
       mycursor.close()

def listar(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM livros"

    mycursor.execute(sql)
    resultado = mycursor.fetchall()
    print(resultado)
    mycursor.close()

def deletar(mydb, id_livro):
    mycursor = mydb.cursor()
    
    sql = "DELETE FROM livros WHERE id_livro=%s"
    val = (id_livro,)
       
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Livro deletado.")
    mycursor.close()

def emprestar(mydb, id_livro):
    mycursor = mydb.cursor()
    status = 'Emprestado'
    
    sql = "UPDATE livros SET status=%s WHERE id_livro=%s"
    val = (status, id_livro)
       
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Livro emprestado.")
    mycursor.close()
    
def devolver(mydb, id_livro):
    mycursor = mydb.cursor()
    status = 'Disponível'
    
    sql = "UPDATE livros SET status=%s WHERE id_livro=%s"
    val = (status, id_livro)
       
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Livro devolvido.")
    mycursor.close()