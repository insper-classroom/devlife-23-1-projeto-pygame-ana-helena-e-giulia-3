import pygame

class Tela_instrucoes():
    def __init__(self):
        self.fundo = pygame.image.load('imagens/fundo_instrucoes.png')

        fonte_titulo = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 70)
        self.fonte_texto = pygame.font.Font('docs/font/WizardWorldSimplified-Kxr7.ttf', 30)

        self.instrucoes = fonte_titulo.render('Instruções', True, (174, 139, 71))

        self.jogar = self.fonte_texto.render('Jogar', True, (174, 139, 71))
        self.jogar_rect = self.jogar.get_rect(center=(1195, 700))

    def desenha(self, window):
        window.fill((0, 0, 0))

        window.blit(self.fundo, (0, 0))

        window.blit(self.instrucoes, (445, 120))

        i1 = self.fonte_texto.render('- Use aswd para movimentar Draco Malfoy', True, (211, 177, 110))
        window.blit(i1, (280, 220))
        i2 = self.fonte_texto.render('- Use as setas para movimentar Harry Potter', True, (211, 177, 110))
        window.blit(i2, (280, 270)) 
        i3 = self.fonte_texto.render('- Colete as horcrux para ganhar pontos e', True, (211, 177, 110))
        window.blit(i3, (280, 320)) 
        i3c = self.fonte_texto.render('conseguir escapar da sala!', True, (211, 177, 110))
        window.blit(i3c, (295, 355)) 
        i4 = self.fonte_texto.render('- O objetivo do jogo é salvar Harry Potter e', True, (211, 177, 110))
        window.blit(i4, (280, 405))
        i4c = self.fonte_texto.render('Draco Malfoy da Malfoy Manor', True, (211, 177, 110))
        window.blit(i4c, (295, 440)) 
        i5 = self.fonte_texto.render('- Se Draco Malfoy cair no líquido vermelho,', True, (211, 177, 110))
        window.blit(i5, (280, 490))
        i5c = self.fonte_texto.render('ele morre, assim como Harry Potter morre', True, (211, 177, 110))
        window.blit(i5c, (295, 525)) 
        i5cc = self.fonte_texto.render('ao cair no líquido azul', True, (211, 177, 110))
        window.blit(i5cc, (295, 560))

        window.blit(self.jogar, self.jogar_rect)

    def atualiza_estado(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.jogar_rect.collidepoint(event.pos):
                    return 'TELA_JOGO'