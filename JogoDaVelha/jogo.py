## Importando a Parte Feia dos Codigos;
from function import jogo, jogadorX, jogadorO,Empate
import os
os.system("cls")

## Introdução;
print("\033[42m####################\033[32;40m Bem Vindo ao meu Jogo Da Velha \033[37;42m####################\033[40m")
print("")


## Declarando Variavéis
erro = 0
nome1 = input("Digite o nome do \033[34m PRIMEIRO \033[37m Jogador: ")
nome2 = input("Digite o nome do \033[33m SEGUNDO \033[37m Jogador: ")
jogo()

## Ciclo da Partida:
while erro != 5:
    erro = 0
    while erro == 0:
        erro = 1
        print("")
        JogadaX = input(f"\033[34m{nome1}\033[37m Digite a coordenada da jogada: ")
        JogadaX = JogadaX.strip().upper()
        erro = jogadorX(JogadaX)
        
    ## Verifição de vitória ou empate;
    empate = Empate()
    if( erro == 5):
        print("")
        print("\033[42m####################\033[32;40m Fim de Jogo! \033[37;42m####################\033[40m")
        break
    elif empate == True:
        print("")
        print("\033[42m####################\033[32;40m Fim de Jogo! \033[37;42m####################\033[40m")
        break
        
    erro = 0
    while erro == 0:
        erro = 1
        print("")
        JogadaO = input(f"\033[33m{nome2}\033[37m Digite a coordenada da jogada: ")
        JogadaO = JogadaO.strip().upper()
        erro = jogadorO(JogadaO)

    ## Verifição de vitória;
    if( erro == 5):
        print("")
        print("\033[42m####################\033[32;40m Fim de Jogo! \033[37;42m####################\033[40m")
        break