from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = {}

    def adicionar_livro(self, titulo, autor, copias):
        self.livros.append(Livro(titulo, autor, copias))
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def listar_livros(self):
        print("\nLivros disponíveis na biblioteca:")
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Cópias disponíveis: {livro.copias}")

    def emprestar_livro(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.copias > 0:
                    livro.copias -= 1
                    livro.emprestados.append(usuario)
                    self.usuarios.setdefault(usuario, []).append(titulo)
                    print(f"Livro '{titulo}' emprestado para {usuario}.")
                else:
                    print(f"Livro '{titulo}' não está disponível no momento.")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def devolver_livro(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower() and usuario in livro.emprestados:
                livro.copias += 1
                livro.emprestados.remove(usuario)
                self.usuarios[usuario].remove(titulo)
                print(f"Livro '{titulo}' devolvido por {usuario}.")
                return
        print(f"Erro: Livro '{titulo}' não foi emprestado para {usuario}.")

    def verificar_disponibilidade(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                print(f"Livro '{titulo}' - Cópias disponíveis: {livro.copias}")
                return
        print(f"Livro '{titulo}' não encontrado.")

    def listar_livros_emprestados(self, usuario):
        livros_emprestados = self.usuarios.get(usuario, [])
        if livros_emprestados:
            print(f"\nLivros emprestados por {usuario}:")
            for titulo in livros_emprestados:
                print(f"- {titulo}")
        else:
            print(f"{usuario} não possui livros emprestados no momento.")
