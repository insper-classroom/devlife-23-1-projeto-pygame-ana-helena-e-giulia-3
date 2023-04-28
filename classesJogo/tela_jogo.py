import pygame
from .harry import Harry
from .draco import Draco
from .objetos import Bloco, Água_Draco, Água_Harry, Água_toxica, Horcrux

class Tela_jogo():
    def __init__(self):
        self.largura_imagem_fundo = 144
        self.altura_imagem_fundo = 144
        self.fundo = pygame.transform.scale(pygame.image.load('imagens/fundo.jpg'), (self.largura_imagem_fundo, self.altura_imagem_fundo)).convert_alpha()
        self.lista_imagem_fundo = []
        self.tamanho_bloco = 20
        self.largura_agua = 160
        self.altura_agua = 40
        self.lista_objetos = []
        self.lista_agua_draco = []
        self.lista_agua_harry = []
        self.lista_agua_toxica = []
        self.lista_horcruxes = []
        self.sprite_personagens = pygame.sprite.Group()
        self.sprite_objetos = pygame.sprite.Group()
        self.sprite_aguas = pygame.sprite.Group()
        self.sprite_horcruxes = pygame.sprite.Group()
        self.harry = Harry(self.lista_objetos)
        self.draco = Draco(self.lista_objetos)
        self.sprite_personagens.add(self.harry)
        self.sprite_personagens.add(self.draco)
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
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(64):
            teto = Bloco(i * self.tamanho_bloco, 0, self.tamanho_bloco)
            self.lista_objetos.append(teto.rect)
            self.sprite_objetos.add(teto)
        for i in range(36):
            parede_esquerda = Bloco(0, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(parede_esquerda.rect)
            self.sprite_objetos.add(parede_esquerda)
        for i in range(36):
            parede_direita = Bloco(1260, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(parede_direita.rect)
            self.sprite_objetos.add(parede_direita)

        # desenha dentro do mapa
        for i in range(64):
            chao = Bloco(i * self.tamanho_bloco, 680, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 660, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 640, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 620, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(59, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 600, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(0, 7):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 570, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 55):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 470, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 55):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 450, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 390, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 430, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 5):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 410, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(10, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 320, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(10, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 340, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 170, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 190, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(55, 64):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 220, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)

        # plataforma das horcruxes
        for i in range(15, 25):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 570, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)

        # adiciona as aguas na tela
        agua_draco = Água_Draco(2 * self.largura_agua, 680, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco.rect)
        self.sprite_aguas.add(agua_draco)

        agua_draco2 = Água_Draco(5 * self.largura_agua, 450, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco2.rect)
        self.sprite_aguas.add(agua_draco2)

        agua_harry1 = Água_Harry(4 * self.largura_agua, 680, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry1.rect)
        self.sprite_aguas.add(agua_harry1)

        agua_harry2 = Água_Harry(3 * self.largura_agua, 320, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry2.rect)
        self.sprite_aguas.add(agua_harry2)

        agua_toxica = Água_toxica(320, 450, 320, self.altura_agua)
        self.lista_agua_toxica.append(agua_toxica.rect)
        self.sprite_aguas.add(agua_toxica)

        agua_toxica2 = Água_toxica(800, 320, 320, self.altura_agua)
        self.lista_agua_toxica.append(agua_toxica2.rect)
        self.sprite_aguas.add(agua_toxica2)

        # adiciona as horcruxes na tela
        diario = Horcrux(380, 520, 40, 40, 'imagens/diario_tom_riddle.png')
        self.lista_horcruxes.append(diario.rect)
        self.sprite_horcruxes.add(diario)

        medalhao = Horcrux(600, 500, 40, 40, 'imagens/medalhao.png')
        self.lista_horcruxes.append(medalhao.rect)
        self.sprite_horcruxes.add(medalhao)

        taca = Horcrux(700, 500, 40, 40, 'imagens/taca.png')
        self.lista_horcruxes.append(taca.rect)
        self.sprite_horcruxes.add(taca)
        
    def checa_agua(self):
        for agua_harry in self.lista_agua_harry:
            if self.draco.rect.colliderect(agua_harry):
                return -1

        for agua_draco in self.lista_agua_draco:
            if self.harry.rect.colliderect(agua_draco):
                return -1

        for agua_toxica in self.lista_agua_toxica:
            if self.harry.rect.colliderect(agua_toxica) or self.draco.rect.colliderect(agua_toxica):
                return -1
        
    def desenha(self, window):
        # desenha tudo na tela 
        window.fill((0, 0, 0))

        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)

        self.sprite_personagens.draw(window)
        self.sprite_objetos.draw(window)
        self.sprite_aguas.draw(window)
        self.sprite_horcruxes.draw(window)

    def atualiza_estado(self):
        self.checa_agua()

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
            if self.checa_agua() == -1:
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.draco.state['pulando'] = True
                    self.draco.state['caindo'] = False

                if event.key == pygame.K_UP:
                    self.harry.state['pulando'] = True
                    self.harry.state['caindo'] = False

        self.sprite_personagens.update()
        self.sprite_objetos.update()

        return True