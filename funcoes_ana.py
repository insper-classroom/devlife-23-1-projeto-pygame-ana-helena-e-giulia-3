import pygame
import classesJogo.objetos as objetos
from os import listdir
from os.path import isfile, join

def inicializa():
    pygame.init()
    pygame.display.set_caption("Hogwarts Scape")
    window = pygame.display.set_mode((1280, 720))

    assets = {
        'musica_fundo': pygame.mixer.music.load('som/musica_tema.mp3')
    }

    state = {
        'tela': objetos.Tela_inicial('imagens/fundo_inicio.png', 'docs/font/WizardWorldSimplified-Kxr7.ttf')
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


def upload_sprite_sheets(largura, altura, direcao=False):
    path = join("imagens")
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image))

        sprites = []
        for i in range(sprite_sheet.get_width() // largura):
            surface = pygame.Surface((largura, altura), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * largura, 0, largura, altura)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direcao:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = inverte(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def carrega_bloco():
    imagem = (pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (80, 80)))
    return imagem    

def colisao_vertical(harry, objetos, y_vel):
    objetos_colididos = []
    for objeto in objetos:
        if pygame.sprite.collide_mask(harry, objeto):
            if y_vel > 0:
                harry.rect.bottom = objeto.rect.top
                harry.atingiu_chao()
            if y_vel < 0:
                harry.rect.top = objeto.rect.bottom
                harry.bateu_cabeca()
        objetos_colididos.append(objeto)
    
    return objetos_colididos

# # def colisao_horizontal(harry, objetos, dx):
# #     harry.movimenta(dx, 0)
# #     harry.update()
# #     objeto_colidido = None
# #     for objeto in objetos:
# #         if pygame.sprite.collide_mask(harry, objeto):
# #             objeto_colidido = objeto
# #             break
    
#     harry.movimenta(-dx, 0)
#     harry.update()
#     return objeto_colidido


def desenha(window, background, bg_image, harry, objetos, state):
    state['tela'].desenha(window)

    # if state['tela_instrucoes2']:
    #     fundo_instruc = pygame.image.load('imagens/fundo_instrucoes.png')
    #     window.blit(fundo_instruc, (0, 0))

    #     mouse_pos1 = pygame.mouse.get_pos()

    #     fonte_tit = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 70)
    #     fonte_text1 = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 30)

    #     instruc = fonte_tit.render('Instruções', True, (174, 139, 71))
    #     window.blit(instruc, (445, 120))

    #     i1 = fonte_text1.render('- Use aswd para movimentar Draco Malfoy', True, (211, 177, 110))
    #     window.blit(i1, (280, 220))
    #     i2 = fonte_text1.render('- Use as setas para movimentar Harry Potter', True, (211, 177, 110))
    #     window.blit(i2, (280, 270)) 
    #     i3 = fonte_text1.render('- Colete as horcrux para ganhar pontos e', True, (211, 177, 110))
    #     window.blit(i3, (280, 320)) 
    #     i3c = fonte_text1.render('conseguir escapar da sala!', True, (211, 177, 110))
    #     window.blit(i3c, (295, 355)) 
    #     i4 = fonte_text1.render('- O objetivo do jogo é salvar Harry Potter e', True, (211, 177, 110))
    #     window.blit(i4, (280, 405))
    #     i4c = fonte_text1.render('Draco Malfoy da Malfoy Manor', True, (211, 177, 110))
    #     window.blit(i4c, (295, 440)) 
    #     i5 = fonte_text1.render('- Se Draco Malfoy cair no líquido vermelho,', True, (211, 177, 110))
    #     window.blit(i5, (280, 490))
    #     i5c = fonte_text1.render('ele morre, assim como Harry Potter morre', True, (211, 177, 110))
    #     window.blit(i5c, (295, 525)) 
    #     i5cc = fonte_text1.render('ao cair no líquido azul', True, (211, 177, 110))
    #     window.blit(i5cc, (295, 560)) 

    #     jogar = fonte_text1.render('Jogar', True, (174, 139, 71))
    #     jogar_rect = jogar.get_rect(center=(1195, 700))
    #     window.blit(jogar, jogar_rect)

    #     if jogar_rect.collidepoint((mouse_pos1)) and pygame.mouse.get_pressed()[0]:
    #         state['tela_instrucoes2'] = False
    #         state['tela_jogo'] = True
    
    # elif state['tela_jogo']:
    #     for tile in background:
    #         window.blit(bg_image, tile)
        
    #     for objeto in objetos:
    #         objeto.desenha(window)

    #     harry.desenha(window)

    pygame.display.update()


def main(window, assets, state):
    clock = pygame.time.Clock()
    background, bg_image = gera_fundo()
    harry = objetos.Personagens(100, 100, 50, 50)
    tamanho_bloco = 80
    lista_objetos = []
    for i in range(16):
        chao = objetos.Bloco(i * tamanho_bloco, 640, tamanho_bloco)
        lista_objetos.append(chao)
    for i in range(16):
        teto = objetos.Bloco(i * tamanho_bloco, 0, tamanho_bloco)
        lista_objetos.append(teto)
    for i in range(9):
        parede_esquerda = objetos.Bloco(0, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_esquerda)
    for i in range(9):
        parede_direita = objetos.Bloco(1200, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_direita)
    
    # colisao_esquerda = colisao_horizontal(harry, lista_objetos, -VEL_JOGADOR)
    # colisao_direita = colisao_horizontal(harry, lista_objetos, VEL_JOGADOR)
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
                if event.key == pygame.K_UP:
                    harry.pulo()
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    harry.movimenta_esquerda(0)
                if event.key == pygame.K_RIGHT:
                    harry.movimenta_direita(0) 

            if state['tela'].verifica_colisao() == -1:
                print('oi')

        # if state['tela_jogo']:
        #     harry.loop(FPS)
        #     colisao_vertical(harry, lista_objetos, harry.y_vel)
        #     desenha(window, background, bg_image, harry, lista_objetos, state)
        # else:
        #     desenha(window, background, bg_image, harry, lista_objetos, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    main(window, assets, state)