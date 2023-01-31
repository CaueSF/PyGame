import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
from sprites import Input

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING
    lista_de_imagens = pygame.sprite.Group()
    input = Input(dicionario_de_arquivos)
    y = input.rect.y + 8
    lista_de_imagens.add(input)
    palavra = ''
    pontos = 0

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                palavra += event.unicode
            if event.type == pygame.QUIT:
                state = DONE
        
        if y > 700:
            if palavra != input.palavra:
                state = DONE
            if palavra == input.palavra:
                pontos += 1
                print(pontos)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        lista_de_imagens.update()
        lista_de_imagens.draw(window)
        fonte = pygame.font.SysFont(None, 30)
        texto = fonte.render(input.palavra, True, (255, 255, 255))
        print(palavra)
        resposta = fonte.render(palavra, True, (0, 0, 0))
        # event.unicode = texto.get_rect()
        # texto += event.unicode
        x = input.rect.x + 85
        y = input.rect.y + 8
        x_resposta = input.rect.x + 60
        y_resposta = input.rect.y + 45
        window.blit(texto, (x, y))
        window.blit(resposta, (x_resposta, y_resposta))

        pygame.display.update()  # Mostra o novo frame para o jogador


    return state
