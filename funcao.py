from conexao import connect

def insert(mydb, titulo, autor):
    mycursor = mydb.cursor()
    sql = "INSERT INTO livros (titulo, autor) VALUES (%s, %s)"
    val = (titulo, autor)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Inserido com Sucesso.")
    mycursor.close()

def update(mydb, titulo, ano_pub):
    mycursor = mydb.cursor()
    update_query = "UPDATE Livros SET ano_pub = %s WHERE titulo = %s"
    mycursor.execute(update_query, (titulo, ano_pub))
    mycursor.execute(update_query)
    mycursor.commit()
    print(mycursor.rowcount, "Atualizado com Sucesso.")
    mycursor.close()


def select(mydb, autor):
    mycursor = mydb.cursor()
    select_query = "SELECT * FROM Livros WHERE autor = %s"
    mydb.execute(select_query, (autor))
    Livros = mydb.fetchall()
    for livro in Livros:
        print(livro)
    mycursor.execute(select_query)
    mydb.commit()
    print(mycursor.rowcount, "Inserido com Sucesso.")
    mycursor.close()
