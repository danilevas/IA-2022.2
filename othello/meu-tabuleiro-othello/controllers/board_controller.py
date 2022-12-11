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
        self.tempos = [0.0, 0.0]
        self.tempos_medios = [0.0, 0.0]
        self.vitorias = [0, 0, 0]
        
        self.overs3 = [0, 0]
        self.overs5 = [0, 0]
        self.overs7 = [0, 0]
        self.overs10 = [0, 0]
        
    def fake_init(self):
        self.board = Board(None)
        self.view = ConsoleBoardView(self.board)
        self.tempos = [0.0, 0.0]
        self.tempos_medios = [0.0, 0.0]
        
        self.overs3 = [0, 0]
        self.overs5 = [0, 0]
        self.overs7 = [0, 0]
        self.overs10 = [0, 0]

    def init_game(self):

        self.white_player = self._select_player(Board.WHITE)
        self.black_player = self._select_player(Board.BLACK)
        vezes = int(input("Quantas vezes você quer rodar o jogo? "))

        for vzs in range(vezes):
            if vzs > 0:
                self.fake_init() # reinicia o tabuleiro
            
            self.atual_player = self.black_player

            finish_game = 0
            jogadas = [0, 0]

            # self.view.update_view()

            while finish_game != 2:
                # input("")
                atual_color = self.atual_player.color
                # print('Jogador: ' + atual_color)
                start = time.time() * 1000

                if self.board.valid_moves(atual_color).__len__() > 0:
                    self.board.play(self.atual_player.play(self.board.get_clone()), atual_color)
                    # self.view.update_view()
                    finish_game = 0
                    
                    tempo_jogada = (time.time() * 1000) - start
                    if self.atual_player == self.white_player:
                        self.tempos[0] += tempo_jogada
                        jogadas[0] += 1
                        if tempo_jogada >= 3000.0:
                            self.overs3[0] += 1
                    else:
                        self.tempos[1] += tempo_jogada
                        jogadas[1] += 1
                        if tempo_jogada >= 10000.0:
                            self.overs10[1] += 1
                        elif tempo_jogada >= 7000.0:
                            self.overs7[1] += 1
                        elif tempo_jogada >= 5000.0:
                            self.overs5[1] += 1
                        elif tempo_jogada >= 3000.0:
                            self.overs3[1] += 1
                    # print(f"Tempo de jogada: {str(tempo_jogada)} ms.\n")
                else:
                    # print('Sem movimentos para o jogador: ' + atual_color)
                    finish_game += 1
                self.atual_player = self._opponent(self.atual_player)

                # time.sleep(0.7)

            self.tempos_medios[0] = self.tempos[0]/jogadas[0]
            self.tempos_medios[1] = self.tempos[1]/jogadas[1]
            
            print("\n[JOGO " + str(vzs + 1) + "/" + str(vezes) + "]")
            self._end_game()
        print("\nJogador " + self.white_player.__class__.__name__ +
                  " BRANCO " + '(' + Board.WHITE + ") ganhou " + str(self.vitorias[0]) + " jogos")
        print("Jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + ") ganhou " + str(self.vitorias[1]) + " jogos")
        print("Ocorreram " + str(self.vitorias[2]) + " empates")

    def _end_game(self):
        score = self.board.score()
        if score[0] > score[1]:
            self.vitorias[0] += 1
            print('Jogador ' + self.white_player.__class__.__name__ +
                  ' BRANCO ' + '('+Board.WHITE+') Ganhou\n')
        elif score[0] < score[1]:
            self.vitorias[1] += 1
            print('Jogador ' + self.black_player.__class__.__name__ +
                  ' PRETO ' + '('+Board.BLACK+') Ganhou\n')
        else:
            self.vitorias[2] += 1
            print('Jogo terminou empatado\n')
        
        print("Tempo total do jogador " + self.white_player.__class__.__name__ +
                  " BRANCO " + '(' + Board.WHITE + "): " + str(self.tempos[0]) + " ms")
        print("Tempo médio do jogador " + self.white_player.__class__.__name__ +
                  " BRANCO " + '(' + Board.WHITE + "): " + str(self.tempos_medios[0]) + " ms")
        print("Jogadas acima de 3 segundos do jogador " + self.white_player.__class__.__name__ +
                  " BRANCO " + '(' + Board.WHITE + "): " + str(self.overs3[0]) + " jogadas\n")
        
        print("Tempo total do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.tempos[1]) + " ms")
        print("Tempo médio do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.tempos_medios[1]) + " ms\n")
        
        print("Jogadas entre 3 e 5 segundos do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.overs3[1]) + " jogadas")
        print("Jogadas entre 5 e 7 segundos do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.overs5[1]) + " jogadas")
        print("Jogadas entre 7 e 10 segundos do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.overs7[1]) + " jogadas")
        print("Jogadas acima de 10 segundos do jogador " + self.black_player.__class__.__name__ +
                  " PRETO " + '(' + Board.BLACK + "): " + str(self.overs10[1]) + " jogadas")

    def _opponent(self, player):
        if player.color == Board.WHITE:
            return self.black_player

        return self.white_player

    def _select_player(self, color):
        players = glob.glob('C:/Programas/IA/othello/meu-tabuleiro-othello/models/players/*_player.py')
        if color == Board.WHITE:
            name = 'BRANCO'
        else:
            name = 'PRETO'
        while True:
            print('\nSelecione um dos players abaixo para ser o jogador {} ({})'.format(name, color))

            for idx, player in enumerate(players):
                print(idx.__str__() + " - " + player.split('\\')[-1].split('/')[-1])
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