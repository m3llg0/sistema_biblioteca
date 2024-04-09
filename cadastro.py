import sqlite3
import hashlib
from conexao import connect
mydb = connect()

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    cpf TEXT NOT NULL
                )''')

conn.commit()

def cadastrar_usuario(nome, email, senha, cpf):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    cursor.execute('INSERT INTO usuarios (nome, email, senha, cpf) VALUES (?, ?, ?, ?)', (nome, email, senha_hash, cpf))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

def fazer_login(email, senha):
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    cursor.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha_hash))
    usuario = cursor.fetchone()
    
    if usuario:
        print("Login bem-sucedido!")
    else:
        print("E-mail ou senha incorretos.")

cadastrar_usuario("Emilly Marrocos", "emilly@example.com", "senha123", "123.456.789-00")
fazer_login("emilly@example.com", "senha123")
fazer_login("emilly@example.com", "senha456")

conn.close()