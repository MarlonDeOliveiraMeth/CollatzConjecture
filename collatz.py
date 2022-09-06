# Função que realiza os cálculos necessários no estudo da Conjectura de Collatz.
def collatz(n, values):
    calculations = 0
    print(n)
    while n != 1:
        if n%2 == 0:
            n = n/2
        elif n%2 == 1:
            n = 3*n+1
        values.append(n)
        calculations += 1
        if n == 1:
            print(values)
            print("Resultado de acordo com a conjectura após", calculations, "cálculos!\n")
            break

# No código abaixo, é apresentado ao usuário duas alternativas para análise da Conjectura.
while True:
    askoption = int(input("De qual forma você gostaria de testar a Conjectura de Collatz?\nDigite 1 para iniciar um teste manual.\nDigite 2 para iniciar um teste automático. CUIDADO! O programa entrará em um loop que testará todos números possíveis!\n"))
    if askoption == 1:
        n = int(input("\nInsira um número inteiro que não seja igual ou menor que zero: "))
        if n > 0:
            values = []
            collatz(n, values)
        else:
            print("\nPor favor, insira um número inteiro que não seja igual ou menor que zero.\n")
    elif askoption == 2:
        n = 1
        while True:
            values = []
            collatz(n, values)
            n += 1
    else:
        print("\nPor favor, insira uma opção válida.\n")