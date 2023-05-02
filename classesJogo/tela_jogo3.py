import pygame
from .harry import Harry
from .draco import Draco
from .objetos import Bloco, Água_Draco, Água_Harry, Água_toxica, Diamante

class Tela_jogo3():
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
        self.conta_diamantes_draco = 0
        self.conta_diamantes_harry = 0
        self.conta_diamantes = 0
        self.sprite_personagens = pygame.sprite.Group()
        self.sprite_objetos = pygame.sprite.Group()
        self.sprite_aguas = pygame.sprite.Group()
        self.sprite_diamante_draco = pygame.sprite.Group()
        self.sprite_diamante_harry = pygame.sprite.Group()
        self.harry = Harry(self.lista_objetos, 580, 600)
        self.draco = Draco(self.lista_objetos, 670, 650)
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
        for i in range(10, 34):
            chao = Bloco(32 * self.tamanho_bloco, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(7, 34):
            chao = Bloco(16 * self.tamanho_bloco, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(7, 34):
            chao = Bloco(48 * self.tamanho_bloco, i * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(10, 23):
            chao = Bloco(i * self.tamanho_bloco, 30 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(43, 54):
            chao = Bloco(i * self.tamanho_bloco, 30 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(25, 40):
            chao = Bloco(i * self.tamanho_bloco, 26 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(43, 54):
            chao = Bloco(i * self.tamanho_bloco, 22 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(10, 23):
            chao = Bloco(i * self.tamanho_bloco, 22 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(25, 40):
            chao = Bloco(i * self.tamanho_bloco, 18 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(43, 54):
            chao = Bloco(i * self.tamanho_bloco, 14 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(10, 23):
            chao = Bloco(i * self.tamanho_bloco, 14 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(25, 40):
            chao = Bloco(i * self.tamanho_bloco, 10 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(11, 22):
            chao = Bloco(i * self.tamanho_bloco, 7 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(43, 53):
            chao = Bloco(i * self.tamanho_bloco, 7 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(43, 53):
            chao = Bloco(i * self.tamanho_bloco, 6 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(11, 22):
            chao = Bloco(i * self.tamanho_bloco, 6 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(1, 8):
            chao = Bloco(i * self.tamanho_bloco, 10 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(56, 63):
            chao = Bloco(i * self.tamanho_bloco, 10 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(1, 8):
            chao = Bloco(i * self.tamanho_bloco, 18 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(56, 63):
            chao = Bloco(i * self.tamanho_bloco, 18 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(1, 8):
            chao = Bloco(i * self.tamanho_bloco, 26 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)
        for i in range(56, 63):
            chao = Bloco(i * self.tamanho_bloco, 26 * self.tamanho_bloco, self.tamanho_bloco)
            self.lista_objetos.append(chao.rect)
            self.sprite_objetos.add(chao)

        # adiciona as águas na tela
        agua_draco = Água_Draco(1.5 * self.largura_agua, 120, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco.rect)
        self.sprite_aguas.add(agua_draco)

        agua_harry1 = Água_Harry(5.5 * self.largura_agua, 120, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry1.rect)
        self.sprite_aguas.add(agua_harry1)

        agua_toxica = Água_toxica(0, 680, 320, self.altura_agua)
        self.lista_agua_toxica.append(agua_toxica.rect)
        self.sprite_aguas.add(agua_toxica)

        agua_toxica2 = Água_toxica(960, 680, 320, self.altura_agua)
        self.lista_agua_toxica.append(agua_toxica2.rect)
        self.sprite_aguas.add(agua_toxica2)

        # adiciona os diamantes na tela 
        diamante_dm1 = Diamante(910, 370, 25, 25, 'imagens/diamante_draco.png')
        self.sprite_diamante_draco.add(diamante_dm1)

        diamante_dm2 = Diamante(320, 70, 25, 25, 'imagens/diamante_draco.png')
        self.sprite_diamante_draco.add(diamante_dm2)

        diamante_dm3 = Diamante(70, 300, 25, 25, 'imagens/diamante_draco.png')
        self.sprite_diamante_draco.add(diamante_dm3)

        diamante_dm4 = Diamante(250, 550, 25, 25, 'imagens/diamante_draco.png')
        self.sprite_diamante_draco.add(diamante_dm4)

        diamante_hp1 = Diamante(550, 450, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp1)

        diamante_hp2 = Diamante(770, 100, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp2)

        diamante_hp3 = Diamante(1200, 140, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp3)

        diamante_hp4 = Diamante(1000, 550, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp4)

    def checa_agua(self):
        # verifica se colidiu com qualquer água do jogo
        for agua_harry in self.lista_agua_harry:
            if self.draco.rect.colliderect(agua_harry):
                return 'draco_dead'

        for agua_draco in self.lista_agua_draco:
            if self.harry.rect.colliderect(agua_draco):
                return 'harry_dead'

        for agua_toxica in self.lista_agua_toxica:
            if self.harry.rect.colliderect(agua_toxica):
                return 'harry_deaddead'
            
            if self.draco.rect.colliderect(agua_toxica):
                return 'draco_deaddead'
    
    def checa_diamantes(self):
        # permite pegar os diamantes da tela 
        for diamante_draco in self.sprite_diamante_draco:
            if self.draco.rect.colliderect(diamante_draco):
                self.conta_diamantes += 1
                self.conta_diamantes_draco += 1
                diamante_draco.kill()

        for diamante_harry in self.sprite_diamante_harry:
            if self.harry.rect.colliderect(diamante_harry):
                self.conta_diamantes += 1
                self.conta_diamantes_harry += 1
                diamante_harry.kill()

    def desenha(self, window):
        # desenha tudo na tela 
        window.fill((0, 0, 0))

        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)

        self.sprite_personagens.draw(window)
        self.sprite_objetos.draw(window)
        self.sprite_aguas.draw(window)
        self.sprite_diamante_draco.draw(window)
        self.sprite_diamante_harry.draw(window)

    def atualiza_estado(self):
        # retorna qual tela deve ser desenhada em seguida e permite o jogador se mover 
        self.checa_agua()
        self.checa_diamantes()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.harry.image = pygame.transform.scale(pygame.image.load('imagens/harry_lado_esquerdo.png'), (50, 60))
            self.harry.movimenta_esquerda()
        if keys[pygame.K_RIGHT]:
            self.harry.image = pygame.transform.scale(pygame.image.load('imagens/harry_lado_direito.png'), (50, 60))
            self.harry.movimenta_direita()
        
        if keys[pygame.K_a]:
            self.draco.image = pygame.transform.scale(pygame.image.load('imagens/draco_lado_esquerdo.png'), (50, 60))
            self.draco.movimenta_esquerda()
        if keys[pygame.K_d]:
            self.draco.image = pygame.transform.scale(pygame.image.load('imagens/draco_lado_direito.png'), (50, 60))
            self.draco.movimenta_direita()
        
        if self.checa_agua() == 'harry_dead' and self.conta_diamantes == 8:
            return 'TELA_GANHOU'
        if self.checa_agua() == 'harry_deaddead' and self.conta_diamantes == 8:
            return 'TELA_GANHOU'
        if self.checa_agua() == 'harry_dead' or self.checa_agua() == 'draco_dead' or self.checa_agua() == 'harry_deaddead' or self.checa_agua() == 'draco_deaddead':
            return 'TELA_GAMEOVER'
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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