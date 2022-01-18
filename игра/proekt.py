import pygame
from ball import Ball
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

f = pygame.font.SysFont('arial', 30)

W = 962
H = 586
sc = pygame.display.set_mode((W, H))

hp3 = pygame.image.load("3.png").convert()
hp2 = pygame.image.load("2.png").convert()
hp1 = pygame.image.load("1.png").convert()
bg = pygame.image.load("1620711637_14-phonoteka_org-p-shakhta-fon-18.mWXGf.jpg").convert()
score = pygame.image.load('score_fon.png').convert_alpha()
vagon = pygame.image.load("png-clipart-coal-mining-minecart-shaft-mining-mines-miscellaneous-angle.IqMwr.png").convert_alpha()
t_rect = vagon.get_rect(centerx=W//2, bottom=H-5)

clock = pygame.time.Clock()
FPS = 60
game_score = 0
hp = 3


balls_data = ({'path': "CopperOre_128.png", 'score': 100},
              {'path': "gold.png", 'score': 150},
              {'path': 'diamond.png', 'score': 200})

balls_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]

balls = pygame.sprite.Group()


def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speed = randint(1, 4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


createBall(balls)
speed = 10

def collideBalls():

    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()


def print(message,font_color = (0, 0, 0), font_type = "PFAgoraSlabPro Bold.ttf", font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    bg.blit(text, (300, 300))


def pause():
    paused = True
    while paused:
        print("Paused. Press enter to continue")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pygame.display.update()
            clock.tick(15)
            paused = False

def minus_hp():
    if hp == 3:
        sc.blit(hp3, (720, 0))
    elif hp == 2:
        sc.blit(hp2, (720, 0))
    elif hp == 1:
        sc.blit(hp1, (720, 0))






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()

    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width

    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(score, (0, 0))
    minus_hp()
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    sc.blit(vagon, t_rect)
    pygame.display.update()


    clock.tick(FPS)

    balls.update(H)
    collideBalls()






