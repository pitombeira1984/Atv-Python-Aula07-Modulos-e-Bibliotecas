from Somar import(Somar)
from Subtrair import(Subtrair)
from Dividir import(Dividir)
from Multiplicar import(Multiplicar)

def Calculadora():
    while True:
        print("Calculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Divisão")
        print("4 - Multiplicação")
        print("0 - Sair")
        operacao = int(input("Escolha uma opção: "))
        if operacao == 1:
            Num1 = int(input("Digite o primeiro número: "))
            Num2 = int(input("Digite o segundo número: "))
            resultado = Somar(Num1, Num2)
            print(resultado)
        elif operacao == 2:
            Num1 = int(input("Digite o primeiro número: "))
            Num2 = int(input("Digite o segundo número: "))
            resultado = Subtrair(Num1, Num2)
            print(resultado)
        elif operacao == 3:
            Num1 = int(input("Digite o primeiro número: "))
            Num2 = int(input("Digite o segundo número: "))
            resultado = Dividir(Num1, Num2)
            print(resultado)
        elif operacao == 4:
            Num1 = int(input("Digite o primeiro número: "))
            Num2 = int(input("Digite o segundo número: "))
            resultado = Multiplicar(Num1, Num2)
            print(resultado)
        elif operacao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida")        
Calculadora()