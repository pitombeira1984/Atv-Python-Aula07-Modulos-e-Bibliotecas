from biblioteca import Biblioteca

def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\n--- Gerenciador de Livros de Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Listar livros disponíveis")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Verificar disponibilidade de um livro")
        print("6. Listar livros emprestados por um usuário")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            copias = int(input("Número de cópias disponíveis: "))
            biblioteca.adicionar_livro(titulo, autor, copias)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            titulo = input("Título do livro a emprestar: ")
            usuario = input("Nome do usuário: ")
            biblioteca.emprestar_livro(titulo, usuario)

        elif opcao == "4":
            titulo = input("Título do livro a devolver: ")
            usuario = input("Nome do usuário: ")
            biblioteca.devolver_livro(titulo, usuario)

        elif opcao == "5":
            titulo = input("Título do livro: ")
            biblioteca.verificar_disponibilidade(titulo)

        elif opcao == "6":
            usuario = input("Nome do usuário: ")
            biblioteca.listar_livros_emprestados(usuario)

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    menu()
