from models.players.random_player import RandomPlayer
from models.players.corner_player import CornerPlayer
from views.console_board_view import ConsoleBoardView
from models.board import Board
import time
import glob


class BoardController:
    def __init__(self):
        self.board = Board(None)
        self.view = ConsoleBoardView(self.board)

    def init_game(self):

        self.white_player = self._select_player(Board.WHITE)
        self.black_player = self._select_player(Board.BLACK)

        self.atual_player = self.black_player

        finish_game = 0

        self.view.update_view()

        while finish_game != 2:
            # input("")
            atual_color = self.atual_player.color
            print('Jogador: ' + atual_color)
            start = time.time()
            if self.board.valid_moves(atual_color).__len__() > 0:
                self.board.play(self.atual_player.play(
                    self.board.get_clone()), atual_color)
                self.view.update_view()
                finish_game = 0
            else:
                print('Sem movimentos para o jogador: ' + atual_color)
                finish_game += 1
            self.atual_player = self._opponent(self.atual_player)
            print(
                f"Tempo de jogada: {str(round(time.time() - start))} seg.\n")
            time.sleep(0.7)

        self._end_game()

    def _end_game(self):
        score = self.board.score()
        if score[0] > score[1]:
            print("")
            print('Jogador ' + self.white_player.__class__.__name__ +
                  ' BRANCO ' + '('+Board.WHITE+') Ganhou')
        elif score[0] < score[1]:
            print("")
            print('Jogador ' + self.black_player.__class__.__name__ +
                  ' PRETO ' + '('+Board.BLACK+') Ganhou')
        else:
            print("")
            print('Jogo terminou empatado')

    def _opponent(self, player):
        if player.color == Board.WHITE:
            return self.black_player

        return self.white_player

    def _select_player(self, color):
        players = glob.glob('C:/Programas/IA/othello/tabuleiro-othello/models/players/*_player.py')
        if color == Board.WHITE:
            name = 'BRANCO'
        else:
            name = 'PRETO'
        while True:
            print('\nSelecione um dos players abaixo para ser o jogador {} ({})'.format(
                name, color))

            for idx, player in enumerate(players):
                print(idx.__str__() + " - " +
                      player.split('\\')[-1].split('/')[-1])
            try:
                player = int(
                    input("\nDigite o numero do player que voce deseja: "))
            except ValueError:
                print("Escolha deve ser um inteiro")
                continue

            if 0 <= player < len(players):
                break

            print("Escolha inválida")
        print()
        module_globals = {}
        exec(open(players[int(player)]).read(), module_globals)

        return module_globals[list(module_globals.keys())[len(module_globals.keys()) - 1]](color)