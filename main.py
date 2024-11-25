# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from Shot import *

def main():
    pygame.init()   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()    

    dt = 0

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,updateable,drawable)

    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for sth in updateable:
            sth.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for sth in drawable:
            sth.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()