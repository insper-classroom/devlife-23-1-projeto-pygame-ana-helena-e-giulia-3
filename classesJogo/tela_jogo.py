import pygame
from .harry import Harry

VEL_JOGADOR = 15
FPS = 60

class Tela_jogo():
    def __init__(self):
        self.largura_imagem_fundo = 144
        self.altura_imagem_fundo = 144
        self.fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (self.largura_imagem_fundo, self.altura_imagem_fundo))
        self.lista_imagem_fundo = []
        self.harry = Harry()
        self.todas_sprites = pygame.sprite.Group()
        self.todas_sprites.add(self.harry)
        self.delta_t = 0
        self.t0 = 0
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

        self.gera_fundo()
        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)

        self.todas_sprites.draw(window)

    def atualiza_estado(self):
        t1 = pygame.time.get_ticks()
        self.delta_t = (t1 - self.t0) / 1000
        self.t0 = t1

        self.todas_sprites.update(self.delta_t)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.harry.velocidade -= 500
                elif event.key == pygame.K_RIGHT:
                    self.harry.velocidade += 500

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.harry.velocidade += 500
                elif event.key == pygame.K_RIGHT:
                    self.harry.velocidade -= 500

        return True