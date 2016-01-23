import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()

# Parameters
window_size = (720, 640)
# Paddle


done = False

clock = pygame.time.Clock()
ball = Ball()
paddle = Paddle()
print(ball.x_pos)
screen = pygame.display.set_mode(window_size)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: paddle.x_pos -= 3
    if pressed[pygame.K_RIGHT]: paddle.x_pos += 3

    screen.fill((0, 0, 0))

    if (ball.x_pos <= 20) or (ball.x_pos >= window_size[0]-20):
        ball.vx = -ball.vx
    if (ball.y_pos <= 20) or (ball.y_pos >= window_size[1]-20):
        ball.vy = -ball.vy

    ball.move()

    pygame.draw.rect(screen, paddle.color, pygame.Rect(paddle.x_pos, paddle.y_pos, paddle.size[0], paddle.size[1]))
    pygame.draw.circle(screen, ball.color, (ball.x_pos, ball.y_pos), ball.size)
    pygame.display.flip()
    clock.tick(60)

