from random import choice

def JogoAdivinha():
    print("Bem vindo ao jogo de adivinhação!")
    print("Escolha um número de 1 a 10")
    print("Você tem 3 tentativas")
    print("Boa sorte!")
    print("")

    numero = choice(range(1, 11))
    tentativas = 3

    while tentativas > 0:
        print("Tentativas restantes: ", tentativas)
        chute = int(input("Digite um número: "))
        if chute == numero:
            print("Parabéns, você acertou!")
            break
        elif chute > numero:
            print("O número é menor")
        elif chute < numero:
            print("O número é maior")
        tentativas -= 1
        print("")

    if tentativas == 0:
        print("Você perdeu!")
        print("O número era: ", numero)

    print("")
    print("Fim do jogo")
    print("")
JogoAdivinha()