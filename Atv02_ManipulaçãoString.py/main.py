from manipulacao_string import (InverterString,ContarPalavras,VerificarPalindromo)

def main():
    while True:
        print("Menu:")
        print("1 - Inverter String")
        print("2 - Contar Palavras")
        print("3 - Verificar Palíndromo")
        print("0 - Sair")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            InverterString()
        elif escolha == 2:
            ContarPalavras()
        elif escolha == 3:
            VerificarPalindromo()
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida")
main()