tabuleiro = [[" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "]]
tabuleiro[3][3] = "X"
tabuleiro[4][4] = "X"
tabuleiro[3][4] = "O"
tabuleiro[4][3] = "O"

def imprimir(tab):
    for i in range (0,7):
        for j in range (0,8):
            if (tab[i][j] == " " and j != 7):
                print("___|", end="")
            elif (tab[i][j] == " " and j == 7):
                print("___")
            elif (tab[i][j] == "X" and j != 7):
                print("_X_|", end="")
            elif (tab[i][j] == "X" and j == 7):
                print("_X_")
            elif (tab[i][j] == "O" and j != 7):
                print("_O_|", end="")
            elif (tab[i][j] == "O" and j == 7):
                print("_O_")
                
    for j in range (0,8):
        if (tab[7][j] == " " and j != 7):
            print("   |", end="")
        elif (tab[7][j] == " " and j == 7):
            print("   ")
        elif (tab[7][j] == "X" and j != 7):
            print(" X |", end="")
        elif (tab[7][j] == "X" and j == 7):
            print(" X ")
        elif (tab[7][j] == "O" and j != 7):
            print(" O |", end="")
        elif (tab[7][j] == "O" and j == 7):
            print(" O ")

def jogar(letra):
    print(letra + ": Em qual casa você quer jogar?")
    coluna = int(input("Coluna: ")) - 1 # porque quando o jogador diz [1,1] na verdade é o índice [0,0]
    linha = int(input("Linha: ")) - 1
    
    while tabuleiro[linha][coluna] != " ":
        print("Casa inválida, já há uma peça nessa posição. Jogue novamente.")
        coluna = int(input("Coluna: ")) - 1
        linha = int(input("Linha: ")) - 1
    
    # depois que o jogador escolheu a posição da nova peça, vamos checar se essa posição é válida varrendo sua coluna, linha e diagonais
    # for j in range(0,8):
    #     if tabuleiro[linha][j] != " " and tabuleiro[linha][j] != letra:
                
    tabuleiro[linha][coluna] = letra
    imprimir(tabuleiro)
done = False
imprimir(tabuleiro)
print("Bem vindos ao Othello. O jogador \"X\" começa.")
while done == False:
   jogar("X")
   jogar("O")