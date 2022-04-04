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
playerX = 250
playerY = 650
vel_x = 10
vel_y = 10
jump = False

# enemy
playerImg_2 = pygame.image.load('enemy.png')
playerX_2 = 1400
playerY_2 = 615
vel_x_2 = 10
vel_y_2 = 10
#jump_2 = False


def loadify(img):
    return pygame.image.load(img).convert_alpha()


# background
background = loadify('Untitled.png')


def player():
    screen.blit(playerImg, (playerX,playerY))

def enemy():
    screen.blit(playerImg_2,(playerX_2,playerY_2))



running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))


    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and playerX > 220:
        playerX -= vel_x
    if userInput[pygame.K_RIGHT] and playerX < 1450:
        playerX += vel_x

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True

    if jump is True:
        playerY -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10


    player()
    enemy()
    pygame.time.delay(10)
    pygame.display.update()
