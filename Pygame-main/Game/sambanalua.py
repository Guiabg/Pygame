# Bibliotecas
import pygame

from sys import exit
#Janela
pygame.init()
screen = pygame.display.set_mode((1300,750))
pygame.display.set_caption('Samba na Lua')
clock = pygame.time.Clock()
fonte_teste = pygame.font.Font('Pygame-main\\font\\Pixeltype.ttf', 50)


#Imagens e textos usados
#Para colocar imagens, basta coloca-las dentro da pasta do jogo.
#Usamos convert para trabalhar melhor com as imagens no pygame, além de melhorar o desempenho do jogo.
space_surf = pygame.image.load('Pygame-main\sprites\space.png').convert()
ground_surf = pygame.image.load('Pygame-main\graphics\ground.png').convert()
snail_surf = pygame.image.load('Pygame-main\graphics\snail\snail1.png').convert_alpha()
text_score_surf = fonte_teste.render('Teste.', False, (64,64,64))
astro_surf = pygame.image.load('Pygame-main\\sprites\\spr_1.png').convert_alpha()

#Imagens rescalionadas
astro_big = pygame.transform.scale(astro_surf, (90,135)).convert_alpha()
space_big = pygame.transform.scale(space_surf, (1300,600)).convert()
ground_big = pygame.transform.scale(ground_surf, (1300,200)).convert()
snail_big = pygame.transform.scale(snail_surf, (100,60)).convert_alpha()

#Posições e colisões
snail_x_pos = 600
score_rect = text_score_surf.get_rect(center = (650, 50))
snail_rect = snail_big.get_rect(bottomright = (100,550))
astro_rect = astro_big.get_rect(midbottom = (300,550))

#Gravidade
astro_grav = 0

#LOOP para manter tudo funcionando.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if astro_rect.collidepoint(event.pos) and astro_rect.bottom >=550:
                astro_grav = -17
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse down')
        if event.type == pygame.MOUSEBUTTONUP:
            print('Mouse up')'''
        #Controles
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and astro_rect.bottom >=550:
                astro_grav = -17

    #Camadas
    screen.blit(space_big,(0,0))
    screen.blit(ground_big,(0,550))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
    #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100)) - Para criar círculos ou elípses.
    #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) - para uma linha apontar para a posição do mouse
    
    screen.blit(text_score_surf,(score_rect))
    """snail_x_pos-=4
    if snail_x_pos <-100: snail_x_pos = 800"""
    snail_rect.x -= 4
    if snail_rect.right <=0: snail_rect.left = 800

    screen.blit(snail_big,snail_rect)
    # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
    # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

    #Astronauta
    astro_grav +=0.5
    astro_rect.y += astro_grav
    if astro_rect.bottom >=550:
        astro_rect.bottom = 550
    screen.blit(astro_big, astro_rect)

    #Controles
    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print('Jump')'''

    #Teste de colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if astro_rect.colliderect(snail_rect):
        print('Collision')"""
    pygame.draw.rect(screen, (255,0,0), astro_rect, 2)
    pygame.draw.rect(screen, (255,0,0), snail_rect, 2)
    """mouse_pos = pygame.mouse.get_pos()
    if astro_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)
