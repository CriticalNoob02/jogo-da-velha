## Importando a Parte Feia dos Codigos;
from function import jogo, jogadorX, jogadorO

## Declarando Variavéis
Partida = True


## Ciclo da Partida:
while Partida:
    erro = 0
    while erro == 0:
        erro = 1
        JogadaX = input(" Digite a coordenada da jogada: ")
        JogadaX = JogadaX.strip()
        Partida = jogadorX(JogadaX)
        

    erro = 0
    while erro == 0:
        erro = 1
        JogadaO = input(" Digite a coordenada da jogada: ")
        JogadaO = JogadaO.strip()
        Partida = jogadorO(JogadaO)