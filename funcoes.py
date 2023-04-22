import pygame
import classes

def inicializa():
    pygame.init()
    pygame.display.set_caption("Hogwarts Scape")
    window = pygame.display.set_mode((1280, 720))

    assets = {
        'musica_fundo': pygame.mixer.music.load('som/musica_tema.mp3')
    }
    
    state = {
        'tela_inicio': True,
        'tela_instrucoes': False,
        'tela_jogo': False
    }

    pygame.mixer.music.play()

    return window, assets, state


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


def inverte(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def carrega_sprite(direcao=False):
    todas_sprites = {}
    sprites = []
    sprite = pygame.image.load('imagens/harry_lado.png')

    sprites.append(sprite)

    if direcao:
        todas_sprites['harry_lado.png'.replace('.png', '') + '_direita'] = sprites
        todas_sprites['harry_lado.png'.replace('.png', '') + '_esquerda'] = inverte(sprites)
    else: 
        todas_sprites['harry_lado'.replace('.png', '')] = sprites
    
    return todas_sprites


def carrega_bloco():
    imagem = (pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (72, 72)))
    return imagem
               

def desenha(window, background, bg_image, harry, objetos, state):
    window.fill((0, 0, 0))

    if state['tela_inicio']:
        imagem = pygame.image.load('imagens/fundo_inicio.jpg')
        fundo = pygame.transform.scale(imagem, (1280, 720))
        window.blit(fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        fonte_titulo = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        titulo_jogo = fonte_titulo.render('Hogwarts Scape', True, ((211, 177, 110)))
        window.blit(titulo_jogo, (220, 130))
            
        fonte_text = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 60)

        play = fonte_text.render('Play', True, (174, 139, 71))
        play_rect = play.get_rect(center=(1280/2, 720/2))
        window.blit(play, play_rect)

        if play_rect.collidepoint((mouse_pos)) and pygame.mouse.get_pressed()[0]:
            state['tela_inicio'] = False
            state['tela_jogo'] = True

        instrucoes = fonte_text.render('Instruções', True, (174, 139, 71))
        instrucoes_rect = instrucoes.get_rect(center=(1280/2, 500))
        window.blit(instrucoes, instrucoes_rect)
        
        if instrucoes_rect.collidepoint((mouse_pos)) and pygame.mouse.get_pressed()[0]:
            state['tela_inicio'] = False
            state['tela_instrucoes'] = True

    if state['tela_instrucoes']:
        window.fill((230, 201, 143))

        mouse_pos = pygame.mouse.get_pos()

        fonte_text = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 60)

        play = fonte_text.render('Play', True, (174, 139, 71))
        play_rect = play.get_rect(center=(1280/2, 720/2))
        window.blit(play, play_rect)

        if play_rect.collidepoint((mouse_pos)) and pygame.mouse.get_pressed()[0]:
            state['tela_inicio'] = False
            state['tela_jogo'] = True
    
    if state['tela_jogo']:
        for tile in background:
            window.blit(bg_image, tile)

        for objeto in objetos:
            objeto.desenha(window)

        harry.desenha(window)

    pygame.display.update()


def main(window, assets, state):
    clock = pygame.time.Clock()
    background, bg_image = gera_fundo()
    harry = classes.Personagens(100, 100, 50, 50)
    tamanho_bloco = 72
    chao = [classes.Bloco(i * tamanho_bloco, 720 * tamanho_bloco, tamanho_bloco) for i in range(-1280 // tamanho_bloco, 1280 * 2 // tamanho_bloco)]
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

        if state['tela_jogo']:
            harry.loop(FPS)
            desenha(window, background, bg_image, harry, chao, state)
        else:
            desenha(window, background, bg_image, harry, chao, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    main(window, assets, state)