import pygame
import random

#Sirve para inicializar a pygame
pygame.init()

#Sirve para crear la pantalla donde correra nuestro juego
screen = pygame.display.set_mode((800,600))

#Titulo e icono de la ventana
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.png")

#variables del jugador
#Jugador
img_player = pygame.image.load("nave-espacial.png")

player_x = 368
player_y = 500

player_x_changed = 0

#variables del enemigo
#Enemigo
img_enemy = pygame.image.load("enemigo.png")
enemy_random_x = random.randint(0, 736)
enemy_random_y = random.randint(50,200)

enemy_x = 368
enemy_y = 200

enemy_x_changed = 0.3
enemy_y_changed = 30


#Funcion player
def player(x, y):
    screen.blit(img_player,(x, y))

#Funcion enemigo
def enemy(x, y):
    screen.blit(img_enemy,(x, y))

#loop del juego
running_game = True
while running_game:
    #RGB
    #screen.fill((205, 144, 228))
    #imagen de fondo
    screen.blit(fondo, (0,0))

    #iterar eventos
    for evento in pygame.event.get():
        #evento cerrar
        if evento.type == pygame.QUIT:
            running_game = False
        #evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_x_changed = -1
            if evento.key == pygame.K_RIGHT:
                player_x_changed = +1

        #evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                player_x_changed = 0

    #modificar ubicacion jugador
    player_x += player_x_changed

    #mantener dentro de bordes al jugador
    if player_x <= 0:
        player_x = 0

    if player_x >= 736:
        player_x = 736

    # modificar ubicacion jugador
    enemy_x += enemy_x_changed

    # mantener dentro de bordes al enemigo
    if enemy_x <= 0:
        enemy_x_changed = 0.2
        enemy_y += enemy_y_changed
    elif enemy_x >= 736:
        enemy_x_changed = -0.2
        enemy_y += enemy_y_changed

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    #actualizar
    pygame.display.update()