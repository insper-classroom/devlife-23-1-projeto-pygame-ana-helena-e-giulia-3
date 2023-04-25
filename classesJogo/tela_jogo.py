import pygame
from .harry import Harry
from .draco import Draco

VEL_JOGADOR = 15
FPS = 60

class Tela_jogo():
    def __init__(self):
        self.largura_imagem_fundo = 144
        self.altura_imagem_fundo = 144
        self.fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (self.largura_imagem_fundo, self.altura_imagem_fundo)).convert_alpha()
        self.lista_imagem_fundo = []
        self.harry = Harry()
        self.draco = Draco()
        self.todas_sprites = pygame.sprite.Group()
        self.todas_sprites.add(self.harry)
        self.todas_sprites.add(self.draco)
        self.gera_fundo() 

        # self.bloco = pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (30, 30))

    def gera_fundo(self):
        # gera a tela de fundo 
        for i in range(1280 // self.largura_imagem_fundo + 1):
            for j in range(720 // self.altura_imagem_fundo + 1):
                posicao = (i * self.largura_imagem_fundo, j * self.altura_imagem_fundo)
                self.lista_imagem_fundo.append(posicao)
        
    def desenha(self, window):
        # desenha tudo na tela 
        window.fill((0, 0, 0))

        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)

        self.todas_sprites.draw(window)
        pygame.display.update()

    def atualiza_estado(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.harry.movimenta_esquerda()
        if keys[pygame.K_RIGHT]:
            self.harry.movimenta_direita()
        
        if keys[pygame.K_a]:
            self.draco.movimenta_esquerda()
        if keys[pygame.K_d]:
            self.draco.movimenta_direita()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

        self.todas_sprites.update()

        
        return True