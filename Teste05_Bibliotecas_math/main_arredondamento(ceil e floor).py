import math

def Arredondamento():
    num = float(input("Digite um número: "))
    arredonda_cima = math.ceil(num)
    arredonda_baixo = math.floor(num)
    print(f"Arredondamento para cima: {arredonda_cima}")
    print(f"Arredondamento para baixo: {arredonda_baixo}")
Arredondamento()