import pygame
import player
import asteroid
import asteroidfield
import sys
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)

    new_player = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    new_asteroidfield = asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for element in drawable:
            element.draw(screen)

        updatable.update(dt)

        for element in asteroids:
            if element.detect_collision(new_player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
