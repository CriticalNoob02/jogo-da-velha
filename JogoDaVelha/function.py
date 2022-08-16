## Declarando as Variavéis;
import re


li = [
    [" ","X","O"],
    [" ","X","O"],
    [" ","X","O"]
]

a = 0
b = 0 
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

## Funções do Jogo

# Tabela
def jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i):
    print(f"    1   2   3  ")
    print(f"A   {li[0][a]} | {li[0][b]} | {li[0][c]}  ")
    print(f"   ---|---|--- ")
    print(f"B   {li[1][d]} | {li[1][e]} | {li[1][f]}  ")
    print(f"   ---|---|--- ")
    print(f"C   {li[2][g]} | {li[2][h]} | {li[2][i]}  ")

# Jogada "X"
def jogadorX(JogadaX):
    ## Chamando as Variaveis;
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i


    ## Possibiliadades;
    if(JogadaX == "A1"):
        if(a == 0):
            a = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "A2"):
        if(b == 0):
            b = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "A3"):
        if(c == 0):
            c = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "B1"):
        if(d == 0):
            d = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "B2"):
        if(e == 0):
            e = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "B3"):
        if(f == 0):
            f = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "C1"):
        if(g == 0):
            g = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0 
            return erro               
    elif(JogadaX == "C2"):
        if(h == 0):
            h = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaX == "C3"):
        if(i == 0):
            i = 1
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    else:
        print("Jogada Invalida! Tente novamente.")
        erro = 0
        return erro

    ## Vitória por Coluna;
    if(a == 1 and d == 1 and g == 1 or b == 1 and e == 1 and h == 1 or c == 1 and f == 1 and i == 1):
        print("Parece que o 'X' ganhou!")
        erro = 5
        return erro

    ## Vitória por Linha;  
    elif(a == 1 and b == 1 and c == 1 or d == 1 and e == 1 and f == 1 or g == 1 and h == 1 and i == 1):
        print("Parece que o 'X' ganhou!")
        erro = 5
        return erro

    ## Vitória na Diagonal;
    elif(a == 1 and e == 1 and i == 1 or c == 1 and e == 1 and g == 1):
        print("Parece que o 'X' ganhou!")
        erro = 5
        return erro
  
# Jogada "O"
def jogadorO(JogadaO):
    ## Chamando as Variaveis;
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i


    ## Possibiliadades;
    if(JogadaO  == "A1"):
        if(a == 0):
            a = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "A2"):
        if(b == 0):
            b = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "A3"):
        if(c == 0):
            c = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "B1"):
        if(d == 0):
            d = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "B2"):
        if(e == 0):
            e = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "B3"):
        if(f == 0):
            f = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "C1"):
        if(g == 0):
            g = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "C2"):
        if(h == 0):
            h = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    elif(JogadaO  == "C3"):
        if(i == 0):
            i = 2
            jogo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i)
        else:
            print("Jogada Invalida! Tente novamente.")
            erro = 0
            return erro
    else:
        print("Jogada Invalida! Tente novamente.")
        erro = 0
        return erro

    ## Vitória por Coluna;
    if(a == 2 and d == 2 and g == 2 or b == 2 and e == 2 and h == 2 or c == 2 and f == 2 and i == 2):
        print(f"Parece que o 'O' ganhou!")
        erro = 5
        return erro
        
    ## Vitória por Linha;  
    elif(a == 2 and b == 2 and c == 2 or d == 2 and e == 2 and f == 2 or g == 2 and h == 2 and i == 2):
        print(f"Parece que o 'O' ganhou!")
        erro = 5
        return erro

    ## Vitória na Diagonal;
    elif(a == 2 and e == 2 and i == 2 or c == 2 and e == 2 and g == 2):
        print(f"Parece que o 'O' ganhou!")       
        erro = 5
        return erro
   