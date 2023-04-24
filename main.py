from classesJogo.gerenciador_telas import Gerenciador_Telas
import pygame

pygame.init()
pygame.display.set_caption("Hogwarts Scape")
window = pygame.display.set_mode((1280, 720))
tela = Gerenciador_Telas(window)
tela.tela_update()
tela.desenha()
tela.game_loop() # Loop único e principal do jogo