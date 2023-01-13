import pygame

pygame.init()
size = width, height = 612, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Game')
clock = pygame.time.Clock()
FPS = 60
bg_pos = 0
bg_speed = 3
bg = pygame.image.load('data/ground.png')
sky = pygame.Surface([612, 803])
sky.fill(pygame.Color('#3ec9ff'))


running = True
while running:
    clock.tick(FPS)
    screen.blit(bg, (bg_pos, 800))
    bg_pos -= bg_speed
    if bg_pos < -40:
        bg_pos = 0
    screen.blit(sky, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
