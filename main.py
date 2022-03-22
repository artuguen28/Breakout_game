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