class No:
    def __init__(self, h, ab=None):
        self.h = h
        self.ab = ab
        self.filhos = []

no_1 = No(2)
no_2 = No(4)
no_3 = No(3)
no_4 = No(4, 4)
no_5 = No(5, 5)
no_6 = No(-2, -2)
no_7 = No(20, 20)

no_1.filhos.append(no_2)
no_1.filhos.append(no_3)
no_2.filhos.append(no_4)
no_2.filhos.append(no_5)
no_3.filhos.append(no_6)
no_3.filhos.append(no_7)

# max                          no_1 (2)
# min         no_2 (4)               no_3 (3)
# max   no_4 (4)  no_5 (5)     no_6 (-2)  no_7 (20)

# PENSAR EM COMO FAZER QUANDO ACABA O JOGO (TARGETDEPTH FICA SENDO MENOR PORQUE PARA ANTES)
def minimaxno (curDepth, no_atual, maxTurn, targetDepth):
     
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return [no_atual, no_atual.ab]
     
    if (maxTurn == True):
        h_max = -10000
        for filho in no_atual.filhos:
    
            if (minimaxno(curDepth + 1, filho, False, targetDepth)[1] >= h_max):
                h_max = minimaxno(curDepth + 1, filho, False, targetDepth)[1]
                filho_max = filho

        no_atual.ab = h_max
        return [filho, h_max]
     
    else:
        h_min = 10000
        for filho in no_atual.filhos:
            if (minimaxno(curDepth + 1, filho, False, targetDepth)[1] <= h_min):
                h_min = minimaxno(curDepth + 1, filho, False, targetDepth)[1]

        no_atual.ab = h_min
        return [filho, h_min]

treeDepth = 2

print("The optimal value is : ", end = "")
print(minimaxno(0, no_1, True, treeDepth)[1])

def minimax (curDepth, nodeIndex, maxTurn, scores, targetDepth):
     
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]
     
    if (maxTurn == True):
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
        
def escolha(self, board, moves):
        h = self.choose_h(board)
        no_raiz = No(None, h)
        retMove = None

        print("\nScore atual:", board.score(), "\n")
        for i in range(len(moves)):
    
            print("Move atual:", moves[i].x, moves[i].y)
            new_board = board.get_clone()
            new_board.play(moves[i], self.color)
            
            h = self.choose_h(board)
            no_atual = No(moves[i], h, None)
            
            self.escolha(new_board, new_board.valid_moves(self.color))
            
            print("h:", h, "\n")
            if h > maiorH:
                maiorH = h
                retMove = moves[i]
                print("Melhor jogada ate agora: [" + str(moves[i].x) + ", " + str(moves[i].y) + "]\n" + "h = " + str(h) + "\n")
            
            if i == len(moves) - 1:
                ultimo_pai = no_atual

        return retMove
     
# Driver code
# scores = [3, 5, 2, 9, 12, 5, 23, 23]
 
# treeDepth = math.ceil(math.log(len(scores), 2))
 
# print("The optimal value is : ", end = "")
# print(minimax(0, 0, True, scores, treeDepth))
 
# This code is contributed
# by rootshadow