


import pygame

pygame.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("GodOfWar")
# icon = pygame.imgae.load('game.png')
# pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load('sword.png')
playerX = 490
playerY = 490
playerX_cahnge = 0
vel = 10

# background
#background = pygame.image.load('Untitled.png')


def player(x,y):
    screen.blit(playerImg, (x, y))


running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # screen.blit(background, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_cahnge = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_cahnge = 0.8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_cahnge = 0

    playerX+= playerX_cahnge

    if playerX <= 0:
        playerX = 0
    elif playerX >= :

    player(playerX,playerY)
    pygame.display.update()
