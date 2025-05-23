def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print("Verificador de Números Primos")

numero = int(input("Digite um número: "))

if eh_primo(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo.")

from Melhorias import explicacao

# ... depois da verificação
explicacao(numero)

with open("historico.txt", "a") as arquivo:
    status = "primo" if eh_primo(numero) else "não primo"
    arquivo.write(f"{numero} é {status}\n")