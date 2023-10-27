import pygame
from game_logic import Snake, Apple

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

def game_loop():
    game_over = False
    game_close = False

    # Initialize snake and apple
    snake = Snake(width, height)
    apple = Apple(width, height)

    while not game_over:
        while game_close:
            window.fill(WHITE)
            font = pygame.font.SysFont('arial', 30)
            message = font.render('You Lost! Press C-Continue or Q-Quit', True, RED)
            window.blit(message, [width/6, height/3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # (rest of the game loop code remains the same)
