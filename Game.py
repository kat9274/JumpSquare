import pygame, random
pygame.init()

Screen = pygame.display.set_mode()
Clock = pygame.time.Clock()

WIDTH, HEIGHT = pygame.display.get_surface().get_size()
RETAIN = round(HEIGHT / 100)
RUNNING = False

Platforms = []
Old = []

class Platform:
    def __init__(self, Pos, Color):
        self.Width, self.Height = 80, 20
        self.Pos = (Pos[0]-(self.Width/2), Pos[1]-(self.Height/2))
        self.Color = Color
        Platforms.append(self)

    def New(self, Direction):
        if Direction == 2:
            Platform((self.Pos[0]-110, self.Pos[1]-75), (random.randrange(30, 150), random.randrange(30, 255), random.randrange(30, 255)))
            Platform((self.Pos[0]+190, self.Pos[1]-75), (random.randrange(30, 150), random.randrange(30, 255), random.randrange(30, 255)))
            return 0
        Platform((self.Pos[0]+([-110, 190][Direction] if self.Pos[0] > 100 and self.Pos[0] < WIDTH-100 else (190 if self.Pos[0] <= 100 else -110)), self.Pos[1]-75), (random.randrange(30, 150), random.randrange(30, 255), random.randrange(30, 255)))

class Player:
    Width, Height = 30, 30
    Pos = (WIDTH/2-(Width/2), HEIGHT-101-(Height/2))
    Color = (50, 100, 255)
    Score = 0
    Falling = False

def Reset():
    global Old, Platforms
    Width, Height = 30, 30
    Player.Pos = (WIDTH/2-(Width/2), HEIGHT-101-(Height/2))
    Player.Score = 0
    Player.Falling = False

    Old, Platforms = [], []
    Platform((WIDTH/2, HEIGHT-75), (random.randrange(30, 150), random.randrange(30, 255), random.randrange(30, 255)))

def Die():
    global RUNNING
    while Player.Pos[1] < HEIGHT:
        Screen.fill((0, 0, 0))
        Player.Pos = (Player.Pos[0], Player.Pos[1] + 5)

        Screen.blit(pygame.font.Font('freesansbold.ttf', 50).render(str(Player.Score), True, (60, 95, 100)), (WIDTH//2-(pygame.font.Font('freesansbold.ttf', 50).render(str(Player.Score), True, (60, 95, 100)).get_size()[0]/2), 0))
        for i in range(len(Platforms)):
            pygame.draw.rect(Screen, Platforms[i].Color, pygame.Rect(Platforms[i].Pos, (Platforms[i].Width, Platforms[i].Height)))
        for i in range(len(Old)):
            pygame.draw.rect(Screen, Old[i].Color, pygame.Rect(Old[i].Pos, (Old[i].Width, Old[i].Height)))
        pygame.draw.rect(Screen, Player.Color, pygame.Rect(Player.Pos, (Player.Width, Player.Height)))

        pygame.display.flip()
        Clock.tick(60)
    RUNNING = False
    Reset()

def Jump(Direction):
    global Platforms, Old
    Player.Pos = (Player.Pos[0]+[-150, 150][Direction], Player.Pos[1]-85)
    if Player.Pos[0] > Platforms[Direction if len(Platforms) > 1 else 0].Pos[0] and Player.Pos[0] < Platforms[Direction if len(Platforms) > 1 else 0].Pos[0]+Platforms[Direction if len(Platforms) > 1 else 0].Width and Player.Pos[0] > 0 and Player.Pos[0] < WIDTH:
        Player.Score += 1
        pass
    else:
        Die()
    Old = Old + Platforms
    Platform = Platforms[Direction if len(Platforms) > 1 else 0]
    Platforms = []
    Platform.New(random.randint(0, 2))

Platform((WIDTH/2, HEIGHT-75), (random.randrange(30, 150), random.randrange(30, 255), random.randrange(30, 255)))
Platforms[0].New(random.randint(0, 2))
Old.append(Platforms.pop(Platforms.index(Platforms[0])))

def Events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Jump(0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Jump(1)

    if len(Old) >= RETAIN:
        Old.pop(0)

    if Player.Pos[1] > HEIGHT:
        Die()

while True:
    if RUNNING:
        try:
            Screen.fill((0, 0, 0))

            if Old[0].Pos[1] < HEIGHT - 100:
                Player.Falling = True

            if Player.Falling == True:
                for i in range(len(Platforms)):
                    Platforms[i].Pos = (Platforms[i].Pos[0], Platforms[i].Pos[1] + (10 if Player.Pos[1] < 150 else 2.5))
                for i in range(len(Old)):
                    Old[i].Pos = (Old[i].Pos[0], Old[i].Pos[1] + (10 if Player.Pos[1] < 150 else 2.5))
                Player.Pos = (Player.Pos[0], Player.Pos[1] + (10 if Player.Pos[1] < 150 else 2.5))

            Screen.blit(pygame.font.Font('freesansbold.ttf', 50).render(str(Player.Score), True, (60, 95, 100)), (WIDTH//2-(pygame.font.Font('freesansbold.ttf', 50).render(str(Player.Score), True, (60, 95, 100)).get_size()[0]/2), 0))
            for i in range(len(Platforms)):
                pygame.draw.rect(Screen, Platforms[i].Color, pygame.Rect(Platforms[i].Pos, (Platforms[i].Width, Platforms[i].Height)))
            for i in range(len(Old)):
                pygame.draw.rect(Screen, Old[i].Color, pygame.Rect(Old[i].Pos, (Old[i].Width, Old[i].Height)))
            pygame.draw.rect(Screen, Player.Color, pygame.Rect(Player.Pos, (Player.Width, Player.Height)))

            Events()

            pygame.display.flip()
            Clock.tick(60)

        except KeyboardInterrupt:
            pygame.quit()
            exit()
    else:
        try:
            Screen.fill((0, 0, 0))

            Screen.blit(pygame.font.Font('freesansbold.ttf', 80).render("Jump Square", True, (60, 150, 100)), (WIDTH//2-(pygame.font.Font('freesansbold.ttf', 80).render("Jump Square", True, (60, 150, 100)).get_size()[0]/2), HEIGHT/6))

            pygame.draw.rect(Screen, (255, 0, 0), pygame.Rect((WIDTH//2-100, HEIGHT/3-50), (200, 100)))
            Screen.blit(pygame.font.Font('freesansbold.ttf', 50).render("Start", True, (60, 150, 100)), (WIDTH//2-(pygame.font.Font('freesansbold.ttf', 50).render("Start", True, (60, 150, 100)).get_size()[0]/2), HEIGHT/3-25))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    if mousepos[0] > WIDTH//2-100 and mousepos[0] < WIDTH//2+100 and mousepos[1] > HEIGHT/3-50 and mousepos[1] < HEIGHT/3+50:
                        RUNNING = True

            pygame.display.flip()
            Clock.tick(60)
        except KeyboardInterrupt:
            pygame.quit()
            exit()
