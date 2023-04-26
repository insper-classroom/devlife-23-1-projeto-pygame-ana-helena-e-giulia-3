import pygame

class Objetos(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.image = pygame.Surface((largura, altura))
        self.largura = largura
        self.altura = altura
    
    def desenha(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bloco(Objetos):
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho, tamanho)
        bloco = pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (20, 20))
        self.image.blit(bloco, (0, 0)) 