import pygame

pygame.init()
size = width, height = 612, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Game')
clock = pygame.time.Clock()
FPS = 60
bg_pos = 0
bg_speed = 4
bg_1 = pygame.image.load('data/background.png')
bg_2 = pygame.image.load('data/background.png')
sky = pygame.Surface([612, 533])
sky.fill(pygame.Color('#3ec9ff'))


running = True
while running:
    clock.tick(FPS)
    screen.blit(bg_1, (bg_pos, 533))
    bg_pos -= bg_speed
    screen.blit(sky, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
