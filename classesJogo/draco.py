import pygame

class Draco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('imagens/draco_lado.png'), (135, 135))
        self.rect = self.image.get_rect()
        # posicao inicial do boneco
        self.rect.x = 200
        self.rect.y = 200

    def movimenta_esquerda(self):
        self.rect.x -= 2
    
    def movimenta_direita(self):
        self.rect.x += 2