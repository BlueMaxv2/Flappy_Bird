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
sky.fill(pygame.Color('#00a2e8'))


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_num = 0
        self.counter = 0
        for i in range(1, 4):
            img = pygame.image.load(f'data/bird_{i}.png')
            self.frames.append(img)
        self.image = self.frames[self.frame_num]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        anim_cd = 7
        self.counter += 1
        if self.counter > anim_cd:
            self.counter = 0
            self.frame_num += 1
            if self.frame_num >= len(self.frames):
                self.frame_num = 0
        self.image = self.frames[self.frame_num]


b_group = pygame.sprite.Group()
bird = Bird(100, 450)
b_group.add(bird)

running = True
while running:
    clock.tick(FPS)
    screen.blit(bg, (bg_pos, 800))
    b_group.draw(screen)
    b_group.update()
    bg_pos -= bg_speed
    if bg_pos < -40:
        bg_pos = 0
    screen.blit(sky, (0, 0))
    b_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
