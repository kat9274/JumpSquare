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

class Platform:
    def __init__(self, Pos, Color):
        self.Width = 100
        self.Height = 25
        self.Pos = (Pos[0] - (self.Width/2), Pos[1] - (self.Height/2))
        self.Color = Color
        self.Rect = Rect((self.Pos[0], self.Pos[1]), (self.Width, self.Height))

        Platforms.append(self)

class Square:
    def __init__(self, Pos, Color):
        self.Width = 50
        self.Height = 50
        self.Pos = (Pos[0] - (self.Width/2), Pos[1] - (self.Height/2))
        self.Rect = pygame.Rect(Pos, (self.Width, self.Height))

    def Jump():
        if (self.Pos[0]+50, self.Pos[1]+50) in Platforms and Direction == "left":
            print("you jumped right")
            self.Pos = (self.Pos[0]+50, self.Pos[1]+50)
        elif (self.Pos[0]-50, self.Pos[1]+50) in Platforms and Direction == "right":
            print("you jumped left")
            self.Pos = (self.Pos[0]-50, self.Pos[1]+50)

Platforms = []

def PlatformTree(Platform, Amount, Platforms):
    Pos = Platform.Pos
    Paths = random.randrange(1, 3)
    if Paths == 1:
        Platforms.append(Platform((0 - [50, -50][random.randrange(0, 1)], Pos[1] + 50)))
    elif Paths == 2:
        Platforms.append(Platform((Pos[0] - 50, Pos[1] + 50)))
        Platforms.append(Platform((Pos[0] + 100, Pos[1])))
    else:
        return 0
    Amount = Amount + Paths if Paths != 3 else 0
    if Amount < 50:
        PlatformTree(Platforms[0], Amount, Platforms)
        PlatformTree(Platforms[1], Amount, Platforms)

#PlatformTree()

while True:
    Screen.fill((0, 0, 0))

    for i in range(len(Platforms)):
        pygame.draw.rect(Surface, Platforms[i].Color, Platforms[i].Rect)

    Events()

    pygame.display.flip()
    Clock.tick(FrameRate)
