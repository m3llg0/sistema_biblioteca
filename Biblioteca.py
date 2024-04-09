from conexao import connect


def inserir(mydb, id_livro, titulo, autor, ano_pub, status):
    mycursor = mydb.cursor()
    sql = "INSERT INTO livros (titulo, autor, ano_pub, status, id_livro) VALUES (%s, %s, %s, %s, %s)"
    val = (titulo, autor, ano_pub, status, id_livro)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Inserido com Sucesso.")
    mycursor.close()

def atualizar(mydb):
    mycursor = mydb.cursor()
    print('')
    print('Atualizando: ')
    print('1. Atualizar título')
    print('2. Atualizar autor')
    print('3. Atualizar ano de publicação')
    print('4. Atualizar tudo')
    op = str(input('Digite a opção desejada: '))
    print('')

    if op == '4':
        id01 = int(input('Digite o id do livro desejado: '))
        t01 = str(input('Digite o novo titulo: '))
        a01 = str(input('Digite o novo autor: '))
        ap01 = int(input('Digite o novo ano de publicação: '))

        sql = "UPDATE livros SET titulo=?, autor=?, ano_pub=? WHERE id=?"
        val = (t01, a01, ap01, id01)

        mycursor.execute(sql, val)
        mydb.conn.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()
    elif op == '1':
        id01 = int(input('Digite o id do livro desejado: '))
        t01 = str(input('Digite o novo nome: '))

        sql = "UPDATE livros SET titulo=? WHERE id=?"
        val = (t01, id01)

        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()

    elif op == '2':
        id01 = int(input('Digite o id do livro desejado: '))
        a01 = str(input('Digite o novo autor: '))

        sql = "UPDATE livros SET autor=? WHERE id=?"
        val = (a01,id01)

        mycursor.execute(sql, val)
        mydb.conn.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()
        
    elif op == '3':
        id01 = int(input('Digite o id do livro desejado: '))
        ap01 = int(input('Digite o novo ano de publicação: '))

        sql = "UPDATE livros SET ano_pub=? WHERE id=?"
        val = (ap01, id01)

        mycursor.execute(sql, val)
        mydb.conn.commit()
        print(mycursor.rowcount, "Atualizado com Sucesso.")
        mycursor.close()

def listar(self):
    mycursor = self.cursor()
    self.cursor.execute('''SELECT * FROM livros''')
    return self.cursor.fetchall()
    mycursor.close()

def deletar(self, livro_id):
    self.cursor.execute('''DELETE FROM livros WHERE id=?''', (livro_id,))
    self.conn.commit()

def emprestar(self, livro_id):
    self.cursor.execute('''UPDATE livros SET disponivel=? WHERE id=?''',
                        (False, livro_id))
    self.conn.commit()
    
def devolver(self, livro_id):
    self.cursor.execute('''UPDATE livros SET disponivel=? WHERE id=?''',
                        (True, livro_id))
    self.conn.commit()
