# -*- coding: utf-8 -*-

# Bibliotecas
import pygame
from sys import exit

#Pontuação
def display_score():
    current_time = int (pygame.time.get_ticks() / 1000) - start_time
    score_surf = fonte_texto.render(f'Tempo: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)

#Janela
pygame.init()
screen = pygame.display.set_mode((1300,750))
pygame.display.set_caption('Samba na Lua')
clock = pygame.time.Clock()
fonte_texto = pygame.font.Font('Pygame-main\\font\\ari-w9500-display.ttf', 55)
jogo_ativo = False
start_time = 0


#Imagens e textos usados
#Para colocar imagens, basta coloca-las dentro da pasta do jogo.
#Usamos convert para trabalhar melhor com as imagens no pygame, além de melhorar o desempenho do jogo.
space_surf = pygame.image.load('Pygame-main\sprites\space.png').convert()
ground_surf = pygame.image.load('Pygame-main\graphics\ground.png').convert()
snail_surf = pygame.image.load('Pygame-main\graphics\snail\snail1.png').convert_alpha()
#text_score_surf = fonte_texto.render('Teste.', False, (64,64,64))
astro_surf = pygame.image.load('Pygame-main\\sprites\\spr_1.png').convert_alpha()
planeta = pygame.image.load('Pygame-main\sprites\Objetos\planeta.png').convert_alpha()

#Imagens rescalionadas
astro_big = pygame.transform.scale(astro_surf, (98,135))
space_big = pygame.transform.scale(space_surf, (1300,650))
ground_big = pygame.transform.scale(ground_surf, (1300,200))
snail_big = pygame.transform.scale(snail_surf, (100,60))
planeta= pygame.transform.scale(planeta, (230,230))

#Posições e colisões
snail_x_pos = 600
#score_rect = text_score_surf.get_rect(center = (650, 50))
snail_rect = snail_big.get_rect(bottomright = (100,600))
astro_rect = astro_big.get_rect(midbottom = (300,600))
planeta_rect = planeta.get_rect(center = (630,370))

nome_jogo = fonte_texto.render('Samba na Lua', False, (111,196,169))
nome_jogo_rect = nome_jogo.get_rect(center = (630,115))
mensagem_jogo = fonte_texto.render('Pressione Espaço para começar.', False, (111,196,169))
mensagem_jogo_rect = mensagem_jogo.get_rect(center = (650,620))

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
                    astro_grav = -19
            '''if event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse down')
            if event.type == pygame.MOUSEBUTTONUP:
                print('Mouse up')'''
            #Controles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and astro_rect.bottom >=600:
                    astro_grav = -19
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                snail_rect.left = 1000
                start_time = int(pygame.time.get_ticks() / 1000)

    if jogo_ativo:

        #Camadas
        screen.blit(space_big,(0,0))
        screen.blit(ground_big,(0,600))
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100)) - Para criar círculos ou elípses.
        #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) - para uma linha apontar para a posição do mouse
        
        #screen.blit(text_score_surf,(score_rect))
        display_score()
        """snail_x_pos-=4
        if snail_x_pos <-100: snail_x_pos = 800"""
        snail_rect.x -= 10
        if snail_rect.right <=0: snail_rect.left = 1300

        screen.blit(snail_big,snail_rect)
        # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
        # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

        #Astronauta
        astro_grav +=0.5
        astro_rect.y += astro_grav
        if astro_rect.bottom >=600:
            astro_rect.bottom = 600
        screen.blit(astro_big, astro_rect)
        if snail_rect.colliderect(astro_rect):
            jogo_ativo = False
    #Menu
    else:
        screen.fill((94,129,162))
        screen.blit(planeta, planeta_rect)
        screen.blit(nome_jogo, nome_jogo_rect)
        screen.blit(mensagem_jogo, mensagem_jogo_rect)

    #Teste de colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if astro_rect.colliderect(snail_rect):
        print('Collision')"""
    pygame.draw.rect(screen, (255,0,0), astro_rect, 2)
    pygame.draw.rect(screen, (255,0,0), snail_rect, 2)
    """mouse_pos = pygame.mouse.get_pos()
    if astro_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""

    #Tecla de atalho para sair
    

    pygame.display.update()
    clock.tick(60)