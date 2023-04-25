import pygame

class Personagens(pygame.sprite.Sprite):
    GRAVIDADE = 1

    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.transform.scale(pygame.image.load('imagens/harry_lado_direito.png'), (135, 135))
        self.mask = pygame.mask.from_surface(self.sprite)
        self.largura = 135
        self.altura = 135
        self.rect = pygame.Rect(x, y, self.largura, self.altura)
        self.x_vel = 0
        self.y_vel = 0
        self.tempo_queda = 0

    def movimenta(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def movimenta_esquerda(self, vel):
        self.x_vel = -vel
    
    def movimenta_direita(self, vel):
        self.x_vel = vel
    
    # def pulo(self):
    #     self.y_vel = -self.GRAVIDADE * 5
    #     self.tempo_queda = 0
    
    # def atingiu_chao(self):
    #     self.tempo_queda = 0
    #     self.y_vel = 0
       
    # def bateu_cabeca(self):
    #     self.y_vel *= -1
    
    # def update(self):
    #     self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
    #     self.mask = pygame.mask.from_surface(self.sprite)
    
    def anda(self):
        # self.y_vel += min(1, (self.tempo_queda / fps) * self.GRAVIDADE)
        self.movimenta(self.x_vel, self.y_vel)
        # self.tempo_queda += 1
        # self.update()

    def desenha(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))