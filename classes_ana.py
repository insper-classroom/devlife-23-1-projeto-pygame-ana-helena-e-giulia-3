import pygame
import funcoes_ana

class Personagens(pygame.sprite.Sprite):
    GRAVIDADE = 1
    SPRITE = funcoes_ana.upload_sprite_sheets(32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.direcao = 'esquerda'
        self.animation_count = 0
        self.tempo_queda = 0
        self.mask = None
        self.conta_pulo = 0

    def movimenta(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def movimenta_esquerda(self, vel):
        self.x_vel = -vel
        if self.direcao != 'esquerda':
            self.direcao = 'esquerda'
            self.animation_count = 0
    
    def movimenta_direita(self, vel):
        self.x_vel = vel
        if self.direcao != 'direita':
            self.direcao = 'direita'
            self.animation_count = 0
    
    def pulo(self):
        self.y_vel = -self.GRAVIDADE * 5
        self.animation_count = 0
        self.conta_pulo += 1
        if self.conta_pulo == 1:
            self.tempo_queda = 0
    
    def atingiu_chao(self):
        self.tempo_queda = 0
        self.y_vel = 0
        self.conta_pulo = 0
    
    def bateu_cabeca(self):
        self.conta = 0
        self.y_vel *= -1
    
    def update_sprite(self):
        sprite_sheet = "harry_frente"
        if self.y_vel != 0 and self.x_vel != 0:
            sprite_sheet = "harry_lado"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
    
    def loop(self, fps):
        self.y_vel += min(1, (self.tempo_queda / fps) * self.GRAVIDADE)
        self.movimenta(self.x_vel, self.y_vel)

        self.tempo_queda += 1
        self.update_sprite()
    
    def desenha(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))

class Objetos(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, nome=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
        self.largura = largura
        self.altura = altura
        self.nome = nome
    
    def desenha(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bloco(Objetos):
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho, tamanho)
        bloco = funcoes_ana.carrega_bloco()
        self.image.blit(bloco, (0, 0))
       
class Tela_inicial():
    def __init__(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def desenha(self, window):
        window.fill(0, 0, 0)

        imagem_fundo = pygame.image.load('imagens/fundo_inicio.png')
        fundo = pygame.transform.scale(imagem_fundo, (1280, 720))
        window.blit(fundo, (0, 0))

        fonte = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        titulo_jogo = fonte.render('Hogwarts Scape', True, (211, 177, 110))
        window.blit(titulo_jogo, (220, 130))

        fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 60)

        self.botao_rect_play = pygame.Rect(515, 315, 250, 80)
        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_play)
        play = fonte_texto.render('Play', True, (174, 139, 71))
        play_rect = play.get_rect(center=(1280/2, 720/2))
        window.blit(play, play_rect)
        
        self.botao_rect_instruc = pygame.Rect(445, 455, 390, 80)
        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_instruc)
        instrucoes = fonte_texto.render('Instruções', True, (174, 139, 71))
        instrucoes_rect = instrucoes.get_rect(center=(1280/2, 500))
        window.blit(instrucoes, instrucoes_rect)

        pygame.display.update()

    def verifica_colisao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.botao_rect_play.collidepoint(self.mouse_pos):
                    return True
                elif self.botao_rect_instruc.collidepoint(self.mouse_pos):
                    return True
        return self

class Tela_harry():
    def __init__(self, imagem_fundo, imagem_harry, caminho_fonte):
        self.imagem_fundo = imagem_fundo
        self.imagem_harry = imagem_harry 
        self.mouse_pos = pygame.mouse.get_pos()
        self.caminho_fonte = caminho_fonte

    def desenha(self, window):
        window.fill(0, 0, 0)

        fundo = pygame.image.load(f'{self.imagem_fundo}')
        window.blit(fundo, (0, 0))

        fonte_texto = pygame.font.Font(f'{self.caminho_fonte}', 30)

        prosseguir = fonte_texto.render('Prosseguir', True, (174, 139, 71))
        self.prosseguir_rect = prosseguir.get_rect(center=(1180, 700))
        window.blit(prosseguir, self.prosseguir_rect)

        harry_img = pygame.image.load(f'{self.imagem_harry}')
        harry_maior = pygame.transform.scale(harry_img, (700, 700))
        window.blit(harry_maior, (-300, 30))

        t1 = fonte_texto.render('Olá! Eu sou o', True, (0, 0, 0))
        window.blit(t1, (500, 120))
        t2 = fonte_texto.render('Harry Potter! Estou', True, (0, 0, 0))
        window.blit(t2, (470, 160))
        t3 = fonte_texto.render('preso no porão da', True, (0, 0, 0))
        window.blit(t3, (470, 200))
        t4 = fonte_texto.render('Malfoy Manor e', True, (0, 0, 0))
        window.blit(t4, (470, 240))
        t5 = fonte_texto.render('preciso da sua ajuda!', True, (0, 0, 0))
        window.blit(t5, (460, 280))

        pygame.display.update()

    def verifica_colisao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.prosseguir_rect.collidepoint(self.mouse_pos):
                    return True
                
class Tela_instrucoes():
    def __init__(self, imagem_fundo, caminho_fonte, texto, tamanho_fonte):
        self.imagem_fundo = imagem_fundo
        self.mouse_pos = pygame.mouse.get_pos()
        self.caminho_fonte = caminho_fonte
        self.texto = texto
        self.tamanho = tamanho_fonte

    def desenha(self, window):
        window.fill(0, 0, 0)

        fundo = pygame.image.load(f'{self.imagem_fundo}')
        window.blit(fundo, (0, 0))

        fonte_titulo = pygame.font.Font(f'{self.caminho_fonte}', 70)
        fonte_texto = pygame.font.Font(f'{self.caminho_fonte}', 30)

        instrucoes = fonte_titulo.render('Instruções', True, (174, 139, 71))
        window.blit(instrucoes, (445, 120))

        t1 = fonte_texto.render('- Use aswd para movimentar Draco Malfoy', True, (211, 177, 110))
        window.blit(t1, (280, 220))
        t2 = fonte_texto.render('- Use as setas para movimentar Harry Potter', True, (211, 177, 110))
        window.blit(t2, (280, 270)) 
        t3 = fonte_texto.render('- Colete as horcrux para ganhar pontos e', True, (211, 177, 110))
        window.blit(t3, (280, 320)) 
        t3b = fonte_texto.render('conseguir escapar da sala!', True, (211, 177, 110))
        window.blit(t3b, (295, 355)) 
        t4b = fonte_texto.render('- O objetivo do jogo é salvar Harry Potter e', True, (211, 177, 110))
        window.blit(t4b, (280, 405))
        t4c = fonte_texto.render('Draco Malfoy da Malfoy Manor', True, (211, 177, 110))
        window.blit(t4c, (295, 440)) 
        t5b = fonte_texto.render('- Se Draco Malfoy cair no líquido vermelho,', True, (211, 177, 110))
        window.blit(t5b, (280, 490))
        t5c = fonte_texto.render('ele morre, assim como Harry Potter morre', True, (211, 177, 110))
        window.blit(t5c, (295, 525)) 
        t5d = fonte_texto.render('ao cair no líquido azul', True, (211, 177, 110))
        window.blit(t5d, (295, 560)) 

        jogar = fonte_texto.render('Jogar', True, (174, 139, 71))
        jogar_rect = jogar.get_rect(center=(1195, 700))
        window.blit(jogar, jogar_rect)
