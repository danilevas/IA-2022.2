from models.board import Board

class ComilaoV2Player:
    def __init__(self, color):
        self.color = color

    def play(self, board):
        return self.escolha(board, board.valid_moves(self.color))

    def escolha(self, board, moves):
        maiorComidas = 0
        retMove = None
        score_atual = board.score()
        # info_moves = []
        print("\nScore atual: ", board.score(), "\n")
        for i in range(len(moves)):
            if moves[i].x == 1 or moves[i].y == 1 or moves[i].x == 8 or moves[i].y == 8:
                print("Move atual (parede):", moves[i].x, moves[i].y)
            else:
                print("Move atual:", moves[i].x, moves[i].y)
            new_board = board.get_clone()
            new_board.play(moves[i], self.color)
            if self.color == Board.WHITE:
                comidas = (new_board.score()[0] - score_atual[0]) - 1
            else:
                comidas = (new_board.score()[1] - score_atual[1]) - 1
            print("Comidas no move:", comidas, "\n")
            if comidas > maiorComidas:
                maiorComidas = comidas
                retMove = moves[i]
                print("Melhor jogada ate agora: [" + str(moves[i].x) + ", " + str(moves[i].y) + "]\n" + str(comidas) + " pecas comidas\n")
            elif comidas == maiorComidas:
                if moves[i].x == 1 or moves[i].y == 1 or moves[i].x == 8 or moves[i].y == 8:
                    maiorComidas = comidas
                    retMove = moves[i]
                    print("Melhor jogada ate agora (parede): [" + str(moves[i].x) + ", " + str(moves[i].y) + "]\n" + str(comidas) + " pecas comidas\n")

        return retMove