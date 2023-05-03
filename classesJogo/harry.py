import pygame

class Harry(pygame.sprite.Sprite):
    """
    Classe que representa o personagem Harry no jogo.
    """
    def __init__(self, lista_blocos, x, y):
        """
        Construtor da classe Harry.

        Argumentos necessários:
            lista_blocos (list): lista de objetos que representam os blocos na tela.
            x (int): posição horizontal inicial do personagem.
            y (int): posição vertical inicial do personagem.
        """
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('imagens/harry_lado_direito.png'), (50, 60))
        self.rect = self.image.get_rect()
        # posição inicial do harry
        self.lista_blocos = lista_blocos
        self.rect.x = x
        self.rect.y = y
        self.GRAVIDADE = 2
        self.jump = 80
        self.state = {
            'pulando': False,
            'caindo': True
        }

    def movimenta_esquerda(self):
        """
        Método que move o personagem para a esquerda na tela.
        """
        self.rect.x -= 3

         # verifica colisão com parede esquerda
        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.x += 3
    
    def movimenta_direita(self):
        """
        Método que move o personagem para a direita na tela.
        """
        self.rect.x += 3

        # verifica colisão com parede direita
        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.x -= 3

    def update(self):
        """
        Método que atualiza a posição do personagem na tela.
        """
        # verifica se o harry está pulando e o limita dentro da tela 
        if self.state['pulando'] == True:
            self.rect.y -= self.jump
        if self.state['caindo'] == True:
            self.rect.y += self.GRAVIDADE
        self.state['caindo'] = True
        self.state['pulando'] = False

        if self.rect.y < 20:
            self.rect.y = 20 + self.jump

        if self.rect.collidelist(self.lista_blocos) != -1:
            self.rect.y -= self.GRAVIDADE
            self.state['caindo'] = False