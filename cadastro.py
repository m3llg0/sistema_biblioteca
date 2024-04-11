import hashlib
from conexao import connect

mydb = connect()


def cadastrar_usuario(mydb, id_cliente, nome, email, senha, cpf):
    mycursor = mydb.cursor()
    sql = "INSERT INTO cadastro (id_cliente, nome, email, senha, cpf) VALUES (%s, %s, %s, %s, %s)"
    val = (id_cliente, nome, email, senha, cpf)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Usuário cadastrado com sucesso!")
    mycursor.close()

def fazer_login(mydb, email, senha):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM cadastro WHERE email=%s AND senha=%s"
    val = (email, senha)
    mycursor.execute(sql, val)

    usuario = mycursor.fetchone()
    if usuario:
        print("Login bem-sucedido!")
        return usuario
    else:
        print("E-mail ou senha incorretos.")
        return None

    mycursor.close()