import pygame
import random

class Sprite:
    def __init__(self, x, y, width, height, *, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)

        self.vel_x = 0
        self.vel_y = 0

        self.surface = pygame.Surface((width, height))
        self.surface.fill(color)

        @property
        def x(self):
            return self.rect.x

        @x.setter
        def x(self, value):
            self.rect.x = value

        @property
        def y(self):
            return self.rect.y

        @y.setter
        def y(self, value):
            self.rect.y = value

        @property
        def width(self):
            return self.rect.width

        @property
        def height(self):
            return self.rect.height

    def move(self, dt=1):
        self.rect.x += self.vel_x * dt
        self.rect.y += self.vel_y * dt

    def clamp_to_window(self, win_width, win_height):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > win_width:
            self.rect.right = win_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > win_height:
            self.rect.bottom = win_height

    def collides_with(self, other_sprite):
        return self.rect.colliderect(other_sprite.rect)

    def draw(self, surface):
        surface.blit(self.surface, self.rect.topleft)

class Wall(Sprite):
    def __init__(self, x, y, w, h, color=(0, 0, 255), min_margin=100):
        super().__init__(x, y, w, h, color=color)
        self.min_margin = min_margin
        self.w = w
        self.h = h

    def reset(self):
        self.rect.x = random.randint(self.min_margin, window.width - self.min_margin - self.w)
        self.rect.y = random.randint(self.min_margin, window.height - self.min_margin - self.h)

class Pixel(Sprite):
    def __init__(self, x, y, w, h, color=(255, 255, 255), min_margin=50):
        super().__init__(x, y, w, h, color=color)
        self.min_margin = min_margin
        self.w = w
        self.h = h

    def reset(self):
        self.rect.x = random.randint(self.min_margin, window.width - self.min_margin - self.w)
        self.rect.y = random.randint(self.min_margin, window.height - self.min_margin - self.h)

class House(Sprite):
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        super().__init__(x, y, w, h, color=color)

def wall(width=4, height=4, min_margin=170):
    x = random.randint(min_margin, window.width - min_margin - width)
    y = random.randint(min_margin, window.height - min_margin - height)
    return Wall(x, y, width, height, color=(0, 0, 255))

def pixel(width=10, height=10, min_margin=50, color=(255, 255, 255)):
    x = random.randint(min_margin, window.width - min_margin - width)
    y = random.randint(min_margin, window.height - min_margin - height)
    return Pixel(x, y, width, height, color=color)

def house(x=0, y=0, width=60, height=60, color=(255, 255, 255)):
    return House(x, y, width, height, color=color)

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Pixel Courier")

player = Sprite(5, int(window.height / 2 - 25), 50, 50)

pixels = [
    pixel(color=(255, 0, 0)),
    pixel(color=(0, 255, 0)),
    pixel(color=(0, 0, 255))
]

houses = [
    house(window.width - 65, 5, color=(255, 0, 0)),
    house(5, window.height - 65, 100, color=(0, 255, 0)),
    house(window.width - 65, window.height - 125, height=120, color=(0, 0, 255))
]

walls = [
    wall(4, 260)
]

inventory = [
    False,
    False,
    False
]

font = pygame.font.Font(None, 36)

scoreText = font.render("", True, (0, 0, 0), (255, 255, 255))
score = 0

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player.vel_x = 0.2
            if event.key == pygame.K_UP:
                player.vel_y = -0.2
            if event.key == pygame.K_DOWN:
                player.vel_y = 0.2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.vel_x = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.vel_y = 0

    window.fill((255, 255, 255))

    for i in range(len(pixels)):
        if player.collides_with(pixels[i]):
            inventory[i] = True

    for i in walls:
        if player.collides_with(i):
            player.rect.x = 5
            player.rect.y = 40

    for i in range(len(inventory)):
        if inventory[i] == True:
            pixels[i].rect.x = player.rect.x + 5 + i*15
            pixels[i].rect.y = player.rect.y + 5

    for i in range(len(houses)):
        if player.collides_with(houses[i]) and inventory[i] == True:
            pixels[i].reset()
            for j in walls:
                j.reset()
            score += 1
            if random.randint(0, 1) == 0:
                walls.append(wall(4, 260))
            else:
                walls.append(wall(460, 4))
            scoreText = font.render("Score: " + str(score), True, (0, 0, 0), (255, 255, 255))
            inventory[i] = False

    player.move(20)
    player.clamp_to_window(window.width, window.height)

    for i in houses:
        i.draw(window)

    window.blit(player.surface, player.rect)

    for i in pixels:
        i.draw(window)



    for i in walls:
        i.draw(window)

    window.blit(scoreText, (5, 5))

    pygame.display.flip()
    clock.tick(60)