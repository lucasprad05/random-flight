#Random Flight Route Ideas
#by Lucas Prado

import random

def randomRoute(list):
    N = len(list) - 1
    apt1 = random.randint(0, N)
    apt2 = random.randint(0, N)
    if apt1 == apt2:
        return randomRoute(list)
    print('Rota: ' + list[apt1] + ' - ' + list[apt2])
    op = input('Deseja resortear a rota? (s/n): ')
    if op == 's' or op == 'S':
        randomRoute(list)

def main():  
    list = []
    j = 0
    while j == 0:
        x = input('Digite um aeroporto ou digite "e" para sair: ')
        if x != 'e' and x != 'E':
            list.append(x)
        else:
            j = 1
    randomRoute(list)

main()