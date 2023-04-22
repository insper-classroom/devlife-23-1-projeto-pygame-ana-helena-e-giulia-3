import pygame
import funcoes

class Personagens(pygame.sprite.Sprite):
    GRAVIDADE = 1
    SPRITE = funcoes.carrega_sprite(True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.direcao = 'esquerda'
        self.animation_count = 0
        self.tempo_queda = 0
    
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
    
    def loop(self, fps):
        # self.y_vel += min(1, (self.tempo_queda / fps) * self.GRAVIDADE)
        self.movimenta(self.x_vel, self.y_vel)

        self.tempo_queda += 1
    
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
       

        
    
    
    


    