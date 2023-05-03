import pygame

class Tela_gameover():
    """Representa a tela de Game Over do jogo.

    Atributos:
        fundo (pygame.Surface): imagem de fundo da tela de game over.
        gameover (pygame.Surface): texto 'GAME OVER' da tela.
        fonte_texto (pygame.font.Font): fonte para o texto da tela.
        menu (pygame.Surface): opção 'Voltar para o Menu' da tela.
        menu_rect (pygame.Rect): retângulo para a opção 'Voltar para o Menu'.

    Métodos:
        desenha(window): desenha os elementos da tela na janela passada como parâmetro.
        atualiza_estado(): atualiza o estado da tela de acordo com as interações do usuário.
    """
    def __init__(self):
        """Inicializa os elementos da tela de Game Over."""
        imagem_fundo = pygame.image.load('imagens/fundo_gameover.png')
        self.fundo = pygame.transform.scale(imagem_fundo, (1280, 720))

        fonte = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        self.gameover = fonte.render('GAME OVER', True, (211, 177, 110))

        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 25)
        self.menu = self.fonte_texto.render('Voltar para o Menu', True, (174, 139, 71))

        self.menu_rect = self.menu.get_rect(center=(1280/2, 660))

    def desenha(self, window):
        """Desenha os elementos da tela na janela passada como parâmetro.

        Argumentos necessários:
            window (pygame.Surface): janela onde os elementos serão desenhados.
        """
        # Desenha a imagem de fundo na posição (0, 0) da janela.
        window.blit(self.fundo, (0, 0))

        # Desenha o texto 'GAME OVER' na posição (350, 130) da janela.
        window.blit(self.gameover, (350, 130))

        # Desenha um retângulo preto na posição (250, 340) da janela.
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(250, 340, 790, 180))

        # Renderiza e desenha o texto explicativo sobre o Game Over.
        dd = self.fonte_texto.render('Oh, no!! Harry Potter e Draco Malfoy não conseguiram', True, (211, 177, 110))
        window.blit(dd, (280, 370))
        dd2 = self.fonte_texto.render('escapar da Mansão Malfoy e destruir as horcrux. Ago-', True, (211, 177, 110))
        window.blit(dd2, (280, 400))
        dd3 = self.fonte_texto.render('ra, Voldemort ganhou a guerra. Hogwarts e seus  ami-', True, (211, 177, 110))
        window.blit(dd3, (280, 430))
        dd4 = self.fonte_texto.render('gos correm grande perigo!', True, (211, 177, 110))
        window.blit(dd4, (280, 460))

        # Desenha o botão para voltar ao menu principal
        window.blit(self.menu, self.menu_rect)

    def atualiza_estado(self):
        """
        Atualiza o estado da tela de Game Over com base nos eventos do Pygame.

        Returns:
            str or int: Se o jogador clicou no botão "Voltar para o Menu", retorna "TELA_INICIAL".
                    Se o jogador clicou no botão de fechar a janela, retorna -1.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_rect.collidepoint(event.pos):
                    return 'TELA_INICIAL'