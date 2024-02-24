# Primeira questão
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

media = (numero1 + numero2 + numero3) / 3
print ("a média dos três números é: ", media)

# Segunda questão
numero = int(input("Digite o seu número: "))
if  numero % 2 == 0:
    print ("O número é par")
else:
    print ("O número é impar")
    

# Terceira questão
    numero = int(input("Insira um número: "))

print("Números pares até", numero, ":")
for i in range(numero+1):
    if i % 2 == 0:
        print(i)

# Quarta questão
numeros = input("Digite uma lista de números separados por espaço: ")

numeros = [int(x) for x in numeros.split()]

if numeros:
    maior = max(numeros)
    menor = min(numeros)

    print("O maior valor na lista é:", maior)
    print("O menor valor na lista é:", menor)

else:
    print("A lista está vazia.")

# Quinta questão
numero = input("Digite uma lista de números: ")

numeros = [int(x) for x in numeros.split('')]
soma_pares = 0
contage,_pares = 0

if numeros:
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares += numero
            contagem_pares += 1

if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
    print("A média dos números apres é: ", media_pares)
    
else:
    print ("Não há números pares na lsita.")

else:
print("Lista vazia.")

# Sexta questão
numero = int(input("Digite um número inteiro positivo: "))
if  numero < 0:
    print("Você digitou um número positivo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
print("O fatorial de", numero, "é:", fatorial)

# Sétima questão
limite = int(input("por favor, digite o seu número: "))
if limite <= 0:
    print("por favor , digite um número maior que zero")
else:
    fibonacci = [0, 1]
    while fibonacci[-1] <= limite:
        proximo = fibonacci[-1] + fibonacci[-2]
        if proximo <= limite:
            fibonacci.append(proximo)
        else:
            break

print("Sequência de Fibonacci até", limite, ":")
for numero in fibonacci:
    print(numero, end=" ")

# Oitava questão
def eh_primo(numero):
    if numero <= 1:
        for i in range(2, int(numero**0.5) +1):
            if numero % i == 0:
                return False
            return True
numero = int(input("Digite um numero: "))
if eh_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo")

# Nona questão
nomes = input("Digite aqui a lista de nomes: ")
lista_de_nomes = nomes.split()
nomes_com_a = []

for nome in lista_de_nomes:
    if nome.lower().startswith('a'):
        nomes_com_a.append(nome)

print("Nomes que começam com a letra 'A': ", nomes_com_a)

# Décima questão
import random
def jogo_pedra_papel_tesoura(jogada_usuário):
    jogadas = ['pedra', 'papel', 'tesoura']
    jogada_maquina = random.choice(jogadas)

    print("Você jogou:", jogada_usuário)
    print("Maquina jogou:", jogada_maquina)
    
    if jogada_usuário == jogada_maquina:
        return "Empate!"
    elif (jogada_usuário == 'pedra' and jogada_maquina == 'tesoura') or\
        (jogada_usuário == 'papel'and jogada_maquina == 'pedra') or \
        (jogada_usuário=='tesoura' and jogada_maquina=='papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"
    
jogada_usuário = input("Escolha sua jogada (pedra, papel ou tesoura).").lower()
if jogada_usuário in ['pedra', 'papel', 'tesoura']:
    resultado = jogo_pedra_papel_tesoura(jogada_usuário)
    print("resultado")
 else:
    print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")