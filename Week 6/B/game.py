# Imports
import pygame
import sys
from pygame.locals import *
import random
import time

# Init pygame
pygame.init()

# SetFPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Colours ( we didn't actually need all of them Max :) )
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Settings ( I made this for a 4k monitor btw,
#            so change this if your screen is too small :D )
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1600
SPEED = 7
SCORE = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background Image
background = pygame.image.load("bg.jpg")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

### CLASES ###
# ** these classes describe how they will behave each time
# ** a new "Sprite" (pygame term) is created
# Enemy


class Enemy(pygame.sprite.Sprite):
    # NOTE: all objects that are created (including this "Sprite") runs the
    # `__init__` function first (on initialization)!
    def __init__(self):
        super().__init__()  # call pygame's Sprite super class's `__init__` function
        # Image of the missile
        self.image = pygame.image.load("Enemy.png")
        # Hitbox of the missile
        self.surf = pygame.Surface((34, 128))
        # Spawn location of the missile, 20 is the minimum distance from either side of the SCREEN
        self.rect = self.surf.get_rect(  # the `randint` function returns a random
            # number between the two inputted values
            center=(random.randint(20, SCREEN_WIDTH-20), 0))

    def move(self):
        global SCORE  # recall that we learnt that you must use the `global` keyword
        # if you want to use a "global" variable!
        self.rect.move_ip(0, SPEED)
        # keep moving missile downwards until it nearly reaches the bottom of the screen
        if (self.rect.top > SCREEN_HEIGHT-10):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player (fighter jet)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # same as enemy
        # Load image of the fighter jet
        self.image = pygame.image.load("Player.png")
        # Hitbox
        self.surf = pygame.Surface((220, 250))
        # Spawn location of the player sprite
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH/2, SCREEN_HEIGHT-170))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

######################################
### THE GAME ACTUALLY STARTS HERE! ###
######################################


# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# "Game Loop"
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and re-renders all the Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # If a missile hits the fighter jet
    if pygame.sprite.spritecollideany(P1, enemies):
        #   pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        # Display game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        # Clean up the game so that there are no memory leaks
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Call this stuff after each frame is rendered
    pygame.display.update()
    FramePerSec.tick(FPS)
