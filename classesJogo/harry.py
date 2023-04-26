import pygame

class Harry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('imagens/harry_lado_direito.png'), (125, 125))
        self.rect = self.image.get_rect()
        # posicao inicial do boneco
        self.rect.x = -40
        self.rect.y = 555

    def movimenta_esquerda(self):
        self.rect.x -= 2
    
    def movimenta_direita(self):
        self.rect.x += 2