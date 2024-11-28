from math import sqrt

def RaizQuadrada():
    while True:
        try:
            num = int(input("Digite um numero: "))
            raiz_quadrada = sqrt(num)
            print(f"A Raiz Quadrada de {num} é {raiz_quadrada:.2f}")
            break
        except ValueError:
            print("Digite um numero valido")
RaizQuadrada()