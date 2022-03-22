import pygame

# Initialize pygame for game machanics
pygame.init()
# Initialize pygame for game sounds
pygame.mixer.init()

s_width = 750
s_height = 800  # 1010
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("BREAKOUT")

# Colors dictionary
colors = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Grey": (212, 210, 212),
    "Orange": (183, 119, 0),
    "Green": (0, 127, 33),
    "Blue": (0, 97, 148),
    "Red": (162, 8, 0),
    "Yellow": (197, 199, 37),
}

# define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 60

points = 0
balls = 1
vel = 4

p_height = 48
p_width = 15


# Creating the player

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > s_width - wall_width - p_width - 33:
            self.rect.x = s_width - wall_width - p_width - 33

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


# Creating the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.vel = [vel, vel]

    def update(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def bounce(self):
        self.vel[0] = self.vel[0]
        self.vel[1] = -self.vel[1]

    def draw(self):
        pygame.draw.circle(screen, colors["White"], (375, 300), 10)


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


# Creating object of player and ball

player = Paddle(colors["Blue"], p_height, p_width)
player.rect.x = s_width // 2
player.rect.y = 750
balls = 1
velocity = 4

ball = Ball(colors["White"], 10, 10)
ball.rect.x = s_width // 2 - 5
ball.rect.y = s_height // 2 - 5

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16



def main_game(points, balls):

    step = 0

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeft(8)
        if keys[pygame.K_RIGHT]:
            player.moveRight(8)

        screen.fill(colors["Black"])

        pygame.display.update()

        clock.tick(fps)


main_game(points, balls)