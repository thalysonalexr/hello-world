import time
import os
import platform
import ctypes, sys
import random


def limpar_tela(sistema):
    return 'cls' if sistema is 'Windows' else 'clear'

SISTEMA = platform.system()
COMANDO = limpar_tela(SISTEMA)
FRASE = 'Olá mundo!'

ANSI = ['\033[31m', '\033[32m',
        '\033[34m', '\033[36m',
        '\033[35m', '\033[33m']


def printColorizedInLinux(text, color):
    print(text, ANSI[color]+'\033[0;0m')


def printColorizedInWindows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)


def executa_x(frase, y, direita=True, MAX=60):
    x = 0 if direita else MAX
    while True:
        if SISTEMA is 'Windows':
            printColorizedInWindows('\n' * y + ' ' * x + frase, [random.randint(1, 15)])
        else:
            printColorizedInLinux('\n' * y + ' ' * x + frase, random.randint(1, len(ANSI)))
        time.sleep(0.1)
        os.system(COMANDO)
        if direita:
            x += 1
        else:
            x -= 1
        if x == MAX or x == 0: return


def executa_y(MAX=5):
    y = 0
    while True:
        y += 1
        executa_x(FRASE, y)
        y += 1
        executa_x(FRASE, y, False)

if __name__ == '__main__':
    while True:
        executa_y(6)