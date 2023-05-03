import pygame
from .harry import Harry
from .draco import Draco
from .objetos import Bloco, Água_Draco, Água_Harry, Horcrux, Porta, Diamante

class Tela_jogo2():
    """
    Representa a tela da segunda fase do jogo e controla sua renderização, bem como as interações dos personagens e objetos.
    """
    def __init__(self):
        """
        Inicializa os atributos da instância da classe Tela_jogo2.
        
        Atributos:
            largura_imagem_fundo (int): inteiro que armazena a largura da imagem de fundo
            altura_imagem_fundo (int): inteiro que armazena a altura da imagem de fundo
            fundo (Surface): imagem de fundo carregada do arquivo 'imagens/fundo.jpg' e redimensionada para a largura e altura definidas pelos atributos largura_imagem_fundo e altura_imagem_fundo
            lista_imagem_fundo (list): lista que armazena as imagens de fundo geradas na função gera_fundo()
            tamanho_bloco (int): inteiro que armazena o tamanho do bloco do terreno
            largura_agua (int): inteiro que armazena a largura da água na tela
            altura_agua (int): inteiro que armazena a altura da água na tela
            lista_objetos (list): lista que armazena os objetos do jogo, como diamantes e horcruxes
            lista_agua_draco (list): lista que armazena as águas próximas ao Draco
            lista_agua_harry (list): lista que armazena as águas próximas ao Harry
            lista_agua_toxica (list): lista que armazena as águas tóxicas
            conta_horcruxes (int): inteiro que armazena a quantidade de horcruxes coletadas pelos jogadores
            conta_diamantes_draco (int): inteiro que armazena a quantidade de diamantes coletados pelo Draco
            conta_diamantes_harry (int): inteiro que armazena a quantidade de diamantes coletados pelo Harry
            conta_diamantes (int): inteiro que armazena a quantidade total de diamantes coletados pelos jogadores
            sprite_personagens (Group): sprite group que armazena os personagens do jogo (Harry e Draco)
            sprite_objetos (Group): sprite group que armazena os objetos do jogo (Porta)
            sprite_aguas (Group): sprite group que armazena as águas do jogo (água do rio e água tóxica)
            sprite_horcrux_draco (Group): sprite group que armazena os horcruxes coletados pelo Draco
            sprite_horcrux_harry (Group): sprite group que armazena os horcruxes coletados pelo Harry
            sprite_diamante_draco (Group): sprite group que armazena os diamantes coletados pelo Draco
            sprite_diamante_harry (Group): sprite group que armazena os diamantes coletados pelo Harry
            sprite_nagini (Group): sprite group que armazena a personagem Nagini
            harry (Harry): objeto da classe Harry, que representa o personagem Harry na tela
            draco (Draco): objeto da classe Draco, que representa o personagem Draco na tela
            porta (Porta): objeto da classe Porta, que representa a porta que leva ao jogo 2 na tela
        """
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
        self.conta_horcruxes = 0
        self.conta_diamantes_draco = 0
        self.conta_diamantes_harry = 0
        self.conta_diamantes = 0
        self.sprite_personagens = pygame.sprite.Group()
        self.sprite_objetos = pygame.sprite.Group()
        self.sprite_aguas = pygame.sprite.Group()
        self.sprite_horcrux_draco = pygame.sprite.Group()
        self.sprite_horcrux_harry = pygame.sprite.Group()
        self.sprite_diamante_draco = pygame.sprite.Group()
        self.sprite_diamante_harry = pygame.sprite.Group()
        self.sprite_nagini = pygame.sprite.Group()
        self.harry = Harry(self.lista_objetos, 20, 600)
        self.draco = Draco(self.lista_objetos, 1200, 600)
        self.porta = Porta(1170, 110, 70, 70)
        self.sprite_personagens.add(self.harry)
        self.sprite_personagens.add(self.draco)
        self.sprite_objetos.add(self.porta)
        self.gera_fundo() 
        self.gera_terreno()

    def gera_fundo(self):
        """
        Método que gera a imagem de fundo da tela do jogo. 
        """
        # gera a tela de fundo 
        for i in range(1280 // self.largura_imagem_fundo + 1):
            for j in range(720 // self.altura_imagem_fundo + 1):
                posicao = (i * self.largura_imagem_fundo, j * self.altura_imagem_fundo)
                self.lista_imagem_fundo.append(posicao)
    
    def gera_terreno(self):
        """
        Método que gera as plataformas e as bordas do jogo, assim como os objetos nele existentes. 
        """
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
        for i in range(12, 50):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 440, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 170, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(0, 47):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 190, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(55, 64):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 180, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)

        # plataforma das horcruxes
        for i in range(15, 25):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 590, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(15, 25):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 570, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(31, 41):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 590, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(31, 41):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 570, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 9):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 90, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(58, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 480, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(58, 64):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 580, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(14, 34):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 330, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(45, 55):
            plataforma_direita = Bloco(i * self.tamanho_bloco, 330, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_direita.rect)
            self.sprite_objetos.add(plataforma_direita)
        for i in range(15, 25):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 90, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(31, 41):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 90, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)
        for i in range(0, 6):
            plataforma_esquerda = Bloco(i * self.tamanho_bloco, 540, self.tamanho_bloco)
            self.lista_objetos.append(plataforma_esquerda.rect)
            self.sprite_objetos.add(plataforma_esquerda)

        # adiciona as águas na tela
        agua_draco = Água_Draco(2 * self.largura_agua, 680, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco.rect)
        self.sprite_aguas.add(agua_draco)

        agua_draco2 = Água_Draco(4 * self.largura_agua, 570, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco2.rect)
        self.sprite_aguas.add(agua_draco2)

        agua_draco3 = Água_Draco(4 * self.largura_agua, 170, self.largura_agua, self.altura_agua)
        self.lista_agua_draco.append(agua_draco3.rect)
        self.sprite_aguas.add(agua_draco3)

        agua_harry1 = Água_Harry(4 * self.largura_agua, 680, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry1.rect)
        self.sprite_aguas.add(agua_harry1)

        agua_harry2 = Água_Harry(2 * self.largura_agua, 570, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry2.rect)
        self.sprite_aguas.add(agua_harry2)

        agua_harry3 = Água_Harry(2 * self.largura_agua, 170, self.largura_agua, self.altura_agua)
        self.lista_agua_harry.append(agua_harry3.rect)
        self.sprite_aguas.add(agua_harry3)

        # adiciona as horcruxes na tela
        taca = Horcrux(700, 380, 40, 40, 'imagens/taca.png')
        self.sprite_horcrux_draco.add(taca)

        diadema = Horcrux(1190, 420, 40, 40, 'imagens/diadema.jpg')
        self.sprite_horcrux_harry.add(diadema)

        nagini = Horcrux(30, 30, 40, 40, 'imagens/nagini.jpg')
        self.sprite_nagini.add(nagini)

        # adiciona os diamantes na tela 
        diamante_dm1 = Diamante(50, 500, 25, 25, 'imagens/diamante_draco.png')
        self.sprite_diamante_draco.add(diamante_dm1)

        diamante_hp1 = Diamante(450, 300, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp1)

        diamante_hp2 = Diamante(700, 50, 25, 25, 'imagens/diamante_harry.png')
        self.sprite_diamante_harry.add(diamante_hp2)
        
    def checa_agua(self):
        """
        Método que verifica a colisão de algum personagem do jogo com as águas do mesmo. 
        Caso Harry caia na água verde, ou Draco na água vermelha ou qualquer um dos dois na água preta, a função retorna -1.

        Returns: 
            -1 quando há a colisão com a água. 
        """
        # verifica se colidiu com qualquer água do jogo
        for agua_harry in self.lista_agua_harry:
            if self.draco.rect.colliderect(agua_harry):
                return -1

        for agua_draco in self.lista_agua_draco:
            if self.harry.rect.colliderect(agua_draco):
                return -1

        for agua_toxica in self.lista_agua_toxica:
            if self.harry.rect.colliderect(agua_toxica) or self.draco.rect.colliderect(agua_toxica):
                return -1
            
    def checa_horcruxes(self):
        """
        Método que verifica a colisão de algum personagem do jogo com as horcruxes, para assim poder pegá-las. 
        Harry e Draco tem as suas respectivas horcruxes.
        """
        # permite pegar as horcruxes da tela
        for horcrux_draco in self.sprite_horcrux_draco:
            if self.draco.rect.colliderect(horcrux_draco):
                self.conta_horcruxes += 1
                horcrux_draco.kill()

        for horcrux_harry in self.sprite_horcrux_harry:
            if self.harry.rect.colliderect(horcrux_harry):
                self.conta_horcruxes += 1  
                horcrux_harry.kill()

        if self.conta_diamantes_harry == 2:
            for nagini in self.sprite_nagini:
                if self.harry.rect.colliderect(nagini):
                    self.conta_horcruxes += 1
                    nagini.kill()

    def checa_diamantes(self):
        """
        Método que verifica a colisão de algum personagem do jogo com os diamantes, para assim poder pegá-los. 
        Harry e Draco tem os seus respectivos diamantes.
        """
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

    def checa_porta(self):
        """
        Método que verifica a colisão dos personagens com a porta de saída da sala. 
        Só é ativado, caso os personagens peguem todas as horcruxes da tela. 

        Returns: 
            -1 quando há a colisão com a porta. 
        """
        # verifica se colidiu com a porta
        if self.conta_diamantes == 3 and self.conta_horcruxes == 3:
            if self.draco.rect.colliderect(self.porta.rect) and self.harry.rect.colliderect(self.porta.rect):
                return -1
        
    def desenha(self, window):
        """
        Método que chama as funções de desenhar das sprites, assim como desenha tudo que precisa na tela. 
        """
        # desenha tudo na tela 
        window.fill((0, 0, 0))

        for imagem in self.lista_imagem_fundo:
            window.blit(self.fundo, imagem)

        self.sprite_personagens.draw(window)
        self.sprite_objetos.draw(window)
        self.sprite_aguas.draw(window)
        self.sprite_horcrux_draco.draw(window)
        self.sprite_horcrux_harry.draw(window)
        self.sprite_diamante_draco.draw(window)
        self.sprite_diamante_harry.draw(window)
        self.sprite_nagini.draw(window)

    def atualiza_estado(self):
        """
        Método que atualiza o estado do jogo e retorna a próxima tela que deve ser desenhada.
        Checa se o jogador caiu na água, se coletou todas as Horcruxes e todos os diamantes e se chegou à porta de saída.
        Permite que o jogador se mova com as teclas de seta para o Harry e 'a' e 'd' para Draco.
        Ao pressionar 'w' ou 'up', o jogador salta com Draco e Harry, respectivamente.

        Returns:
            'TELA_GAMEOVER' se a função checa_agua retornar -1
            'TELA_JOGO3' se a função checa_porta retornar -1
            True caso o contrário, mantendo o jogo rodando dentro do loop principal 
        """
        # retorna qual tela deve ser desenhada em seguida e permite o jogador se mover 
        self.checa_agua()
        self.checa_diamantes()
        self.checa_horcruxes()
        self.checa_porta()

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
        
        if self.checa_agua() == -1: 
            return 'TELA_GAMEOVER'
        if self.checa_porta() == -1:
            return 'TELA_JOGO3'
        
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