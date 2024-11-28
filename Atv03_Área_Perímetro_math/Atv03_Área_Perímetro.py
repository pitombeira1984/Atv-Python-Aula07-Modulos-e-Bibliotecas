from math import pi

def CalculoAreaPerimetro():
    while True:
        print("Escolha uma opção:")
        print("1. Calcular Área e Perímetro do círculo")
        print("2. Calcular Área e Perímetro do retângulo")
        print("3. Calcular Área e Perímetro do quadrado")
        print("0 . Sair")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            raio = float(input("Digite o raio do círculo: "))
            area = pi * raio ** 2
            perimetro = 2 * pi * raio
            print(f"Área do círculo: {area:.2f}")
            print(f"Perímetro do círculo: {perimetro:.2f}")
        elif opcao == "2":
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            area = base * altura
            perimetro = 2 * (base + altura)
            print(f"Área do retângulo: {area:.2f}")
            print(f"Perímetro do retângulo: {perimetro:.2f}")
        elif opcao == "3":
            lado = float(input("Digite o lado do quadrado: "))
            area = lado ** 2
            perimetro = 4 * lado
            print(f"Área do quadrado: {area:.2f}")
            print(f"Perímetro do quadrado: {perimetro:.2f}")
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
CalculoAreaPerimetro()