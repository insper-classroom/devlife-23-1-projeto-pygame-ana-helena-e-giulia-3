import pygame
import classes

pygame.init()
pygame.display.set_caption("Hogwarts Scape")
window = pygame.display.set_mode((1280, 720))

FPS = 60
VEL_JOGADOR = 5

def gera_fundo():
    fundo = pygame.transform.scale(pygame.image.load('imagens/masmorra_real.jpg'), (1280,720))
    return fundo

def desenha(window, fundo, harry):
    window.blit(fundo, (0, 0))
    harry.desenha(window)
    pygame.display.update()
 
def detecta_movimento(jogador):
    chaves = pygame.key.get_pressed()
    jogador.x_vel = 0
    if chaves[pygame.K_LEFT]:
        jogador.movimenta_esquerda(VEL_JOGADOR)
    if chaves[pygame.K_RIGHT]:
        jogador.movimenta_direita(VEL_JOGADOR)

def main(window):
    clock = pygame.time.Clock()
    harry = classes.Personagens(100, 100, 50, 50)

    jogo = True
    while jogo: 
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                jogo = False
                break  
            
            harry.loop(FPS)
            detecta_movimento(harry)
            desenha(window, gera_fundo(), harry)

if __name__ == '__main__':
    main(window)
