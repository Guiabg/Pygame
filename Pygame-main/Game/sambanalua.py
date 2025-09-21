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
text_surf = fonte_teste.render('Teste.', False, 'White')
astro_surf = pygame.image.load('Pygame-main\\sprites\\spr_1.png').convert_alpha()

#Imagens rescalionadas
astro_big = pygame.transform.scale(astro_surf, (90,135)).convert_alpha()
space_big = pygame.transform.scale(space_surf, (1300,600)).convert()
ground_big = pygame.transform.scale(ground_surf, (1300,200)).convert()
snail_big = pygame.transform.scale(snail_surf, (100,60)).convert_alpha()

#Posições e colisões
snail_x_pos = 600
snail_rect = snail_big.get_rect(bottomright = (100,550))
astro_rect = astro_big.get_rect(midbottom = (300,550))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        """if event.type == pygame.MOUSEMOTION:  Para checar os botões do mouse no jogo.
            print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Mouse down')
        if event.type == pygame.MOUSEBUTTONUP:
            print('Mouse up')"""

    #Camadas
    screen.blit(space_big,(0,0))
    screen.blit(ground_big,(0,550))
    screen.blit(text_surf,(300,50))
    """snail_x_pos-=4
    if snail_x_pos <-100: snail_x_pos = 800"""
    snail_rect.x -= 4
    if snail_rect.right <=0: snail_rect.left = 800

    screen.blit(snail_big,snail_rect)
    # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
    # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

    screen.blit(astro_big, astro_rect)

    if astro_rect.colliderect(snail_rect):
        print('collision')

    #Teste de colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if astro_rect.colliderect(snail_rect):
        print('Collision')"""
    pygame.draw.rect(screen, (255,0,0), astro_rect, 2)
    pygame.draw.rect(screen, (255,0,0), snail_rect, 2)
    """mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)
