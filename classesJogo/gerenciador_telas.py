# Classe que irá gerenciar as telas do jogo
from .tela_inicial import Tela_inicial
from .tela_harry import Tela_harry
from .tela_instrucoes import Tela_instrucoes
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
        proxima_tela = self.tela.verifica_colisao()
        if proxima_tela == -1:
            return False
        if proxima_tela == 'TELA_JOGO':
            pass
        elif proxima_tela == 'TELA_HARRY':
            self.tela = Tela_harry()
        elif proxima_tela == 'TELA_INSTRUCOES':
            self.tela = Tela_instrucoes()
        return True

    def desenha(self):
        # irá desenhar a tela settada como 'self.tela'
        self.tela.desenha(self.window)

        pygame.display.update()
