import pygame

class Objetos(pygame.sprite.Sprite):
    """
    Classe mãe de todos os objetos.

    Argumentos necessários:
        x (int): posição horizontal do bloco
        y (int): posição vertical do bloco
        largura: largura do bloco
        altura: altura do bloco
    """
    # classe 'mãe' 
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.image = pygame.Surface((largura, altura))
        self.largura = largura
        self.altura = altura
    
    def desenha(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bloco(Objetos):
    """
    Classe do bloco do jogo.
    """
    # classe do bloco do jogo
    def __init__(self, x, y, tamanho):
        super().__init__(x, y, tamanho, tamanho)
        bloco = pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (20, 20))
        self.image.blit(bloco, (0, 0)) 

class Água_Draco(Objetos):
    """
    Classe da água do Draco.
    """
    # classe da água do draco
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_draco = pygame.transform.scale(pygame.image.load('imagens/água_draco.jpg'), (160, 40))
        self.image.blit(água_draco, (0, 0)) 

class Água_Harry(Objetos):
    """
    Classe da água do Harry.
    """
    #  classe da água do harry
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_harry = pygame.transform.scale(pygame.image.load('imagens/água_harry.jpg'), (160, 40))
        self.image.blit(água_harry, (0, 0)) 

class Água_toxica(Objetos):
    """
    Classe da água tóxica de tamanho regular.
    """
    # classe da água tóxica de tamanho regular
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_toxica = pygame.transform.scale(pygame.image.load('imagens/água_tóxica.jpg'), (320, 40))
        self.image.blit(água_toxica, (0, 0)) 

class Água_toxica_2(Objetos):
    """
    Classe da água do tóxica de tamanho reduzido.
    """
    # classe da água tóxica de tamanho reduzido
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.rect = pygame.Rect(x,y-1,largura, altura+1)
        água_toxica = pygame.transform.scale(pygame.image.load('imagens/água_tóxica.jpg'), (120, 40))
        self.image.blit(água_toxica, (0, 0)) 

class Horcrux(Objetos):
    """
    Classe das horcruxes.
    """
    # classe das horcruxes
    def __init__(self, x, y, largura, altura, imagem):
        super().__init__(x, y, largura, altura)
        horcrux = pygame.transform.scale(pygame.image.load(imagem), (40, 40))
        self.image.blit(horcrux, (0, 0)) 

class Porta(Objetos):
    """
    Classe que gera a porta de saída das salas. 
    """
    # classe que gera a porta
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        porta = pygame.transform.scale(pygame.image.load('imagens/porta.png'), (70, 70))
        self.image.blit(porta, (0, 0))

class Diamante(Objetos):
    """
    Classe dos diamantes.
    """
    # classes dos diamantes
    def __init__(self, x, y, largura, altura, imagem):
        super().__init__(x, y, largura, altura) 
        diamante = pygame.transform.scale(pygame.image.load(imagem), (25, 25))
        self.image.blit(diamante, (0, 0)) 