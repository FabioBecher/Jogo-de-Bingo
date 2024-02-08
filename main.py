# jogo do bingo
import random

numeros = list(range(1, 76))
ja_sorteados = []

sorteios = 10
while True:
    input('Digite "Enter" para sortear um numero ')
    numero_sorteado = random.choice(numeros)
    print(f'O numero sorteado foi', numero_sorteado)
    numeros.remove(numero_sorteado)
    ja_sorteados.append(numero_sorteado)
    print(f'** Numeros que já sairam', ja_sorteados, '**')
    sorteios -= 1
    if (sorteios == 0):
        break

