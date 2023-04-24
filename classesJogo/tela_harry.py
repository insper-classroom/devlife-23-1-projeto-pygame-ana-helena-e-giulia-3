import pygame

class Tela_harry():
    def __init__(self):
        self.fundo = pygame.image.load('imagens/fundo_rpg.png')

        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 30)

        self.prosseguir = self.fonte_texto.render('Prosseguir', True, (174, 139, 71))
        self.prosseguir_rect = self.prosseguir.get_rect(center=(1180, 700))

        
        harry_img = pygame.image.load('imagens/harry_frente.png')
        self.harry_maior = pygame.transform.scale(harry_img, (700, 700))

    def desenha(self, window):
        window.fill((0, 0, 0))

        window.blit(self.fundo, (0, 0))

        window.blit(self.prosseguir, self.prosseguir_rect)

        window.blit(self.harry_maior, (-300, 30))

        t1 = self.fonte_texto.render('Olá! Eu sou o', True, (0, 0, 0))
        window.blit(t1, (500, 120))
        t2 = self.fonte_texto.render('Harry Potter! Estou', True, (0, 0, 0))
        window.blit(t2, (470, 160))
        t3 = self.fonte_texto.render('preso no porão da', True, (0, 0, 0))
        window.blit(t3, (470, 200))
        t4 = self.fonte_texto.render('Malfoy Manor e', True, (0, 0, 0))
        window.blit(t4, (470, 240))
        t5 = self.fonte_texto.render('preciso da sua ajuda!', True, (0, 0, 0))
        window.blit(t5, (460, 280))

    def verifica_colisao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.prosseguir_rect.collidepoint(event.pos):
                    return 'TELA_INSTRUCOES'