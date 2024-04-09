from conexao import connect
from biblioteca import inserir
from biblioteca import atualizar
from biblioteca import listar
from biblioteca import deletar
from biblioteca import emprestar
from biblioteca import devolver

mydb = connect()

while True:
    print("Bem vindo à Biblioteca!")
    print(" ")
    print("1. Adicionar um livro")
    print('2. Atualizar um livro')
    print("3. Emprestar um livro")
    print('4. Listar os livros')
    print("5. Devolver um livro")
    print('6. Deletar um livro')
    print("7. Sair do programa")
    print(" ")

    opcao = input("Escolha uma opção: ")

    if opcao == '7':
        break

    elif opcao == "1":
        id_livro01 = int(input('Digite o id do livro: '))
        t01 = str(input('Digite o título do livro: '))
        a01 = str(input('Digite o autor do livro: '))
        ano01 = int(input('Digite o ano de publicação do livro: '))
        st01 = 'Disponível'
        inserir(mydb, id_livro01, t01, a01, ano01, st01)

    elif opcao == "2":
        atualizar(mydb)

    elif opcao == "3":
        id_livro01 = int(input('Digite o id do livro: '))
        emprestar(mydb, id_livro01)

    elif opcao == "4":
        listar(mydb)
    
    elif opcao == "5":
        id_livro01 = int(input('Digite o id do livro: '))
        devolver(mydb, id_livro01)

    elif opcao == "6":
        id_livro01 = int(input('Digite o id do livro: '))
        deletar(mydb, id_livro01)
    
    else:
        print("Opção inválida! Por favor, tente novamente!")

   

       
       
   

