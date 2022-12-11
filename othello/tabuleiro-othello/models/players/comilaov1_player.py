from models.board import Board

class ComilaoPlayer:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.escolha(board, board.valid_moves(self.color))

    def escolha(self, board, moves):
        maiorComidas = 0
        retMove = None
        score_atual = board.score()
        print("\nScore atual: ", board.score(), "\n")
        for move in moves:
            print("Move atual:", move.x, move.y)
            new_board = board.get_clone()
            new_board.play(move, self.color)
            if self.color == Board.WHITE:
                comidas = (new_board.score()[0] - score_atual[0]) - 1
            else:
                comidas = (new_board.score()[1] - score_atual[1]) - 1
            print("Comidas no move:", comidas, "\n")
            if comidas > maiorComidas:
                maiorComidas = comidas
                retMove = move
                print("Melhor jogada ate agora: [" + str(move.x) + ", " + str(move.y) + "]\n" + str(comidas) + " pecas comidas\n")

        return retMove