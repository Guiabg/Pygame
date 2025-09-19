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
sky_surface = pygame.image.load('Pygame-main\graphics\Sky.png').convert()
ground_surface = pygame.image.load('Pygame-main\graphics\ground.png').convert()
snail_surface = pygame.image.load('Pygame-main\graphics\snail\snail1.png').convert_alpha()
text_surface = fonte_teste.render('Teste.', False, 'Black')
player_surface = pygame.image.load('Pygame-main\sprites\spr_1.png').convert_alpha()

#Imagens rescalionadas
player_big = pygame.transform.scale(player_surface, (500,500)).convert_alpha()
sky_big = pygame.transform.scale(sky_surface, (1300,750))
ground_big = pygame.transform.scale(ground_surface, (1300,200))
snail_big = pygame.transform.scale(snail_surface, (100,60))

#Posições
snail_x_pos = 600
snail_rectangle = snail_surface.get_rect(bottomright = (500,200))
player_rectangle = player_surface.get_rect(midbottom = (100,200))


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
    screen.blit(sky_big,(0,0))
    screen.blit(ground_big,(0,550))
    screen.blit(text_surface,(300,50))
    """snail_x_pos-=4
    if snail_x_pos <-100: snail_x_pos = 800"""
    snail_rectangle.x -= 4
    if snail_rectangle.right <=0: snail_rectangle.left = 800

    screen.blit(snail_big,(snail_rectangle))
    # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
    # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

    screen.blit(player_big, (player_rectangle))

    #Colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if player_rectangle.colliderect(snail_rectangle):
        print('Collision')"""
    
    """mouse_pos = pygame.mouse.get_pos()
    if player_rectangle.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)
