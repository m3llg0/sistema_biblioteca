class Livro:
    def _init_(self, titulo, autor, ano_publi, status):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.status = "Disponível"

    def verificar_dispo(self):
        if self.status == "Disponível":
            print("O livro '{}' está disponível para empréstimo.".format(self.titulo))
        else:
            print("O livro '{}' está atualmente emprestado.".format(self.titulo))

    def alt_status(self, novo_status):
        if novo_status == "Disponível" or novo_status == "Emprestado":
            self.status = novo_status
            print("O status do livro '{}' foi alterado para '{}'.".format(self.titulo, novo_status))
        else:
            print("Status inválido. O status deve ser 'Disponível' ou 'Emprestado'.")