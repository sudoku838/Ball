import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
GLASS_WIDTH, GLASS_HEIGHT = 100, 300
GLASS_X = WIDTH - GLASS_WIDTH - 50
GLASS_Y = HEIGHT - GLASS_HEIGHT
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")
ball_x = WIDTH - BALL_RADIUS
ball_y = HEIGHT // 2
ball_speed_y = 5
ball_moving = False
start_button = pygame.Rect(50, HEIGHT - 100, 120, 50)
quit_button = pygame.Rect(200, HEIGHT - 100, 200, 50)
#Цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                ball_moving = True
            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
    # Логика
    if ball_moving:
        ball_y += ball_speed_y
        if ball_y + BALL_RADIUS >= HEIGHT:
            ball_speed_y = -ball_speed_y
        if ball_y - BALL_RADIUS <= 0:
            ball_speed_y = -ball_speed_y
        if ball_x - BALL_RADIUS <= 0:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_x, int(ball_y)), BALL_RADIUS, 2)  # 2 - толщина контура
    pygame.draw.rect(screen, (255, 255, 255), start_button)  # Кнопка "Пуск"
    pygame.draw.rect(screen, (255, 255, 255), quit_button)  # Кнопка "Завершить"
    font = pygame.font.Font(None, 36)
    start_text = font.render("Пуск", True, BLACK)
    quit_text = font.render("Завершить", True, BLACK)
    screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
    screen.blit(quit_text, (quit_button.x + 10, quit_button.y + 10))

    pygame.display.flip()
    pygame.time.delay(30)