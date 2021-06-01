import pygame
from time import sleep

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200


def keyboard_input(target_key, run):
    # print("Keyboard input function reached")
    # sleep(3)
    # print("Delay period expired")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == target_key:
                return True
        else:
            return False


def main():
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Window")

    run = True
    clock = pygame.time.Clock()
    i = 0

    while run:
        i += 1
        take_pic = keyboard_input(pygame.K_a, run)
        if take_pic:
            print("Pressed")
        else:
            continue

        clock.tick(60)


pygame.quit()

if __name__ == '__main__':
    main()
