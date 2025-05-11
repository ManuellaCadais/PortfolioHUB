def explicacao(numero):
    print("\nExplicação:")
    if numero < 2:
        print("Números menores que 2 não são primos.")
        return
    for i in range(2, numero):
        print(f"{numero} ÷ {i} = {numero % i}")
        if numero % i == 0:
            print(f"{numero} é divisível por {i}, então não é primo.")
            return
    print(f"{numero} só é divisível por 1 e ele mesmo. É primo!")