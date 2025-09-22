
'''MENSAGEM PARA A NICOLLY: para mudar sprites, mude as origens de variáveis que usam "pygame.image.load".
    Para os retângulos usados para colisão, mude os que terminam com "Rect".
    Os retângulos dos inimigos estão na linha 126 e 128.
    Se você quiser aumentar o tamanho de um sprite, crie uma variável nova terminando com "BIG" e use pygame.transform.scale
    E é isso! Sobre o vídeo no Youtube, eu parei nas 2:47:26.'''
    
# Bibliotecas
import pygame
from sys import exit

#Usado para colocar inimigos aleatoriamente na tela
from random import randint

#Pontuação
def display_score():
    current_time = int (pygame.time.get_ticks() / 1000) - start_time
    score_surf = fonte_texto.render(f'Tempo: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (1130,57))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
    screen.blit(score_surf, score_rect)
    return current_time

#LOOP de inimigos
def obstacle_movement(lista_inimigos):
    if lista_inimigos:
        for lista_inimigos_rect in lista_inimigos:
            lista_inimigos_rect.x -= 6
            
            if lista_inimigos_rect.bottom == 600:
                screen.blit(snail_big, lista_inimigos_rect)
            else:
                screen.blit(antena_big, lista_inimigos_rect)
        
        lista_inimigos = [obstacle for obstacle in lista_inimigos if obstacle.x > -150]

        return lista_inimigos
    else:
        return []
    

#Colisões de inimigos em geral
def collisions(astro,obstacles):
    if obstacles:
        for lista_inimigos_rect in obstacles:
            if astro.colliderect(lista_inimigos_rect): return False
    return True

#Janela
pygame.init()
screen = pygame.display.set_mode((1300,750))
pygame.display.set_caption('Samba na Lua')
clock = pygame.time.Clock()
fonte_texto = pygame.font.Font('Pygame-main\\font\\ari-w9500-display.ttf', 50)
jogo_ativo = False
start_time = 0
score = 0

#Imagens e textos usados
#Para colocar imagens, basta coloca-las dentro da pasta do jogo.
#Usamos convert ou convert.alpha() para trabalhar melhor com as imagens no pygame, além de melhorar o desempenho do jogo.
space_surf = pygame.image.load('Pygame-main\sprites\space.png').convert()
ground_surf = pygame.image.load('Pygame-main\graphics\ground.png').convert()
#text_score_surf = fonte_texto.render('Teste.', False, (64,64,64))
astro_surf = pygame.image.load('Pygame-main\\sprites\\spr_1.png').convert_alpha()
planeta = pygame.image.load('Pygame-main\sprites\Objetos\planeta.png').convert_alpha()

#Imagens rescalionadas
astro_big = pygame.transform.scale(astro_surf, (98,135))
space_big = pygame.transform.scale(space_surf, (1300,650))
ground_big = pygame.transform.scale(ground_surf, (1300,200))
planeta= pygame.transform.scale(planeta, (230,230))

#Posições e colisões
astro_rect = astro_big.get_rect(midbottom = (170,600))
planeta_rect = planeta.get_rect(center = (630,370))


nome_jogo = fonte_texto.render('Samba na Lua', False, (111,196,169))
nome_jogo_rect = nome_jogo.get_rect(center = (630,115))
mensagem_jogo = fonte_texto.render('Pressione Espaço para começar.', False, (111,196,169))
mensagem_jogo_rect = mensagem_jogo.get_rect(center = (650,620))

#Inimigos
snail_surf = pygame.image.load('Pygame-main\graphics\snail\snail1.png').convert_alpha()
snail_big = pygame.transform.scale(snail_surf, (120,69))
antena_surf = pygame.image.load('Pygame-main\\sprites\Objetos\\antena.png').convert_alpha()
antena_big = pygame.transform.scale(antena_surf, (130,136))
lista_inimigos_rect = []

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

#Gravidade
astro_grav = 0

#LOOP para manter tudo funcionando.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if jogo_ativo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if astro_rect.collidepoint(event.pos) and astro_rect.bottom >=600:
                    astro_grav = -21

            #Comandos para teste de mouse
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse down')
            if event.type == pygame.MOUSEBUTTONUP:
                print('Mouse up')'''
            
            #Controles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and astro_rect.bottom >=600:
                    astro_grav = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                start_time = int(pygame.time.get_ticks() / 1000)
                lista_inimigos_rect.clear()

        if event.type == obstacle_timer and jogo_ativo:
            if randint(0,2):
                lista_inimigos_rect.append(snail_big.get_rect(bottomright = (randint(1400,1600),600)))
            else:
                lista_inimigos_rect.append(antena_big.get_rect(midbottom = (randint(1400,1600),400)))

    #Diferença de jogo "ativo" para game over.
    if jogo_ativo:

        #Camadas
        screen.blit(space_big,(0,0))
        screen.blit(ground_big,(0,600))

        #Comandos para desenhar figuras geométricas na tela.
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100)) - Para criar círculos ou elípses.
        #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) - para uma linha apontar para a posição do mouse
        
        score = display_score() #Associando a variável score à display_score()

        # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
        # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

        #Astronauta
        astro_grav +=0.6
        astro_rect.y += astro_grav
        if astro_rect.bottom >=600:
            astro_rect.bottom = 600
            astro_grav = 0

        screen.blit(astro_big, astro_rect)

        
        #Movimento dos inimigos
        lista_inimigos_rect = obstacle_movement(lista_inimigos_rect)
        
        jogo_ativo = collisions(astro_rect, lista_inimigos_rect)
        
    #Display de tudo na tela
    else:
        screen.fill((94,129,162))
        screen.blit(planeta, planeta_rect)
        screen.blit(nome_jogo, nome_jogo_rect)
        score_message = fonte_texto.render(f'Sua pontuação: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (650,200))

        #Palavras diferentes ao começar o jogo pela primeira vez.        
        if score == 0:
            screen.blit(mensagem_jogo, mensagem_jogo_rect)
        else:
            screen.blit(score_message,score_message_rect)

    #Teste de colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if astro_rect.colliderect(snail_rect):
        print('Collision')"""
    #pygame.draw.rect(screen, (255,0,0), astro_rect, 2)
    #pygame.draw.rect(screen, (255,0,0), snail_rect, 2)
    """mouse_pos = pygame.mouse.get_pos()
    if astro_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""
    '''if snail_rect.colliderect(astro_rect):
            jogo_ativo = False'''

    pygame.display.update()
    clock.tick(60)