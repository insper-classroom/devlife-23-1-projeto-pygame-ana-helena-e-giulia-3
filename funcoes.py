import pygame

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Hogwarts Scape")

    return window

def atualiza_estado():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False
    
    return True

def desenha(window):
    window.fill((0, 0, 0))

def game_loop(window):
    while atualiza_estado():
        desenha(window)
