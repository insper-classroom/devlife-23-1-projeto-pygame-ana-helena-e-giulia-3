import pygame
from .personagens import Personagens

VEL_JOGADOR = 15
FPS = 60

class Tela_jogo():
    def __init__(self):
        self.largura_imagem_fundo = 144
        self.altura_imagem_fundo = 144
        self.fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (self.largura_imagem_fundo, self.altura_imagem_fundo))
        self.lista_imagem_fundo = []
        self.bloco = pygame.transform.scale(pygame.image.load('imagens/terreno.jpg'), (30, 30))
        self.harry = Personagens(100, 100)
        self.posicao_harry = [self.harry.rect.x, self.harry.rect.y]

    def gera_fundo(self):
        for i in range(1280 // self.largura_imagem_fundo + 1):
            for j in range(720 // self.altura_imagem_fundo + 1):
                posicao = (i * self.largura_imagem_fundo, j * self.altura_imagem_fundo)
                self.lista_imagem_fundo.append(posicao)
        
    def desenha(self, window):
        window.fill((0, 0, 0))

        self.gera_fundo()
        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)
        
        self.harry.desenha(window)
    

    def verifica_colisao(self):
        clock = pygame.time.Clock()
        clock.tick(FPS)
        self.harry.anda()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    self.harry.sprite =  pygame.transform.scale(pygame.image.load('imagens/harry_lado_esquerdo.png'), (135, 135))
                    self.harry.movimenta_esquerda(VEL_JOGADOR)
                if event.key == pygame.K_RIGHT: 
                    self.harry.sprite =  pygame.transform.scale(pygame.image.load('imagens/harry_lado_direito.png'), (135, 135))
                    self.harry.movimenta_direita(VEL_JOGADOR)
                if event.key == pygame.K_UP:
                    self.harry.pulo()
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.harry.movimenta_esquerda(0)
                if event.key == pygame.K_RIGHT:
                    self.harry.movimenta_direita(0) 
           