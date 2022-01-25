import pygame
from ball import Ball
from random import randint
import sys
from okno import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDesktopWidget



pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

f = pygame.font.SysFont('arial', 30)

x = 962
y = 586
sc = pygame.display.set_mode((x, y))



hp3 = pygame.image.load("3.png").convert()
hp2 = pygame.image.load("2.png").convert()
hp1 = pygame.image.load("1.png").convert()
bg = pygame.image.load("1620711637_14-phonoteka_org-p-shakhta-fon-18.mWXGf.jpg").convert()
scoree = pygame.image.load('score_fon.png').convert_alpha()
vagon = pygame.image.load("png-clipart-coal-mining-minecart-shaft-mining-mines-miscellaneous-angle.IqMwr.png").convert_alpha()
sobiralka = vagon.get_rect(centerx=x//2, bottom=y-5)

line = pygame.image.load("line.reoqJ.png").convert_alpha()
hpp = line.get_rect(centerx=x//2, bottom=y)



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
    x = randint(20, y-20)
    speed = randint(1, 10)

    return Ball(x, y, speed, balls_surf[indx], balls_data[indx]['score'], group)


createBall(balls)
speed = 10

def score():

    global game_score
    for ball in balls:
        if sobiralka.collidepoint(ball.rect.center):
            game_score += ball.score
            ball.kill()




def print(message,font_color = (0, 0, 0), font_type = "PFAgoraSlabPro Bold.ttf", font_size = 500):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    bg.blit(text, (300, 300))

def pobeda():
    paused = True
    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

def pause():
    paused = True
    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pygame.display.update()
            clock.tick(15)
            paused = False

def close_game():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        exit()






while True:

    if game_score >= 50000:
        print("Pobeda")
        pobeda()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()

    if keys[pygame.K_LEFT]:
        sobiralka.x -= speed
        if sobiralka.x < 0:
            sobiralka.x = 0
    elif keys[pygame.K_RIGHT]:
        sobiralka.x += speed
        if sobiralka.x > x-sobiralka.width:
            sobiralka.x = x-sobiralka.width




    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(scoree, (0, 0))



    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    sc.blit(vagon, sobiralka)
    pygame.display.update()
    close_game()

    clock.tick(FPS)

    balls.update(y)
    score()









