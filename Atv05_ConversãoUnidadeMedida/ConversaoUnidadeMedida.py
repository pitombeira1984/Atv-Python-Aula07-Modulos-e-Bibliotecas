

class ConversaoUnidadeMedida:

    def MetrosParaPes():
        metros = float(input("Digite o valor em metros: "))
        pes = metros * 3.281
        print("O valor em pés é: ", pes)
        
    def QuilogramasParaLibras():
        quilogramas = float(input("Digite o valor em quilogramas: "))
        libras = quilogramas * 2.205
        print("O valor em libras é: ", libras)
        
    def CelsiusParaFahrenheit():
        celsius = float(input("Digite o valor em graus Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("O valor em graus Fahrenheit é: ", fahrenheit)
    
    