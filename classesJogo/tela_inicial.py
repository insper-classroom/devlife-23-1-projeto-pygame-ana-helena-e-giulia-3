import pygame

class Tela_inicial():
    """
    Classe responsável pela criação da tela inicial do jogo.
    """
    def __init__(self):
        """
        Inicializa a tela inicial do jogo.

        Carrega a imagem do fundo, o título do jogo e os botões "Play" e "Instruções".
        """
        imagem_fundo = pygame.image.load('imagens/fundo_inicio.png')
        self.fundo = pygame.transform.scale(imagem_fundo, (1280, 720))

        fonte = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        self.titulo_jogo = fonte.render('Hogwarts Scape', True, (211, 177, 110))
        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 60)

        self.botao_rect_play = pygame.Rect(515, 315, 250, 80)

        self.play = self.fonte_texto.render('Play', True, (174, 139, 71))
        self.play_rect = self.play.get_rect(center=(1280/2, 720/2))

        self.botao_rect_instruc = pygame.Rect(445, 455, 390, 80)

        self.instrucoes = self.fonte_texto.render('Instruções', True, (174, 139, 71))
        self.instrucoes_rect = self.instrucoes.get_rect(center=(1280/2, 500))

    def desenha(self, window):
        """
        Desenha a tela inicial do jogo na janela especificada.

        Argumentos necessários:
            window (pygame.Surface): janela onde será desenhada a tela de início.
        """
        window.fill((0, 0, 0))

        window.blit(self.fundo, (0, 0))
        window.blit(self.titulo_jogo, (220, 130))

        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_play)

        window.blit(self.play, self.play_rect)

        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_instruc)

        window.blit(self.instrucoes, self.instrucoes_rect)

    def atualiza_estado(self):
        """
        Atualiza o estado da tela a partir dos eventos do Pygame.

        Returns:
            -1 se o usuário clicar no botão de fechar a janela.
            'TELA_JOGO' se o usuário clicar no botão "Play".
            'TELA_HARRY' se o usuário clicar no botão "Instruções".
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.botao_rect_play.collidepoint(event.pos):
                    return 'TELA_JOGO'
                elif self.botao_rect_instruc.collidepoint(event.pos):
                    return 'TELA_HARRY'