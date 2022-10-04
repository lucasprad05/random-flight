#Random Flight Route Ideas
#by Lucas Prado

import random

def randomRoute(list):
    N = len(list) - 1
    apt1 = random.randint(0, N)
    apt2 = random.randint(0, N)
    if list[apt1] == list[apt2]:
        return randomRoute(list)
    print('Route: ' + list[apt1] + ' - ' + list[apt2])
    op = input('Do you wanna sort again? (y/n): ')
    if op == 'y' or op == 'Y':
        randomRoute(list)

def main():  
    list = []
    j = 0
    while j == 0:
        x = input('Type an ICAO airport or "e" to exit: ')
        if x != 'e' and x != 'E':
            list.append(x)
        else:
            j = 1
    randomRoute(list)

main()
