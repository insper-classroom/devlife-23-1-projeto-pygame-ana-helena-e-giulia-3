import pygame

class Draco(pygame.sprite.Sprite):
    def __init__(self, lista_blocos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('imagens/draco_lado.png'), (50, 60))
        self.rect = self.image.get_rect()
        # posicao inicial do boneco
        self.lista_blocos = lista_blocos
        self.rect.x = 20
        self.rect.y = 500
        self.GRAVIDADE = 2
        self.jump = 70
        self.state = {
            'pulando': False,
            'caindo': True
        }

    def movimenta_esquerda(self):
        self.rect.x -= 2

         # colisao com parede esquerda
        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.x += 2
    
    def movimenta_direita(self):
        self.rect.x += 2

        # colisao com parede direita
        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.x -= 2

    def update(self):
        if self.state['pulando'] == True:
            self.rect.y -= self.jump
        if self.state['caindo'] == True:
            self.rect.y += self.GRAVIDADE
        self.state['caindo'] = True
        self.state['pulando'] = False

        if self.rect.y < 20:
            self.rect.y = 20 + self.jump

        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.y -= self.GRAVIDADE
            self.state['caindo'] = False