import pygame

class Tela_gameover():
    def __init__(self):
        imagem_fundo = pygame.image.load('imagens/fundo_gameover.png')
        self.fundo = pygame.transform.scale(imagem_fundo, (1280, 720))

        fonte = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 100)
        self.gameover = fonte.render('GAME OVER', True, (211, 177, 110))

        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 25)

        self.menu = self.fonte_texto.render('Voltar para o Menu', True, (174, 139, 71))
        self.menu_rect = self.menu.get_rect(center=(1280/2, 660))

    def desenha(self, window): 

        window.blit(self.fundo, (0, 0))
        window.blit(self.gameover, (350, 130))
        
        pygame.draw.rect(window, (0, 0, 0), pygame.Rect(250, 340, 790, 180))

        dd = self.fonte_texto.render('Oh, no!! Harry Potter e Draco Malfoy não conseguiram', True, (211, 177, 110))
        window.blit(dd, (280, 370))
        dd2 = self.fonte_texto.render('escapar da Mansão Malfoy e destruir as horcrux. Ago-', True, (211, 177, 110))
        window.blit(dd2, (280, 400))
        dd3 = self.fonte_texto.render('ra, Voldemort ganhou a guerra. Hogwarts e seus  ami-', True, (211, 177, 110))
        window.blit(dd3, (280, 430))
        dd4 = self.fonte_texto.render('gos correm grande perigo!', True, (211, 177, 110))
        window.blit(dd4, (280, 460))

        window.blit(self.menu, self.menu_rect)

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_rect.collidepoint(event.pos):
                    return 'TELA_INICIAL'