# Bibliotecas
import pygame

from sys import exit
#Janela
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('A janela')
clock = pygame.time.Clock()
fonte_teste = pygame.font.Font('font\Pixeltype.ttf', 50)


#Imagens e textos usados
#Para colocar imagens, basta coloca-las dentro da pasta do jogo.
#Usamos convert para trabalhar melhor com as imagens no pygame, além de melhorar o desempenho do jogo.
sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()
snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
text_surface = fonte_teste.render('My game', False, 'Black')
player_surface = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()


#Posições
snail_x_pos = 600
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))
player_rectangle = player_surface.get_rect(midbottom = (80,300))


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
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    """snail_x_pos-=4
    if snail_x_pos <-100: snail_x_pos = 800"""
    snail_rectangle.x -= 4
    if snail_rectangle.right <=0: snail_rectangle.left = 800

    screen.blit(snail_surface,(snail_rectangle))
    # print(player_rectangle.left) para ver a posição da linha de certo lado do retângulo.
    # player_rectangle.left +=1 irá mover o personagem para a esquerda da tela.

    screen.blit(player_surface, player_rectangle)

    #Colisão
    # print(player_rectangle.colliderect(snail_rectangle)) para checar colisão entre dois objetos.
    """if player_rectangle.colliderect(snail_rectangle):
        print('Collision')"""
    
    """mouse_pos = pygame.mouse.get_pos()
    if player_rectangle.collidepoint((mouse_pos)):
        print(pygame.mouse.get_pressed())"""

    pygame.display.update()
    clock.tick(60)
