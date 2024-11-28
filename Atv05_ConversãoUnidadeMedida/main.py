from ConversaoUnidadeMedida import ConversaoUnidadeMedida
def main():
    Conversao = ConversaoUnidadeMedida()
    while True:
        print("Conversão de Unidades de Medida")
        print("1 - Metros para Pés")
        print("2 - Quilogramas para Libras")
        print("3 - Celsius para Fahrenheit")
        print("0 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            Conversao.MetrosParaPes()
        elif opcao == 2:
            Conversao.QuilogramasParaLibras()
        elif opcao == 3:
            Conversao.CelsiusParaFahrenheit()
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida")
main()