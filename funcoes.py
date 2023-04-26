import pygame
import classesJogo.objetos as objetos
from classesJogo.harry import Personagens
from os import listdir
from os.path import isfile, join

def inicializa():
    pygame.init()
    pygame.display.set_caption("Hogwarts Scape")
    window = pygame.display.set_mode((1290, 720))

    assets = {
        'musica_fundo': pygame.mixer.music.load('som/musica_tema.mp3')
    }

    state = {
        'tela_inicio': True,
        'tela_instrucoes': False,
        'tela_instrucoes2': False,
        'tela_jogo': False,
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

def carrega_bloco():
    imagem = (pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (30, 30)))
    return imagem    

def colisao_vertical(harry, objetos, y_vel):
    objetos_colididos = []
    for objeto in objetos:
        if pygame.sprite.collide_mask(harry, objeto):
            if y_vel > 0:
                harry.rect.bottom = objeto.rect.top
                harry.atingiu_chao()
            elif y_vel < 0:
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
#     harry.update()desenha
#     return objeto_colidido


def desenha(window, background, bg_image, harry, objetos, state):
    window.fill((0, 0, 0))

    if state['tela_inicio']:
        imagem = pygame.image.load('imagens/fundo_inicio.png')
        fundo = pygame.transform.scale(imagem, (1280, 720))
        window.blit(fundo, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        fonte_titulo = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        titulo_jogo = fonte_titulo.render('Hogwarts Scape', True, ((211, 177, 110)))
        window.blit(titulo_jogo, (220, 130))
            
        fonte_text = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 60)

        botao_rect_play = pygame.Rect(515, 315, 250, 80)
        pygame.draw.rect(window, (240, 229, 198), botao_rect_play)
        play = fonte_text.render('Play', True, (174, 139, 71))
        play_rect = play.get_rect(center=(1280/2, 720/2))
        window.blit(play, play_rect)

        if botao_rect_play.collidepoint((mouse_pos)) and pygame.mouse.get_pressed()[0]:
            state['tela_inicio'] = False
            state['tela_jogo'] = True

        botao_rect_instruc = pygame.Rect(445, 455, 390, 80)
        pygame.draw.rect(window, (240, 229, 198), botao_rect_instruc)
        instrucoes = fonte_text.render('Instruções', True, (174, 139, 71))
        instrucoes_rect = instrucoes.get_rect(center=(1280/2, 500))
        window.blit(instrucoes, instrucoes_rect)
        
        if botao_rect_instruc.collidepoint((mouse_pos)) and pygame.mouse.get_pressed()[0]:
            state['tela_inicio'] = False
            state['tela_instrucoes'] = True

    elif state['tela_instrucoes']:
        fundo_rpg = pygame.image.load('imagens/fundo_rpg.png')
        window.blit(fundo_rpg, (0, 0))

        mouse_pos1 = pygame.mouse.get_pos()

        fonte_text2 = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 30)

        prosseguir = fonte_text2.render('Prosseguir', True, (174, 139, 71))
        prosseguir_rect = prosseguir.get_rect(center=(1180, 700))
        window.blit(prosseguir, prosseguir_rect)

        harry_img = pygame.image.load('imagens/harry_frente.png')
        harry_maior = pygame.transform.scale(harry_img, (700, 700))
        window.blit(harry_maior, (-300, 30))

        t1 = fonte_text2.render('Olá! Eu sou o', True, (0, 0, 0))
        window.blit(t1, (500, 120))
        t2 = fonte_text2.render('Harry Potter! Estou', True, (0, 0, 0))
        window.blit(t2, (470, 160))
        t3 = fonte_text2.render('preso no porão da', True, (0, 0, 0))
        window.blit(t3, (470, 200))
        t4 = fonte_text2.render('Malfoy Manor e', True, (0, 0, 0))
        window.blit(t4, (470, 240))
        t5 = fonte_text2.render('preciso da sua ajuda!', True, (0, 0, 0))
        window.blit(t5, (460, 280))

        if prosseguir_rect.collidepoint((mouse_pos1)) and pygame.mouse.get_pressed()[0]:
            state['tela_instrucoes'] = False
            state['tela_instrucoes2'] = True

    elif state['tela_instrucoes2']:
        fundo_instruc = pygame.image.load('imagens/fundo_instrucoes.png')
        window.blit(fundo_instruc, (0, 0))

        mouse_pos2 = pygame.mouse.get_pos()

        fonte_tit = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 70)
        fonte_text1 = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 30)

        instruc = fonte_tit.render('Instruções', True, (174, 139, 71))
        window.blit(instruc, (445, 120))

        i1 = fonte_text1.render('- Use aswd para movimentar Draco Malfoy', True, (211, 177, 110))
        window.blit(i1, (280, 220))
        i2 = fonte_text1.render('- Use as setas para movimentar Harry Potter', True, (211, 177, 110))
        window.blit(i2, (280, 270)) 
        i3 = fonte_text1.render('- Colete as horcrux para ganhar pontos e', True, (211, 177, 110))
        window.blit(i3, (280, 320)) 
        i3c = fonte_text1.render('conseguir escapar da sala!', True, (211, 177, 110))
        window.blit(i3c, (295, 355)) 
        i4 = fonte_text1.render('- O objetivo do jogo é salvar Harry Potter e', True, (211, 177, 110))
        window.blit(i4, (280, 405))
        i4c = fonte_text1.render('Draco Malfoy da Malfoy Manor', True, (211, 177, 110))
        window.blit(i4c, (295, 440)) 
        i5 = fonte_text1.render('- Se Draco Malfoy cair no líquido vermelho,', True, (211, 177, 110))
        window.blit(i5, (280, 490))
        i5c = fonte_text1.render('ele morre, assim como Harry Potter morre', True, (211, 177, 110))
        window.blit(i5c, (295, 525)) 
        i5cc = fonte_text1.render('ao cair no líquido azul', True, (211, 177, 110))
        window.blit(i5cc, (295, 560)) 

        jogar = fonte_text1.render('Jogar', True, (174, 139, 71))
        jogar_rect = jogar.get_rect(center=(1195, 700))
        window.blit(jogar, jogar_rect)

        if jogar_rect.collidepoint((mouse_pos2)) and pygame.mouse.get_pressed()[0]:
            state['tela_instrucoes2'] = False
            state['tela_jogo'] = True
    
    elif state['tela_jogo']:
        for tile in background:
            window.blit(bg_image, tile)
        
        for objeto in objetos:
            objeto.desenha(window)

        harry.desenha(window)

    pygame.display.update()


def main(window, assets, state):
    clock = pygame.time.Clock()
    background, bg_image = gera_fundo()
    harry = Personagens(100, 100, 129, 72)
    tamanho_bloco = 30
    lista_objetos = []
    for i in range(43):
        chao = objetos.Bloco(i * tamanho_bloco, 690, tamanho_bloco)
        lista_objetos.append(chao)
    for i in range(43):
        teto = objetos.Bloco(i * tamanho_bloco, 0, tamanho_bloco)
        lista_objetos.append(teto)
    for i in range(24):
        parede_esquerda = objetos.Bloco(0, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_esquerda)
    for i in range(24):
        parede_direita = objetos.Bloco(1260, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_direita)
    for i in range(19,23):
        parede_direita = objetos.Bloco(1230, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_direita)
    for i in range(21,23):
        parede_direita = objetos.Bloco(1200, i * tamanho_bloco, tamanho_bloco)
        lista_objetos.append(parede_direita)
    for i in range(1,20):
        parede_direita = objetos.Bloco(i * tamanho_bloco, 570, tamanho_bloco)
        lista_objetos.append(parede_direita)
    for i in range(1,20):
        parede_direita = objetos.Bloco(i * tamanho_bloco, 450, tamanho_bloco)
        lista_objetos.append(parede_direita)
    
    parede_direita = objetos.Bloco(20 * tamanho_bloco, 480, tamanho_bloco)
    lista_objetos.append(parede_direita)
    for i in range(21, 39):
        parede_direita = objetos.Bloco(i * tamanho_bloco, 510, tamanho_bloco)
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
                    harry.sprite = pygame.image.load('imagens/harry_lado_esquerdo.png')
                    harry.movimenta_esquerda(VEL_JOGADOR)
                if event.key == pygame.K_RIGHT: 
                    harry.sprite = pygame.image.load('imagens/harry_lado_direito.png')
                    harry.movimenta_direita(VEL_JOGADOR)
                if event.key == pygame.K_UP:
                    harry.pulo()
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    harry.movimenta_esquerda(0)
                if event.key == pygame.K_RIGHT:
                    harry.movimenta_direita(0) 

        if state['tela_jogo']:
            harry.loop(FPS)
            colisao_vertical(harry, lista_objetos, harry.y_vel)
            desenha(window, background, bg_image, harry, lista_objetos, state)
        else:
            desenha(window, background, bg_image, harry, lista_objetos, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    main(window, assets, state)