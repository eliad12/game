import pygame

pygame.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("GodOfWar")
# icon = pygame.imgae.load('game.png')
# pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load('user.png')
playerX = 290
playerY = 650
vel_x = 10
vel_y = 10
jump = False
player_height = 240
player_width = 269





# enemy
playerImg_2 = pygame.image.load('enemy.png')
enemy_x = 1400
enemy_y = 615
vel_x_2 = 2
vel_y_2 = 2
enemy_height = 182
enemy_width = 294
#jump_2 = False


#HPBAR
GREEN = (0,255,0)
RED = (255,0,0)
display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
player_health = 200


def loadify(img):
    return pygame.image.load(img).convert_alpha()


# background
background = loadify('Untitled.png')


def player():
    screen.blit(playerImg, (playerX,playerY))

def enemy():
    screen.blit(playerImg_2,(enemy_x,enemy_y))

def check_collision(user_x, enemy_x, user_y, enemy_y, player_health):
    if user_x == enemy_x and user_y == enemy_y:
        player_health-=50
    
    

running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    pygame.draw.rect(display, RED,(300,250,200,20))
    pygame.draw.rect(display, GREEN,(300,250,player_health,25))


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
        if playerX == enemy_x and playerY == enemy_y and player and player_height == enemy_height and player_width == enemy_width:
            player_health -= 50
            print(player_health)

        # check_collision(playerX,enemy_x, playerY,enemy_y)
            







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
