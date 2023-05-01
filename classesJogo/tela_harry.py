import pygame

class Tela_harry():
    def __init__(self):
        fundo_img = pygame.image.load('imagens/fundo_rpg.png')
        self.fundo = pygame.transform.scale(fundo_img, (1280, 720))

        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 25)

        self.prosseguir = self.fonte_texto.render('Prosseguir', True, (174, 139, 71))
        self.prosseguir_rect = self.prosseguir.get_rect(center=(1180, 700))
        
        harry_img = pygame.image.load('imagens/harry_frente.png')
        self.harry_maior = pygame.transform.scale(harry_img, (700, 700))

        draco_img = pygame.image.load('imagens/draco_frente.png')
        self.draco = pygame.transform.scale(draco_img, (700, 700))

    def desenha(self, window):

        window.blit(self.fundo, (0, 0))

        window.blit(self.prosseguir, self.prosseguir_rect)

        window.blit(self.harry_maior, (-320, 30))
        window.blit(self.draco, (770, 30))

        t1 = self.fonte_texto.render('Olá! Eu sou o', True, (0, 0, 0))
        window.blit(t1, (300, 160))
        t2 = self.fonte_texto.render('Harry Potter! Estou', True, (0, 0, 0))
        window.blit(t2, (280, 190))
        t3 = self.fonte_texto.render('preso no porão da', True, (0, 0, 0))
        window.blit(t3, (280, 220))
        t4 = self.fonte_texto.render('Mansão Malfoy e', True, (0, 0, 0))
        window.blit(t4, (280, 250))
        t5 = self.fonte_texto.render('preciso da sua ajuda!', True, (0, 0, 0))
        window.blit(t5, (270, 280))

        t6 = self.fonte_texto.render('Vamos, Potter!', True, (0, 0, 0))
        window.blit(t6, (640, 230))
        t7 = self.fonte_texto.render('Não temos tempo para', True, (0, 0, 0))
        window.blit(t7, (585, 260))
        t8 = self.fonte_texto.render('tais tolices. Agora, me', True, (0, 0, 0))
        window.blit(t8, (585, 290))
        t9 = self.fonte_texto.render('siga se quiser sair', True, (0, 0, 0))
        window.blit(t9, (610, 320))
        t9 = self.fonte_texto.render('vivo daqui.', True, (0, 0, 0))
        window.blit(t9, (630, 350))

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.prosseguir_rect.collidepoint(event.pos):
                    return 'TELA_INSTRUCOES'