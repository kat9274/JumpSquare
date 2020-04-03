import pygame
pygame.init()

Screen = pygame.display.set_mode((750, 1000))
Clock = pygame.time.Clock()

def Events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #if event.type == pygame.MOUSEBUTTONDOWN:


#class Square:
#    Size = (50, 50)
#    Pos = (0, 0)

#class SquarePointer:


while True:
    Screen.fill((0, 0, 0))

    Events()

    pygame.display.flip()
    Clock.tick(60)
