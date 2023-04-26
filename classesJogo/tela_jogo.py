import pygame
from .harry import Harry
from .draco import Draco
from .objetos import Bloco

class Tela_jogo():
    def __init__(self):
        self.largura_imagem_fundo = 144
        self.altura_imagem_fundo = 144
        self.fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (self.largura_imagem_fundo, self.altura_imagem_fundo)).convert_alpha()
        self.lista_imagem_fundo = []
        self.harry = Harry()
        self.draco = Draco()
        self.tamanho_bloco = 20
        self.lista_objetos = []
        self.todas_sprites = pygame.sprite.Group()
        self.todas_sprites.add(self.harry)
        self.todas_sprites.add(self.draco)
        self.gera_fundo() 
        self.gera_terreno()

    def gera_fundo(self):
        # gera a tela de fundo 
        for i in range(1280 // self.largura_imagem_fundo + 1):
            for j in range(720 // self.altura_imagem_fundo + 1):
                posicao = (i * self.largura_imagem_fundo, j * self.altura_imagem_fundo)
                self.lista_imagem_fundo.append(posicao)
    
    def gera_terreno(self):
        # desenha as bordas
        for i in range(64):
            chao = Bloco(i * self.tamanho_bloco, 700, self.tamanho_bloco)
            self.lista_objetos.append(chao)
        for i in range(64):
            teto = Bloco(i * self.tamanho_bloco, 0, self.tamanho_bloco)
            self.lista_objetos.append(teto)
        for i in range(36):
            parede_esquerda = Bloco(0, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(parede_esquerda)
        for i in range(36):
            parede_direita = Bloco(1260, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(parede_direita)

        # desenha dentro do mapa
        for i in range(64):
            chao = Bloco(i * self.tamanho_bloco, 680, self.tamanho_bloco)
            self.lista_objetos.append(chao)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 660, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 640, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 620, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 600, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(0, 7):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 570, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(0, 55):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 470, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(0, 55):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 450, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 390, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 430, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 410, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        for i in range(10, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 320, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(10, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 340, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 170, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 190, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita)
        for i in range(55, 64):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 220, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda)
        
    def desenha(self, window):
        # desenha tudo na tela 
        window.fill((0, 0, 0))

        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)
        
        for objeto in self.lista_objetos:
            objeto.desenha(window)

        self.todas_sprites.draw(window)

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