from conexao import connect
from Biblioteca import inserir
from Biblioteca import atualizar
from Biblioteca import listar
from Biblioteca import deletar
from Biblioteca import emprestar
from Biblioteca import devolver
from cadastro import cadastrar_usuario
from cadastro import fazer_login

mydb = connect()

while True:
    print(" ")
    print("Bem vindo à Biblioteca!")
    print(" ")
    print("Selecione a operação desejada: ")
    print(" ")
    print("1. Registrar usuário")
    print('2. Fazer login')
    print("3. Inserir livro")
    print('4. Atualizar livro')
    print("5. Excluir livro")
    print('6. Consultar livros')
    print("7. Emprestar livro")
    print("8. Devolver livro")
    print("9. Sair")
    print(" ")
    opcao = input("Escolha uma opção: ")
    print(" ")

    if opcao == '9':
        break

    elif opcao == "1":
        id_cliente = int(input('Digite o id do usuário: '))
        n01 = str(input('Digite o nome do usuário: '))
        e01 = str(input('Digite o email do usuário: '))
        s01 = str(input('Digite a senha: '))
        cpf01 = str(input("Insira o CPF do usuário: "))
        cadastrar_usuario(mydb, id_cliente, n01, e01, s01, cpf01)

    elif opcao == "2":
        e01 = input("Digite o email: ")
        s01 = input("Digite a senha: ")
        usuario = fazer_login(mydb, e01, s01)

    elif opcao == "3":
        id_livro01 = int(input('Digite o id do livro: '))
        t01 = str(input('Digite o título do livro: '))
        a01 = str(input('Digite o autor do livro: '))
        ano01 = int(input('Digite o ano de publicação do livro: '))
        st01 = 'Disponível'
        inserir(mydb, id_livro01, t01, a01, ano01, st01)


        id_livro01 = int(input('Digite o id do livro: '))
        emprestar(mydb, id_livro01)

    elif opcao == "4":
        atualizar(mydb)
    
    elif opcao == "5":
        id_livro01 = int(input('Digite o id do livro: '))
        deletar(mydb, id_livro01)

    elif opcao == "6":
        listar(mydb)

    elif opcao == "7":
        id_livro01 = int(input('Digite o id do livro: '))
        emprestar(mydb, id_livro01)
    
    elif opcao == "8":
        id_livro01 = int(input('Digite o id do livro: '))
        devolver(mydb, id_livro01)
    
    else:
        print("Opção inválida! Por favor, tente novamente!")

   

       
       
   

