import time
from enitity import *
import random
from logs.log import save

pygame.init()
surface = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT + 1, 200)

if __name__ == '__main__':
    SnakePartSprite(random.randint(0, 10) * 10,
                    random.randint(0, 10) * 10,
                    0,
                    0)
    AppleSprite(random.randint(0, 100 / 10) * 10,
                random.randint(0, 100 / 10) * 10)
    end_game = pygame.font.SysFont(None, 36)
    while True:
        surface.fill((0, 0, 0))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                save([SCORE, len(SNAKE.sprites())])
                surface.blit(end_game.render('SCORE {}'.format(len(SNAKE.sprites())), 1, (0, 255, 0)), (0, 50))
                pygame.display.update()
                time.sleep(10)
                quit()
            if i.type == pygame.USEREVENT:
                a = AppleSprite(random.randint(0, 10) * 10, random.randint(0, 10) * 10)
                save([a.rect.x, a.rect.y])
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    ChangeDirectionSprite(SNAKE.sprites()[0].rect.x, SNAKE.sprites()[0].rect.y, -1, 0)
                if i.key == pygame.K_RIGHT:
                    ChangeDirectionSprite(SNAKE.sprites()[0].rect.x, SNAKE.sprites()[0].rect.y, 1, 0)
                if i.key == pygame.K_UP:
                    ChangeDirectionSprite(SNAKE.sprites()[0].rect.x, SNAKE.sprites()[0].rect.y, 0, -1)
                if i.key == pygame.K_DOWN:
                    ChangeDirectionSprite(SNAKE.sprites()[0].rect.x, SNAKE.sprites()[0].rect.y, 0, 1)
            if i.type == pygame.USEREVENT + 1:
                SNAKE.update()
        APPLES.update()
        CHANGE_DIRECTION.update()

        CHANGE_DIRECTION.draw(surface)
        APPLES.draw(surface)
        SNAKE.draw(surface)
        pygame.display.update()
        clock.tick(FPS)

