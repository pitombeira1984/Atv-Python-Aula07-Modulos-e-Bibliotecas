def InverterString():
    string = input("Digite uma string: ")
    string_invertida = string[::-1]
    print("String invertida:", string_invertida)


def ContarPalavras():
    string = input("Digite uma string: ")
    palavras = string.split()
    print("Número de palavras:", len(palavras))    
    
def VerificarPalindromo():
    string = input("Digite uma string: ")
    string = string.replace(" ", "").lower()
    string_invertida = string[::-1]
    if string == string_invertida:
        print("A string é um palíndromo")
    else:
        print("A string não é um palíndromo")    