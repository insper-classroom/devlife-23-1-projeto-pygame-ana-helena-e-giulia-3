# Classe que irá gerenciar as telas do jogo
from .tela_inicial import Tela_inicial
from .tela_harry import Tela_harry
from .tela_instrucoes import Tela_instrucoes
from .tela_jogo import Tela_jogo
from .tela_jogo2 import Tela_jogo2
from .tela_jogo3 import Tela_jogo3
from .tela_gameover import Tela_gameover
from .tela_ganhou import Tela_ganhou
import pygame

class Gerenciador_Telas():
    def __init__(self, window):
        self.window = window
        self.tela = Tela_inicial()
    
    def game_loop(self):
        jogo = True

        while jogo:
            jogo = self.tela_update()
            self.desenha()

    def tela_update(self):
        # o que vai atualizar o 'self.tela'
        proxima_tela = self.tela.atualiza_estado()
        if proxima_tela == -1:
            return False
        if proxima_tela == 'TELA_JOGO':
            self.tela = Tela_jogo()
        if proxima_tela == 'TELA_HARRY':
            self.tela = Tela_harry()
        if proxima_tela == 'TELA_INSTRUCOES':
            self.tela = Tela_instrucoes()
        if proxima_tela == 'TELA_JOGO2':
            self.tela = Tela_jogo2()
        if proxima_tela == 'TELA_GAMEOVER':
            self.tela = Tela_gameover()
        if proxima_tela == 'TELA_INICIAL':
            self.tela = Tela_inicial()
        if proxima_tela == 'TELA_JOGO3':
            self.tela == Tela_jogo3()
        if proxima_tela == 'TELA_GANHOU':
            self.tela == Tela_ganhou()
        return True

    def desenha(self):
        # irá desenhar a tela settada como 'self.tela'
        self.tela.desenha(self.window)

        pygame.display.update()