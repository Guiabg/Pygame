import os
import pygame
from sys import exit
from random import randint

# Pega o diretório onde o script atual está
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load(os.path.join(sourceFileDir, 'audio', 'music.wav'))
pygame.mixer.music.play(-1)  # faz a música tocar em loop infinito


# FUNÇÕES
# Pontuação
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = fonte_texto.render(f'Tempo: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(1130, 57))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)
    return current_time

# Loop de inimigos
def obstacle_movement(lista_inimigos):
    if lista_inimigos:
        for lista_inimigos_rect in lista_inimigos:
            lista_inimigos_rect.x -= velocidade_inimigo
            if lista_inimigos_rect.bottom == 600:
                screen.blit(snail_big, lista_inimigos_rect)
            else:
                screen.blit(foguete_big, lista_inimigos_rect)

        lista_inimigos = [obstacle for obstacle in lista_inimigos if obstacle.x > -320]

        return lista_inimigos
    else:
        return []

# Colisões
def collisions(astro, obstacles):
    if obstacles:
        for lista_inimigos_rect in obstacles:
            if astro.colliderect(lista_inimigos_rect):
                return False
    return True

# Animação do astronauta
def astro_animation():
    global astro_surf, astro_index

    if astro_rect.bottom < 600:  # Se está no ar
        astro_surf = astro_jump
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_a] or keys[pygame.K_d]:
            astro_index += 0.2
            if astro_index >= len(astro_walk):
                astro_index = 0
            astro_surf = astro_walk[int(astro_index)]
        else:
            astro_surf = astro_stand


# INÍCIO DO JOGO
pygame.init()
screen = pygame.display.set_mode((1300, 750))
pygame.display.set_caption('Samba na Lua')
clock = pygame.time.Clock()

# Diretório base
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

# Fonte
fontByOS = os.path.join(sourceFileDir, 'font', 'ari-w9500-display.ttf')
fonte_texto = pygame.font.Font(fontByOS, 24)

# Estado do jogo
jogo_ativo = False
start_time = 0
score = 0

# Background
space_surf = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'space.png')).convert()
ground_surf = pygame.image.load(os.path.join(sourceFileDir, 'graphics', 'ground.png')).convert()
planeta = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'Objetos', 'planeta.png')).convert_alpha()

space_big = pygame.transform.scale(space_surf, (1300, 650))
ground_big = pygame.transform.scale(ground_surf, (1300, 200))
planeta = pygame.transform.scale(planeta, (230, 230))


# SPRITES DO ASTRONAUTA
astro_walk = []
for i in range(1, 9):
    img = pygame.image.load(os.path.join(sourceFileDir, 'sprites', f'spr_{i}.png')).convert_alpha()
    img = pygame.transform.scale(img, (98, 135))
    astro_walk.append(img)

astro_index = 0
astro_jump = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'Objetos', 'spr_1.png')).convert_alpha()
astro_jump = pygame.transform.scale(astro_jump, (98, 135))
astro_stand = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'spr_1.png')).convert_alpha()
astro_stand = pygame.transform.scale(astro_stand, (98, 135))

astro_surf = astro_stand
astro_rect = astro_surf.get_rect(midbottom=(170, 600))

# Posição do planeta
planeta_rect = planeta.get_rect(center=(630, 370))

# Mensagens
nome_jogo = fonte_texto.render('Samba Lua', False, (111, 196, 169))
nome_jogo_rect = nome_jogo.get_rect(center=(630, 115))
mensagem_jogo = fonte_texto.render('Pressione Espaço para começar.', False, (111, 196, 169))
mensagem_jogo_rect = mensagem_jogo.get_rect(center=(650, 620))

# Inimigos
alien_surf = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'alien1.png')).convert_alpha()
snail_big = pygame.transform.scale(alien_surf, (76, 96))
foguete_surf = pygame.image.load(os.path.join(sourceFileDir, 'sprites', 'Objetos', 'foguete.png')).convert_alpha()
foguete_big = pygame.transform.scale(foguete_surf, (180, 85))
lista_inimigos_rect = []

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Gravidade
astro_grav = 0
velocidade_inimigo = 6


# LOOP PRINCIPAL

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if jogo_ativo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if astro_rect.collidepoint(event.pos) and astro_rect.bottom >= 600:
                    astro_grav = -21

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_w) and astro_rect.bottom >= 600:
                    astro_grav = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                start_time = int(pygame.time.get_ticks() / 1000)
                lista_inimigos_rect.clear()

        if event.type == obstacle_timer and jogo_ativo:
            if randint(0, 2):
                lista_inimigos_rect.append(snail_big.get_rect(bottomright=(randint(1400, 1600), 600)))
            else:
                lista_inimigos_rect.append(foguete_big.get_rect(midbottom=(randint(1400, 1600), 300)))

    if jogo_ativo:
        screen.blit(space_big, (0, 0))
        screen.blit(ground_big, (0, 600))

        score = display_score()
        velocidade_inimigo = 6 + (score // 10)


        # Gravidade
        astro_grav += 0.6
        astro_rect.y += astro_grav
        if astro_rect.bottom >= 600:
            astro_rect.bottom = 600
            astro_grav = 0

        # Movimento lateral
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            astro_rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            astro_rect.x += 5

        if astro_rect.left < 0: astro_rect.left = 0
        if astro_rect.right > 1300: astro_rect.right = 1300

        # Animação
        astro_animation()
        screen.blit(astro_surf, astro_rect)

        # Inimigos
        lista_inimigos_rect = obstacle_movement(lista_inimigos_rect)
        jogo_ativo = collisions(astro_rect, lista_inimigos_rect)

    else:
        screen.fill((94, 129, 162))
        screen.blit(planeta, planeta_rect)
        screen.blit(nome_jogo, nome_jogo_rect)
        score_message = fonte_texto.render(f'Sua pontuação: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(650, 200))
        astro_rect.midbottom = (170, 600)
        astro_grav = 0

        if score == 0:
            screen.blit(mensagem_jogo, mensagem_jogo_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
