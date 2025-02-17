import pygame
import sys
from screeninfo import get_monitors
import json

GAME_NAME = "Tile Game"

is_developer = True

with open("settings.json", "r") as f:
    settings = json.load(f)
    if is_developer:
        print(settings)


    WIDTH = settings["screen"]["width"]
    HEIGHT = settings["screen"]["height"]

    TILE_SIZE = settings["display"]["tile_size"]

    FPS = settings["game"]["fps"]


monitors = get_monitors()
print(monitors)

screen = pygame.display.set_mode((WIDTH*TILE_SIZE, HEIGHT*TILE_SIZE))
pygame.display.set_caption(GAME_NAME)

Clock = pygame.time.Clock()


def main():
    exiting = False
    last_time = pygame.time.get_ticks()
    while True:
        Clock.tick(1000)

        current_time = pygame.time.get_ticks()
        eclipse_time = current_time - last_time
        last_time = current_time

        print(eclipse_time / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exiting = True
                pygame.display.set_caption(f"{GAME_NAME} (exiting...)")

        if exiting:
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
