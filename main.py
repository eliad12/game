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
vel = 10

# background
#background = pygame.image.load('Untitled.png')


def player(x,y):
    screen.blit(playerImg, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    #screen.blit(background, (0, 0))


    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and playerX > 0:
        playerX -= vel
    if userInput[pygame.K_RIGHT] and playerX < WINDOW_WIDTH:
        playerX += vel
    if userInput[pygame.K_UP] and playerY > 0:
        playerY -= vel
    if userInput[pygame.K_DOWN] and playerY < WINDOW_HEIGHT:
        playerY += vel


    player(playerX,playerY)
    pygame.display.update()
