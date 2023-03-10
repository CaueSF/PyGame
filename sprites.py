import pygame
import random

class Input(pygame.sprite.Sprite):
    def __init__(self, dicionario_de_arquivos):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # TODO 1: Defina as informações abaixo
        # self.image = # Carregue a imagem do input disponível em dicionario_de_arquivos
        self.image = dicionario_de_arquivos['input']
        self.rect = self.image.get_rect()
        # self.rect.x = # define uma posição para teste (Depois vamos tornar esta posição aleatória)
        self.rect.x = random.randint(0, (900 - 223))
        # self.rect.y =# defina uma posição para teste
        self.rect.y = random.randint(-200, -76)
        # self.speedy = # aqui defina uma velocidade em que o input cairá
        self.speedy = 3

        self.lista_palavras = ['trompete', 'dessoft', 'cherimoia', 'refrigerante', 'pitoresco', 'concatenar', 'holística', 'epítome', 'sazonal', 'exaurir']
        self.palavra = random.choice(self.lista_palavras)
    def sorteia_palavra(self):
        self.palavra = random.choice(self.lista_palavras)
 

    def update(self):
        self.rect.y += 3
        # Atualização da posição da nave
        #Aqui você deve definir a lógica para fazer a caixa cair


class Botao(pygame.sprite.Sprite):
    def __init__(self, dicionario_de_arquivos, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.dicionario_de_arquivos = dicionario_de_arquivos
        self.image = dicionario_de_arquivos['btn'] # assets é um dicionário de imagens, sons e fonts
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.dicionario_de_arquivos['btn_hover']
        else:
            self.image = self.dicionario_de_arquivos['btn']
