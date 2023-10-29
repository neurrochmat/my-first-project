import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_SPEED = 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Mania")

snake = [(4, 4)]
snake_dir = (1, 0)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, BLUE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, GREEN, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_score(score):
    score_text = font.render("Skor: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
        snake_dir = (1, 0)
    if keys[pygame.K_UP] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    if keys[pygame.K_DOWN] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    x, y = snake[0]
    new_x = (x + snake_dir[0]) % GRID_WIDTH
    new_y = (y + snake_dir[1]) % GRID_HEIGHT
    new_head = (new_x, new_y)
    if new_head in snake:
        running = False
    snake.insert(0, new_head) # type: ignore
    if new_head == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    draw_score(score)

    pygame.display.update()

    clock.tick(SNAKE_SPEED)

pygame.quit()
