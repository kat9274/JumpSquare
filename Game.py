import pygame, random
pygame.init()

WIDTH = 1000
HEIGHT = 1080
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock()
FrameRate = 60

PlatformRetain = 15

Platforms = []
Old = []

class Platform:
    def __init__(self, Pos, Color):
        self.Width = 80
        self.Height = 20
        self.Pos = (Pos[0]-(self.Width/2), Pos[1]-(self.Height/2))
        self.Color = Color
        self.Rect = pygame.Rect(self.Pos, (self.Width, self.Height))

        Platforms.append(self)

    def New(self, Direction):
        Color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        if Direction == 2:
            Platform((self.Pos[0]-110, self.Pos[1]-75), Color)
            Platform((self.Pos[0]+190, self.Pos[1]-75), Color)
        else:
            Platform((self.Pos[0]+[-110, 190][Direction], self.Pos[1]-75), Color)

class Player:
    Width = 30
    Height = 30
    Pos = (WIDTH/2-(Width/2), HEIGHT-101-(Height/2))
    Color = (50, 100, 255)
    Rect = pygame.Rect(Pos, (Width, Height))

def Jump(Direction):
    global Platforms, Old
    Player.Pos = (Player.Pos[0]+[-150, 150][Direction], Player.Pos[1]-85)
    if Player.Pos[0] > Platforms[Direction if len(Platforms) > 1 else 0].Pos[0] and Player.Pos[0] < Platforms[Direction if len(Platforms) > 1 else 0].Pos[0]+Platforms[Direction if len(Platforms) > 1 else 0].Width:
        pass
    else:
        pygame.quit()
        exit()
    Old = Old + Platforms
    Platform = Platforms[Direction if len(Platforms) > 1 else 0]
    Platforms = []
    Platform.New(random.randint(0, 2))
    Player.Rect = pygame.Rect(Player.Pos, (Player.Width, Player.Height))

Platform((WIDTH/2, HEIGHT-75), (50, 100, 255))
Platforms[0].New(random.randint(0, 2))
Old.append(Platforms.pop(Platforms.index(Platforms[0])))

def Events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Jump(0)
            elif event.key == pygame.K_RIGHT:
                Jump(1)

    if len(Old) >= PlatformRetain:
        Old.pop(0)

while True:
    try:
        Screen.fill((0, 0, 0))

        for i in range(len(Platforms)):
            pygame.draw.rect(Screen, Platforms[i].Color, Platforms[i].Rect)
        for i in range(len(Old)):
            pygame.draw.rect(Screen, Old[i].Color, Old[i].Rect)
        pygame.draw.rect(Screen, Player.Color, Player.Rect)

        Events()

        pygame.display.flip()
        Clock.tick(FrameRate)
    except KeyboardInterrupt:
        pygame.quit()
        exit()
