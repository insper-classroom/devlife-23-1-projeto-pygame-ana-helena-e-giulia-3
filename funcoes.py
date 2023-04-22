import pygame
import classes

pygame.init()
pygame.display.set_caption("Hogwarts Scape")
window = pygame.display.set_mode((1280, 720))

FPS = 60
VEL_JOGADOR = 5

def gera_fundo():
    altura = 144
    largura = 144
    fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (largura, altura))
    tiles = []

    for i in range(1280 // largura + 1):
        for j in range(720 // altura + 1):
            pos = (i * largura, j * altura)
            tiles.append(pos)

    return tiles, fundo


def flip(sprite):
    return [pygame.transform.flip(sprite, True, False)]


def carrega_sprite(largura, altura, direcao = False):
    todas_sprites = {}
    sprites = []
    sprite = pygame.image.load('imagens/harry_lado.png').convert_alpha()
    
    surface = pygame.Surface((largura, altura), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, largura, altura)
    surface.blit(sprite, (0, 0), rect)
    sprites.append(surface)

    if direcao:
        todas_sprites['harry_lado'.replace('.png', '') + '_direita'] = sprite
        todas_sprites['harry_lado'.replace('.png', '') + '_esquerda'] = flip(sprite)
    else: 
        todas_sprites['harry_lado'.replace('.png', '')] = sprite
    
    return todas_sprites
               

def desenha(window, background, bg_image, harry):
    for tile in background:
        window.blit(bg_image, tile)

    harry.desenha(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = gera_fundo()
    harry = classes.Personagens(100, 100, 50, 50)

    jogo = True
    while jogo: 
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                jogo = False
                break 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    harry.movimenta_esquerda(VEL_JOGADOR)
                if event.key == pygame.K_RIGHT: 
                    harry.movimenta_direita(VEL_JOGADOR)
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    harry.movimenta_esquerda(0)
                if event.key == pygame.K_RIGHT:
                    harry.movimenta_direita(0) 
            
        harry.loop(FPS)
        desenha(window, background, bg_image, harry)

if __name__ == '__main__':
    main(window)
