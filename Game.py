import pygame, random
pygame.init()

Screen = pygame.display.set_mode((750, 1000))
Clock = pygame.time.Clock()
FrameRate = 60

def Events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.LEFT:
                Square.Jump("left")
            if event.key == pygame.RIGHT:
                Square.Jump("right")

class Square:
    Size = (50, 50)
    Pos = (0, 0)
    #Rect = pygame.Rect(Pos, (Width, Height))

    def Jump(self, Direction):
        print(1)

def PlatformTree():
    Platforms = []
    Pos = (0, 0)
    Paths = random.randrange(1, 3)
    print(Paths)
    if Paths == 1:
        Pos = (0 - [50, -50][random.randrange(0, 1)], 0)
        #Platforms.append(Platform(Pos))
    elif Paths == 2:
        Pos[0] = Pos[0] - 50
        #Platforms.append(Platform(Pos))
        Pos[0] = Pos[0] + 50
        #Platforms.append(Platform(Pos))
    print(Pos)
    #PlatformTree(Platforms[random.randrange(0,1) if len(Platforms) > 0 else 0])

PlatformTree()

while True:
    Screen.fill((0, 0, 0))

    Events()

    pygame.display.flip()
    Clock.tick(FrameRate)
