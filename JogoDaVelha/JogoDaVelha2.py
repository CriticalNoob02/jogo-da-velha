## Importando a Parte Feia dos Codigos;
from function import jogo, jogadorX, jogadorO

## Declarando Variavéis
erro = 0
nome1 = input("Digite o nome do PRIMEIRO Jogador: ")
nome2 = input("Digite o nome do SEGUNDO Jogador: ")
jogo()

## Ciclo da Partida:
while erro != 5:

    erro = 0
    while erro == 0:
        erro = 1
        JogadaX = input(f"{nome1} Digite a coordenada da jogada: ")
        JogadaX = JogadaX.strip().upper()
        erro = jogadorX(JogadaX)
        
    ## Verifição de vitória;
    if( erro == 5):
        print("Fim de Jogo!")
        break
        
    erro = 0
    while erro == 0:
        erro = 1
        JogadaO = input(f"{nome2} Digite a coordenada da jogada: ")
        JogadaO = JogadaO.strip().upper()
        erro = jogadorO(JogadaO)

    ## Verifição de vitória;
    if( erro == 5):
        print("Fim de Jogo!")
        break