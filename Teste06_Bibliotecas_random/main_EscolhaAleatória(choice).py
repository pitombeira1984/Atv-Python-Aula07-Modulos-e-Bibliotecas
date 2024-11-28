import random

def EscolhaAleatoria():
    lista = ["maça", "banana", "laranja", "morango", "uva"]
    escolha_aleatoria = random.choice(lista)
    print(f"A escolha aleatoria foi: {escolha_aleatoria}")
EscolhaAleatoria()