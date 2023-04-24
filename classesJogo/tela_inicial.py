import pygame

class Tela_inicial():
    def __init__(self):
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
        window.fill((0, 0, 0))

        window.blit(self.fundo, (0, 0))
        window.blit(self.titulo_jogo, (220, 130))

        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_play)

        window.blit(self.play, self.play_rect)

        pygame.draw.rect(window, (240, 229, 198), self.botao_rect_instruc)

        window.blit(self.instrucoes, self.instrucoes_rect)

    def verifica_colisao(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.botao_rect_play.collidepoint(event.pos):
                    return 'TELA_JOGO'
                elif self.botao_rect_instruc.collidepoint(event.pos):
                    return 'TELA_HARRY'