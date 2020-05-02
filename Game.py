import pygame, random
pygame.init()
pygame.font.init()

WIDTH = 1920
HEIGHT = 1080
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock()
FrameRate = 60
Falling = False
Score = 0

PlatformRetain = round(WIDTH / 100)

Platforms = []
Old = []

class Platform:
    def __init__(self, Pos, Color):
        self.Width = 80
        self.Height = 20
        self.Pos = (Pos[0]-(self.Width/2), Pos[1]-(self.Height/2))
        self.Color = Color
        self.Rect = pygame.Rect(self.Pos, (self.Width, self.Height))
        if self.Pos[0] < 1000 or self.Pos[0] > 0:
            Platforms.append(self)

    def New(self, Direction):
        Color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        if Direction == 2:
            Platform((self.Pos[0]-110, self.Pos[1]-75), Color)
            Platform((self.Pos[0]+190, self.Pos[1]-75), Color)
        elif self.Pos[0] > 100 and self.Pos[0] < WIDTH-100:
            Platform((self.Pos[0]+[-110, 190][Direction], self.Pos[1]-75), Color)
        elif self.Pos[0] <= 100:
            Platform((self.Pos[0] + 190, self.Pos[1] -75), Color)
        else:
            Platform((self.Pos[0] -110, self.Pos[1] -75), Color)

class Player:
    Width = 30
    Height = 30
    Pos = (WIDTH/2-(Width/2), HEIGHT-101-(Height/2))
    Color = (50, 100, 255)
    Rect = pygame.Rect(Pos, (Width, Height))

def Die():
    while Player.Pos[1] < HEIGHT:
        Screen.fill((0, 0, 0))
        Player.Pos = (Player.Pos[0], Player.Pos[1] + 5)

        Screen.blit(pygame.font.Font('freesansbold.ttf', 50).render(str(Score), True, (60, 95, 100)), (WIDTH//2, 0))
        for i in range(len(Platforms)):
            pygame.draw.rect(Screen, Platforms[i].Color, pygame.Rect(Platforms[i].Pos, (Platforms[i].Width, Platforms[i].Height)))
        for i in range(len(Old)):
            pygame.draw.rect(Screen, Old[i].Color, pygame.Rect(Old[i].Pos, (Old[i].Width, Old[i].Height)))
        pygame.draw.rect(Screen, Player.Color, pygame.Rect(Player.Pos, (Player.Width, Player.Height)))

        pygame.display.flip()
        Clock.tick(FrameRate)
    pygame.quit()
    exit()

def Jump(Direction):
    global Platforms, Old, Score
    Player.Pos = (Player.Pos[0]+[-150, 150][Direction], Player.Pos[1]-85)
    if Player.Pos[0] > Platforms[Direction if len(Platforms) > 1 else 0].Pos[0] and Player.Pos[0] < Platforms[Direction if len(Platforms) > 1 else 0].Pos[0]+Platforms[Direction if len(Platforms) > 1 else 0].Width and Player.Pos[0] > 0 and Player.Pos[0] < WIDTH:
        Score += 1
        pass
    else:
        Die()
    Old = Old + Platforms
    Platform = Platforms[Direction if len(Platforms) > 1 else 0]
    Platforms = []
    Platform.New(random.randint(0, 2))

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

    if Player.Pos[1] > HEIGHT:
        Die()

while True:
    try:
        Screen.fill((0, 0, 0))

        if Old[0].Pos[1] < HEIGHT - 100:
            Falling = True

        if Falling == True:
            for i in range(len(Platforms)):
                Platforms[i].Pos = (Platforms[i].Pos[0], Platforms[i].Pos[1] + (10 if Player.Pos[1] < 100 else 2.5))
            for i in range(len(Old)):
                Old[i].Pos = (Old[i].Pos[0], Old[i].Pos[1] + (10 if Player.Pos[1] < 100 else 2.5))
            Player.Pos = (Player.Pos[0], Player.Pos[1] + (10 if Player.Pos[1] < 100 else 2.5))

        Screen.blit(pygame.font.Font('freesansbold.ttf', 50).render(str(Score), True, (60, 95, 100)), (WIDTH//2, 0))
        for i in range(len(Platforms)):
            pygame.draw.rect(Screen, Platforms[i].Color, pygame.Rect(Platforms[i].Pos, (Platforms[i].Width, Platforms[i].Height)))
        for i in range(len(Old)):
            pygame.draw.rect(Screen, Old[i].Color, pygame.Rect(Old[i].Pos, (Old[i].Width, Old[i].Height)))
        pygame.draw.rect(Screen, Player.Color, pygame.Rect(Player.Pos, (Player.Width, Player.Height)))

        Events()

        pygame.display.flip()
        Clock.tick(FrameRate)

    except KeyboardInterrupt:
        pygame.quit()
        exit()
