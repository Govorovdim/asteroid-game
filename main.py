# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)
    while True:
        for event in pygame.event.get(): # exit when window is clsoed
            if event.type == pygame.QUIT:
                return

        #========================== new frame started
        screen.fill("black") # background
        
        for item in updatable: # items update
            item.update(dt)

        for item in drawable: # items draw
            item.draw(screen)

        #========================== refrash screen
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()