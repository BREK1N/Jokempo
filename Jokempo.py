import os
from time import sleep
from random import randint
score = 0
while True:
    #  menu
    compvar = randint(1, 3)
    print("=" * 21)
    print(" " * 7, "Jokempo")
    print("=" * 21)
    print("[1] Pedra\n[2] Papel\n[3] Tesoura\n[4] Sair")
    print("=" * 21)
    #  Opção e limpar tela
    opc = int(input("Sua Opção: "))
    os.system("cls")
    #  Opção de empate "Pedra"
    if opc == 1 and compvar == 1:
        print("=" * 21)
        print("Sua jogada foi Pedra, A da computador foi Pedra")
        print("\033[33mEmpate\033[m")
        print(f"Score: {score}")
        print("=" * 21)
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opcão de derrota "Pedra"
    elif opc == 1 and compvar == 2:
        print("=" * 21)
        print("Sua jogada foi Pedra, A da computador foi Papel")
        print("\033[31mDerrota\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção de vitoria "Pedra"
    elif opc == 1 and compvar == 3:
        score += 1
        print("=" * 21)
        print("Sua jogada foi Pedra, A da computador foi Tesoura")
        print("\033[34mvitoria\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção de vitoria "Papel"
    elif opc == 2 and compvar == 1:
        score += 1
        print("=" * 21)
        print("Sua jogada foi Papel, A da computador foi Pedra")
        print("\033[34mvitoria\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção de Empate "Papel"
    elif opc == 2 and compvar == 2:
        print("=" * 21)
        print("Sua jogada foi Papel, A da computador foi Papel")
        print("\033[33mEmpate\033[m")
        print(f"Score: {score}")
        print("=" * 21)
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opcão de derrota "Papel"
    elif opc == 2 and compvar == 3:
        print("=" * 21)
        print("Sua jogada foi Papel, A da computador foi Tesoura")
        print("\033[31mDerrota\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção derrota "tesoura
    elif opc == 3 and compvar == 1:
        print("=" * 21)
        print("Sua jogada foi Tesoura, A da computador foi Pedra")
        print("\033[31mDerrota\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção de vitoria "Tesoura"
    elif opc == 3 and compvar == 2:
        score += 1
        print("=" * 21)
        print("Sua jogada foi Tesoura, A da computador foi Papel")
        print("\033[34mvitoria\033[m")
        print("=" * 21)
        print(f"Score: {score}")
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção de empate "Tesoura"
    elif opc == 3 and compvar == 3:
        print("=" * 21)
        print("Sua jogada foi Tesoura, A da computador foi Tesoura")
        print("\033[33mEmpate\033[m")
        print(f"Score: {score}")
        print("=" * 21)
        sleep(1)
        input("Aperte Enter para continuar...")
        os.system("cls")
    #  Opção De Sair do Programa
    elif opc == 4:
        exit()
