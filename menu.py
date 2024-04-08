from biblioteca import Biblioteca

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
        Biblioteca.inserir()

    elif opcao == "2":
        Biblioteca.atualizar()

    elif opcao == "3":
        Biblioteca.emprestar()

    elif opcao == "4":
        Biblioteca.listar()
    
    elif opcao == "5":
        Biblioteca.devolver()

    elif opcao == "6":
        Biblioteca.deletar
    
    else:
        print("Opção inválida! Por favor, tente novamente!")

   

       
       
   

