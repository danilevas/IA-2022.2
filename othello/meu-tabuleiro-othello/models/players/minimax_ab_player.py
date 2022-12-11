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
def minimaxno (profund_atual, no_atual, vez_max, profund_alvo):
     
    # base case : targetDepth reached
    if (profund_atual == profund_alvo):
        return [no_atual, no_atual.ab]
     
    if (vez_max == True):
        h_max = -10000
        for filho in no_atual.filhos:
            if (minimaxno(profund_atual + 1, filho, False, profund_alvo)[1] >= h_max):
                h_max = minimaxno(profund_atual + 1, filho, False, profund_alvo)[1]
                filho_max = filho

        no_atual.ab = h_max
        return [filho_max, h_max]
     
    else:
        h_min = 10000
        for filho in no_atual.filhos:
            if (minimaxno(profund_atual + 1, filho, False, profund_alvo)[1] <= h_min):
                h_min = minimaxno(profund_atual + 1, filho, False, profund_alvo)[1]
                filho_min = filho

        no_atual.ab = h_min
        return [filho_min, h_min]

class MiniMaxAlfaBetaPlayer:
    def __init__(self, color, itera = 0):
        self.color = color
        self.itera = itera

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
    
    def minimaxno2 (self, board, moves, profund_atual, no_atual, alfa, beta, vez_max, profund_alvo):
        
        self.itera += 1
        
        # caso base : profund_alvo atingida
        if (profund_atual == profund_alvo):
            h = self.choose_h(board)
            no_atual.ab = h
            return no_atual
        
        if (vez_max == True):
            ab_max = -10000
            for move in moves:
                new_board = board.get_clone()
                new_board.play(move, self.color)
                h = self.choose_h(board)
                
                filho = No(move, h)
                ab = self.minimaxno2(board, moves, profund_atual + 1, filho, alfa, beta, False, profund_alvo).ab
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
                ab = self.minimaxno2(board, moves, profund_atual + 1, filho, alfa, beta, False, profund_alvo).ab
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
        # print ("Iteracao", self.itera)
        return self.minimaxno2(board, moves, 0, no_raiz, -1000, 1000, True, 4).move