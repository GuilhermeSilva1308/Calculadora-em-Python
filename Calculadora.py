numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operação = input("Digite a operação (+, -, *, /): ")

if (operação == "+"):
    resultado = numero1 + numero2
    print("O resultado da soma é: ", (resultado))
elif (operação == "-"):
    resultado = numero1 - numero2
    print("O resultado da subtração é: ", (resultado))
elif (operação == "*"):
    resultado = numero1 * numero2
    print("O resultado da multiplicação é: ", (resultado))
elif (operação == "/"):
    if (numero2 == 0):
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
        print("O resultado da divisão é: ", (resultado))