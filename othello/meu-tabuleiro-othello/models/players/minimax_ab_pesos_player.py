from models.board import Board
from models.move import Move

glob = 0

class No:
    def __init__(self, move, h, ab=None):
        self.move = move
        self.h = h
        self.ab = ab
        self.filhos = []

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
    
    def choose_hscore(self, board):
        if self.color == Board.WHITE:
            h = board.score()[0] - board.score()[1]
        else:
            h = board.score()[1] - board.score()[0]
        return h
    
    def show_pesos(self):
        pesos = []
        for i in range(0, 10):
            pesos.insert(i, [1]*10)

        for i in range(1, 9):
            for j in range(1, 9):
                move = Move(i, j)
                pesos[i][j] = self.choose_hpeso(move)
        
        print(pesos)
    
    def choose_hpeso(self, move):
        peso = 0
        
        # pensar em colocar não só a casa que você escolhe (move) no peso, mas também as que você conquista no caminho
        
        # cantos
        if (move.x == 1 or move.x == 8) and (move.y == 1 or move.y == 8):
            peso = 1.5
        
        # paredes
        elif (move.x == 1 or move.x == 8) or (move.y == 1 or move.y == 8):
            peso = 0.5
        
        # meiuca (2x2)
        elif (move.x == 4 or move.x == 5) or (move.y == 4 or move.y == 5):
            peso = 1
        
        return peso
    
    def minimaxno2 (self, board, moves, profund_atual, no_atual, alfa, beta, vez_max, profund_alvo):
        
        self.itera += 1
        
        # caso base : profund_alvo atingida
        if (profund_atual == profund_alvo):
            h = self.choose_hscore(board)
            no_atual.ab = h
            return no_atual
        
        if (vez_max == True):
            ab_max = -10000
            for move in moves:
                new_board = board.get_clone()
                new_board.play(move, self.color)
                h = self.choose_hscore(board) + self.choose_hpeso(move)
                
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
                h = self.choose_hscore(board) + self.choose_hpeso(move)
                
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
        h = self.choose_hscore(board)
        no_raiz = No(None, h)
        # print ("Iteracao", self.itera)
        return self.minimaxno2(board, moves, 0, no_raiz, -1000, 1000, True, 4).move