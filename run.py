import pygame

if __name__ == "__main__":
    pygame.init()

    # create a screen
    screen = pygame.display.set_mode((1024, 896))

    from main import main  # очень крутая мега хитрость при запуске
    main(screen)
