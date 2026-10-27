import pygame
import random

def collision_detection(objectA_x, objectA_y, objectB_x, objectB_y, objectA_width, objectA_height, objectB_width, objectB_height):
    return (objectA_x <= (objectB_x + int(objectB_width)) and
            (objectA_x + objectA_width) >= objectB_x and
             objectA_y <= (objectB_y + objectB_height) and
            (objectA_y + objectA_height) >= objectB_y)

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Pixel Courier")

player = pygame.surface.Surface((50, 50))
player.fill((0, 0, 0))

player_x = 5
player_y = window.height / 2 - player.height / 2
player_vel_x = 0
player_vel_y = 0

package = pygame.surface.Surface((10, 10))
package.fill((255, 0, 0))

package_x = random.randint(50, window.width - 50)
package_y = random.randint(50, window.height - 50)

redHouse = pygame.surface.Surface((60,60))
redHouse.fill((255, 255, 255))

redHouse_x = window.width - 70
redHouse_y = 10

wallA = pygame.surface.Surface((4, 160))
wallA.fill((0, 0, 255))
wallA_x = random.randint(100, window.width - 100)
wallA_y = random.randint(100, window.height - 100)

wallB = pygame.surface.Surface((160, 4))
wallB.fill((0, 0, 255))
wallB_x = random.randint(100, window.width - 100)
wallB_y = random.randint(100, window.height - 100)

font = pygame.font.Font(None, 36)

scoreText = font.render("", True, (0, 0, 0), (255, 255, 255))
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2
            if event.key == pygame.K_UP:
                player_vel_y = -0.2
            if event.key == pygame.K_DOWN:
                player_vel_y = 0.2
        else:
            player_vel_x = 0
            player_vel_y = 0

    window.fill((255, 255, 255))

    if collision_detection(player_x, player_y, wallA_x, wallA_y, player.width, player.height, wallA.width, wallA.height) or collision_detection(player_x, player_y, wallB_x, wallB_y, player.width, player.height, wallB.width, wallB.height):
        if player_vel_x > 0:
            player_vel_x = -0.2
        elif player_vel_x < 0:
            player_vel_x = 0.2

        if player_vel_y > 0:
            player_vel_y = -0.2
        elif player_vel_y < 0:
            player_vel_y = 0.2

    if player_x + player_vel_x >= 0 and player_x + player_vel_x + player.width <= window.width + 1:
        player_x += player_vel_x

    if player_y + player_vel_y >= 0 and player_y + player_vel_y + player.height <= window.height + 1:
        player_y += player_vel_y

    if collision_detection(player_x, player_y, package_x, package_y, player.width, player.height, package.width, package.height):
        package_x = player_x + 5
        package_y = player_y + 5
        redHouse.fill((255, 0, 0))
        first = True

    if collision_detection(player_x, player_y, redHouse_x, redHouse_y, player.width, player.height, redHouse.width, redHouse.height) and first:
        package_x = random.randint(50, window.width - 50)
        package_y = random.randint(50, window.height - 50)
        redHouse.fill((255, 255, 255))
        wallA_x = random.randint(100, window.width - 100)
        wallA_y = random.randint(100, window.height - 100)
        wallB_x = random.randint(100, window.width - 100)
        wallB_x = random.randint(100, window.height - 100)
        score += 1
        scoreText = font.render("Score: " + str(score), True, (255, 255, 255), (0, 0, 0))
        first = False


    window.blit(redHouse, ((redHouse_x, redHouse_y)))
    window.blit(player, (player_x, player_y))
    window.blit(package, (package_x, package_y))
    window.blit(wallA, (wallA_x, wallA_y))
    window.blit(wallB, (wallB_x, wallB_y))
    window.blit(scoreText, (5, 5))
    

    pygame.display.flip()