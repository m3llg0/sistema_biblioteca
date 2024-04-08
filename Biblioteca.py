from conexao import connect

class Biblioteca:
    def __init__ (self, id_livro, titulo, autor, ano_pub, status):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano_pub = ano_pub
        self.status = 'Disponível'

    def inserir(mydb, titulo, autor):
        mycursor = mydb.cursor()
        sql = "INSERT INTO livros (titulo, autor) VALUES (%s, %s)"
        val = (titulo, autor)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Inserido com Sucesso.")
        mycursor.close()

    def atualizar(mydb, id_livro, titulo, autor):
        mycursor = mydb.cursor()
        mydb.cursor.execute('''UPDATE livros SET titulo=?, autor=? WHERE id=?''',
                            (titulo, autor, id_livro))
        mydb.conn.commit()
        print(mycursor.rowcount, "Inserido com Sucesso.")
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
