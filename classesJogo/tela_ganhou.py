import pygame

class Tela_ganhou():
    """
    Represena a tela de vitória do jogo.

    Atributos:
        fundo: imagem de fundo da tela de vitória
        vitoria: objeto que armazena o texto "VITÓRIA!" a ser exibido na tela
        fonte_texto: objeto que armazena a fonte a ser utilizada para o texto
        menu: objeto que armazena o texto "Jogar novamente" a ser exibido no botão
        menu_rect: objeto que armazena as coordenadas do retângulo do botão "Jogar novamente"

    Métodos:
        desenha: desenha os elementos da tela de vitória na janela do jogo
        atualiza_estado: atualiza o estado da tela de acordo com os eventos do usuário
    """
    def __init__(self):
        """
        Inicializa a classe com a imagem de fundo, o texto de "vitória" e o botão para jogar novamente.
        """
        imagem_fundo = pygame.image.load('imagens/fundo_ganhou.jpg')
        self.fundo = pygame.transform.scale(imagem_fundo, (1280, 720))

        fonte = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 90)
        self.vitoria = fonte.render('VITÓRIA!', True, (211, 177, 110))

        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 25)

        self.menu = self.fonte_texto.render('Jogar novamente', True, (211, 177, 110))
        self.menu_rect = self.menu.get_rect(center=(1280/2, 660))

    def desenha(self, window):
        """
        Desenha a tela de vitória com os textos e imagens correspondentes.

        Argumentos necessários:
            window: Objeto pygame da janela onde será desenhada a tela de vitória.
        """
        window.blit(self.fundo, (0, 0))
        window.blit(self.vitoria, (450, 130))
        
        pygame.draw.circle(window, (0, 0, 0), (960, 300), 160)
        pygame.draw.circle(window, (0, 0, 0), (1100, 435), 80)
        pygame.draw.rect(window, (0, 0, 0), (510, 633, 260, 50))

        dd = self.fonte_texto.render('Parabéns!! Harry', True, (211, 177, 110))
        window.blit(dd, (850, 180))
        dd2 = self.fonte_texto.render('Potter e Draco Mal-', True, (211, 177, 110))
        window.blit(dd2, (830, 210))
        dd3 = self.fonte_texto.render('foy uniram suas forças,', True, (211, 177, 110))
        window.blit(dd3, (810, 240))
        dd4 = self.fonte_texto.render('coletaram e destruíram', True, (211, 177, 110))
        window.blit(dd4, (800, 270))
        dd5 = self.fonte_texto.render('todas as horcrux e con-', True, (211, 177, 110))
        window.blit(dd5, (800, 300))
        dd6 = self.fonte_texto.render('seguiram derrotar', True, (211, 177, 110))
        window.blit(dd6, (810, 330))
        dd7 = self.fonte_texto.render('LORD VOLDEMORT.', True, (211, 177, 110))
        window.blit(dd7, (830, 360))
        dd8 = self.fonte_texto.render('Hora', True, (211, 177, 110))
        window.blit(dd8, (1070, 390))
        dd8 = self.fonte_texto.render('de', True, (211, 177, 110))
        window.blit(dd8, (1090, 420))
        dd8 = self.fonte_texto.render('celebrar', True, (211, 177, 110))
        window.blit(dd8, (1040, 450))

        window.blit(self.menu, self.menu_rect)

    def atualiza_estado(self):
        """
        Atualiza o estado da tela de vitória de acordo com as interações do usuário com o botão de jogar novamente.

        Returns:
            Retorna o estado da tela inicial caso o usuário clique no botão de jogar novamente, ou -1 caso clique no
            botão de fechar a janela.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_rect.collidepoint(event.pos):
                    return 'TELA_INICIAL'