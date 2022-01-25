import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)

    def update(self, *args):
        hp = 3
        if self.rect.y < args[0] - 60:
            self.rect.y += self.speed

        else:
            self.kill()
            hp -= 1
