import pygame

APPLES = pygame.sprite.Group()
SNAKE = pygame.sprite.Group()
CHANGE_DIRECTION = pygame.sprite.Group()
SCORE = 0
FPS = 30
X = 110
Y = 110

class BaseSprite(pygame.sprite.Sprite):
    size = 10

    def __init__(self, x, y):
        super().__init__()
        self.image: pygame.Surface = pygame.Surface((self.size, self.size))
        self.rect: pygame.Rect = pygame.Rect((x, y, self.size, self.size))

class AppleSprite(BaseSprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((255, 0, 0))
        self.add(APPLES)
        if x == 50 and y == 10:
            AppleSprite(random.randint(0, 100 / 10) * 10,
                random.randint(0, 100 / 10) * 10)
            self.kill()
        for i in SNAKE.sprites():
            if i.rect.x == self.rect.x and i.rect.y == self.rect.y:
                AppleSprite(random.randint(0, 100 / 10) * 10,
                random.randint(0, 100 / 10) * 10)
                self.kill()

    def update(self):
        part = SNAKE.sprites()[0]
        if part.rect.x == self.rect.x and part.rect.y == self.rect.y:
            print('Yam !')
            globals()['SCORE'] += 1
            last_part = SNAKE.sprites()[-1]
            print(last_part.direction)
            SnakePartSprite(last_part.rect.x - last_part.direction[0]*self.size,
                            last_part.rect.y - last_part.direction[1]*self.size,
                            last_part.direction[0],
                            last_part.direction[1])
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {}))
            self.kill()


class SnakePartSprite(BaseSprite):
    def __init__(self, x, y, x_dir, y_dir):
        super().__init__(x, y)
        self.direction = [x_dir, y_dir]
        self.image.fill((255, 255, 255))
        self.add(SNAKE)

    def update(self):
        if 0 > self.rect.x or self.rect.x > X or 0 > self.rect.y or self.rect.y > X:
            pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
            self.kill()

        if self == SNAKE.sprites()[0]:
            for part in SNAKE.sprites()[1:]:
                if part.rect.x == self.rect.x and part.rect.y == self.rect.y:
                    pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
                    self.kill()

        for block in CHANGE_DIRECTION.sprites():
            if block.rect.x == self.rect.x and block.rect.y == self.rect.y:
                self.direction = block.direction
        if 0 <= self.rect.x <= X:
            self.rect.x += self.direction[0] * self.size
        if 0 <= self.rect.y <= Y:
            self.rect.y += self.direction[1] * self.size


