from classesJogo.gerenciador_telas import Gerenciador_Telas
import pygame

pygame.init()
pygame.display.set_caption("Hogwarts Scape")
window = pygame.display.set_mode((1280, 720))
musica = pygame.mixer.music.load('som/musica_tema.mp3')
pygame.mixer.music.play()
tela = Gerenciador_Telas(window)
tela.game_loop() 