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

class Água_Draco(Objetos):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_draco = pygame.transform.scale(pygame.image.load('imagens/água_draco.jpg'), (160, 40))
        self.image.blit(água_draco, (0, 0)) 

class Água_Harry(Objetos):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_harry = pygame.transform.scale(pygame.image.load('imagens/água_harry.jpg'), (160, 40))
        self.image.blit(água_harry, (0, 0)) 

class Água_toxica(Objetos):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_toxica = pygame.transform.scale(pygame.image.load('imagens/água_tóxica.jpg'), (320, 40))
        self.image.blit(água_toxica, (0, 0)) 

