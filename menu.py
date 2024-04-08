import Biblioteca

def add_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")

    Biblioteca.add_livro(titulo, autor)
    print("Livro adicionado com sucesso!")

def emprestar():
    titulo = ("Digite o título do livro que você deseja emprestar: ")
    if Biblioteca.verif_dispo(titulo):
        Biblioteca.emprestar(titulo)
        print("Livro emprestado com sucesso!")
    else: 
        print("O livro não está disponível no momento!")
    
def devolver():
    titulo = input("Digite o título do livro que você deseja devolver: ")
    Biblioteca.devolver(titulo)
    print("O livro foi devolvido com sucesso!")

while True:
    print("Bem vindo à Biblioteca!")
    print(" ")
    print("1. Adicionar um livro")
    print("2. Emprestar um livro")
    print("3. Devolver um livro")
    print("4. Sair do programa")
    print(" ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        add_livro()
    elif opcao == "2":
        emprestar()
    elif opcao == "3":
        devolver()
    elif opcao == "4":
        break
    else:
        print("Opção inválida! Por favor, tente novamente!")

   

       
       
   

