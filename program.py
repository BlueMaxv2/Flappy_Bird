import pygame
import random

pygame.init()
size = width, height = 580, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Game')
clock = pygame.time.Clock()
FPS = 60
bg_pos = 0
bg_speed = 3
game_over = False
can_fly = True
pipe_gap = 150
score = 0
scorer = False
font = pygame.font.SysFont('leelawadeeui', 65)
bg = pygame.image.load('data/ground.png')
sky = pygame.Surface([612, 403])
sky.fill(pygame.Color('#00a2e8'))
top_pipe_image = pygame.image.load('data/pipe.png')
bottom_pipe_image = pygame.transform.flip(top_pipe_image, False, True)


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pressed = False
        self.frames = []
        self.cur_frame = 0
        self.counter = 0
        for i in range(1, 4):
            img = pygame.image.load(f'data/bird_{i}.png')
            self.frames.append(img)
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.fma = 0

    def update(self):
        self.fma += 0.5
        if self.fma > 9:
            self.fma = 9
        if self.rect.bottom < 394:
            self.rect.y += int(self.fma)
        if pygame.mouse.get_pressed()[0] == 1 and self.pressed is False and can_fly is True:
            self.fma -= 12
            self.pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.pressed = False

        anim_cd = 7
        self.counter += 1
        if self.counter > anim_cd:
            self.counter = 0
            self.cur_frame += 1
            if self.cur_frame >= len(self.frames):
                self.cur_frame = 0
        self.image = self.frames[self.cur_frame]


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, flipped):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/pipe.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        if flipped == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if flipped == 0:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        if not game_over:
            self.rect.x -= bg_speed
        if self.rect.x <= -width:
            self.kill()


def score_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


b_group = pygame.sprite.Group()
p_group = pygame.sprite.Group()
bird = Bird(100, height / 2)
b_group.add(bird)
counter = 0

running = True
while running:
    clock.tick(FPS)
    screen.blit(sky, (0, 0))
    p_group.draw(screen)
    p_group.update()
    screen.blit(bg, (bg_pos, 400))
    if len(p_group) > 0:
        if b_group.sprites()[0].rect.left > p_group.sprites()[0].rect.left and b_group.sprites()[0].rect.right < \
                p_group.sprites()[0].rect.right and scorer is not True:
            scorer = True
        if scorer is True:
            if b_group.sprites()[0].rect.left > p_group.sprites()[0].rect.right and game_over == False:
                score += 1
    score_text(str(score), font, (0, 0, 0), 20, 400)
    if pygame.sprite.groupcollide(b_group, p_group, False, False) or bird.rect.top < 0:
        game_over = True
        can_fly = False
    if not game_over:
        bg_pos -= bg_speed
        timer = 120
        counter += 1
        pipe_random = random.randint(0, 150)
        if counter > timer:
            counter = 0
            bot_pipe = Pipe(650, int(height / 2) - pipe_random, 0)
            top_pipe = Pipe(650, int(height / 2) - pipe_random, 1)
            p_group.add(top_pipe)
            p_group.add(bot_pipe)
        if bg_pos < -40:
            bg_pos = 0
    b_group.draw(screen)
    b_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
