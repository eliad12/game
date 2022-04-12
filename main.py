import pygame


pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Swords and Sandals")
# icon = pygame.image.load('game.png')
# pygame.display.set_icon(icon)

# PLAY BACKGROUND MUSIC
pygame.mixer.music.load("sound.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# player
playerImg = pygame.image.load('user.png')
playerX = 290
playerY = 650
vel_x = 10
vel_y = 10
jump = False
player_width = 240 - 10
player_height = 269

# enemy
playerImg_2 = pygame.image.load('enemy.png')
enemy_x = 1400
enemy_y = 615
vel_x_2 = 2
vel_y_2 = 2
enemy_width = 182 - 5
enemy_height = 294


# HPBAR
GREEN = (0, 255, 0)
RED = (255, 0, 0)
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player_health = 200


def loadify(img):
    return pygame.image.load(img).convert_alpha()


# background
background = loadify('Untitled.png')


def player():
    screen.blit(playerImg, (playerX, playerY))


def enemy():
    screen.blit(playerImg_2, (enemy_x, enemy_y))


running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    pygame.draw.rect(display, RED, (1350, 250, 200, 25))
    pygame.draw.rect(display, GREEN, (1350, 250, player_health, 25))

    if player_health <= 0:
        running = False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] or userInput[pygame.K_RIGHT]:
        if userInput[pygame.K_LEFT] and playerX > 280:
            playerX -= vel_x
        if userInput[pygame.K_RIGHT] and playerX < 1400:
            playerX += vel_x

        if enemy_x > playerX:
            enemy_x -= vel_x_2
        elif enemy_x < playerX:
            enemy_x += vel_x_2
        if enemy_x <= playerX <= enemy_x + enemy_width or playerX + player_width > enemy_x:
            player_health -= 50
            playerX -= 150

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
