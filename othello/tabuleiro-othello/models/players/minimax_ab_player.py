from models.board import Board
import math

glob = 0

class No:
    def __init__(self, move, h, ab=None):
        self.move = move
        self.h = h
        self.ab = ab
        self.filhos = []

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
        return [filho_max, h_max]
     
    else:
        h_min = 10000
        for filho in no_atual.filhos:
            if (minimaxno(curDepth + 1, filho, False, targetDepth)[1] <= h_min):
                h_min = minimaxno(curDepth + 1, filho, False, targetDepth)[1]
                filho_min = filho

        no_atual.ab = h_min
        return [filho_min, h_min]

class MiniMaxAlfaBetaPlayer:
    def __init__(self, color, glob=0):
        self.color = color
        self.glob = glob

    def play(self, board):
        return self.escolha2(board, board.valid_moves(self.color))

    def opponent(self, color):
        if color == Board.WHITE:
            return Board.BLACK
        return Board.WHITE
    
    def choose_h(self, board):
        if self.color == Board.WHITE:
            h = board.score()[0] - board.score()[1]
        else:
            h = board.score()[1] - board.score()[0]
        return h
    
    def minimaxno2 (self, board, moves, curDepth, no_atual, alfa, beta, maxTurn, targetDepth):
        
        self.glob += 1
        
        # base case : targetDepth reached
        if (curDepth == targetDepth):
            h = self.choose_h(board)
            no_atual.ab = h
            return no_atual
        
        if (maxTurn == True):
            ab_max = -10000
            for move in moves:
                new_board = board.get_clone()
                new_board.play(move, self.color)
                h = self.choose_h(board)
                
                filho = No(move, h)
                ab = self.minimaxno2(board, moves, curDepth + 1, filho, alfa, beta, False, targetDepth).ab
                filho.ab = ab
                no_atual.filhos.append(filho)
                
                if (ab >= ab_max):
                    ab_max = ab
                    filho_max = filho
                
                alfa = max(alfa, ab)
                if beta <= alfa:
                    break

            no_atual.ab = ab_max
            return filho_max
        
        else:
            ab_min = 10000
            for move in moves:
                new_board = board.get_clone()
                new_board.play(move, self.color)
                h = self.choose_h(board)
                
                filho = No(move, h)
                ab = self.minimaxno2(board, moves, curDepth + 1, filho, alfa, beta, False, targetDepth).ab
                filho.ab = ab
                no_atual.filhos.append(filho)
                
                if (ab <= ab_min):
                    ab_min = ab
                    filho_min = filho
                    
                beta = min(beta, ab)
                if beta <= alfa:
                    break

            no_atual.ab = ab_min
            return filho_min
    
    def escolha2(self, board, moves):
        h = self.choose_h(board)
        no_raiz = No(None, h)
        print ("Iteracao", self.glob)
        return self.minimaxno2(board, moves, 0, no_raiz, -1000, 1000, True, 5).move
    
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