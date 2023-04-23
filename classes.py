import pygame
import funcoes

class Personagens(pygame.sprite.Sprite):
    GRAVIDADE = 1
    SPRITE = funcoes.upload_harry(True)
    ANIMATION_DELAY = 3
    # SPRITE = funcoes.upload_draco(True)

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

        self.sprite = self.SPRITE['harry_lado_' + self.direcao][0]
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
        self.sprite = self.SPRITE['harry_lado_' + self.direcao][0]
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
        bloco = funcoes.carrega_bloco()
        self.image.blit(bloco, (0, 0))
       

        
    
    
    


    