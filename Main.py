import pygame

pygame.init()

# Parameters
window_size = (720, 640)
paddle_color = (0, 128, 255)
paddle_size = [80, 10]
x_position = 310
y_position = 620
done = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: x_position -= 3
    if pressed[pygame.K_RIGHT]: x_position += 3

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, paddle_color, pygame.Rect(x_position, y_position, paddle_size[0], paddle_size[1]))

    pygame.display.flip()
    clock.tick(60)