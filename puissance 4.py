import pygame
import sys
from random import *
import time
pygame.init()
p = 1
x = 0
y = 0
az = 2
fin = 0
scorej1 = 0
scorej2 = 0
manche = 1
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 250, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
BLEU2 = (12, 168, 235)
VIOLET = (212, 12, 235)
jaune = (225, 227, 12)
print('Rentrez le nom du joueur 1')
j1 = input()
print('Rentrez le nom du joueur 2')
j2 = input()


def joueur(p):
    global j1
    global j2
    if p == 1:
        return j1
    else:
        return j2


def joueurf(p):
    global j1
    global j2
    if p == 1:
        return j2
    else:
        return j1


windows = pygame.display.set_mode((800, 800))
window = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont("arial", 16)
font2 = pygame.font.SysFont("arial", 30)
font3 = pygame.font.SysFont("arial", 50)

pygame.Surface.fill(window, 0)
rectangle78 = (0, 0, 800, 800)  # (00abscisse, ordonnée, largeur, hauteur
rectangle = (50, 50, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur
rectangle1 = (50, 250, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle2 = (50, 450, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle3 = (250, 50, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle4 = (250, 250, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle5 = (250, 450, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle6 = (450, 50, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle7 = (450, 250, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle8 = (450, 450, 150, 150)  # (00abscisse, ordonnée, largeur, hauteur)
rectangle_color = WHITE
rectangle1_color = WHITE
rectangle2_color = WHITE
rectangle3_color = WHITE
rectangle4_color = WHITE
rectangle5_color = WHITE
rectangle6_color = WHITE
rectangle7_color = WHITE
rectangle8_color = WHITE
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            print('Rentrez le nom du joueur 1')
            j1 = input()
            print('Rentrez le nom du joueur 2')
            j2 = input() 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            rectangle_color = WHITE
            rectangle1_color = WHITE
            rectangle2_color = WHITE
            rectangle3_color = WHITE
            rectangle4_color = WHITE
            rectangle5_color = WHITE
            rectangle6_color = WHITE
            rectangle7_color = WHITE
            rectangle8_color = WHITE
            scorej1 = 0
            scorej2 = 0
            manche = 1
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] <= 200 and pos[0] >= 50 and pos[1] <= 200 and pos[1] >= 50:
                if rectangle_color == WHITE:
                    if p == 1:
                        rectangle_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle_color = YELLOW

            if pos[0] <= 400 and pos[0] >= 250 and pos[1] <= 200 and pos[1] >= 50:
                if rectangle3_color == WHITE:
                    if p == 1:
                        rectangle3_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle3_color = YELLOW

            if pos[0] <= 600 and pos[0] >= 450 and pos[1] <= 200 and pos[1] >= 50:
                if rectangle6_color == WHITE:
                    if p == 1:
                        rectangle6_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle6_color = YELLOW

            if pos[0] <= 200 and pos[0] >= 50 and pos[1] <= 400 and pos[1] >= 250:
                if rectangle1_color == WHITE:
                    if p == 1:
                        rectangle1_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle1_color = YELLOW

            if pos[0] <= 200 and pos[0] >= 50 and pos[1] <= 600 and pos[1] >= 450:
                if rectangle2_color == WHITE:
                    if p == 1:
                        rectangle2_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle2_color = YELLOW

            if pos[0] <= 400 and pos[0] >= 250 and pos[1] <= 400 and pos[1] >= 250:
                if rectangle4_color == WHITE:
                    if p == 1:
                        rectangle4_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle4_color = YELLOW

            if pos[0] <= 600 and pos[0] >= 450 and pos[1] <= 400 and pos[1] >= 250:
                if rectangle7_color == WHITE:
                    if p == 1:
                        rectangle7_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle7_color = YELLOW

            if pos[0] <= 400 and pos[0] >= 250 and pos[1] <= 600 and pos[1] >= 450:
                if rectangle5_color == WHITE:
                    if p == 1:
                        rectangle5_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle5_color = YELLOW

            if pos[0] <= 600 and pos[0] >= 450 and pos[1] <= 600 and pos[1] >= 450:
                if rectangle8_color == WHITE:
                    if p == 1:
                        rectangle8_color = RED
                        p = 0
                    else:
                        p = 1
                        rectangle8_color = YELLOW

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    col = (r, g, b)
    col2 = 0, 0, 0
    pygame.draw.rect(window, col2, rectangle78)
    pygame.draw.rect(window, rectangle_color, rectangle)
    pygame.draw.rect(window, rectangle1_color, rectangle1)
    pygame.draw.rect(window, rectangle2_color, rectangle2)
    pygame.draw.rect(window, rectangle3_color, rectangle3)
    pygame.draw.rect(window, rectangle4_color, rectangle4)
    pygame.draw.rect(window, rectangle5_color, rectangle5)
    pygame.draw.rect(window, rectangle6_color, rectangle6)
    pygame.draw.rect(window, rectangle7_color, rectangle7)
    pygame.draw.rect(window, rectangle8_color, rectangle8)
    label = font.render("Au tour du joueur " +
                        joueur(p) + " de jouer.", True, BLUE)
    label2 = font.render("appuyez sur r pour recommencer", True, BLUE)
    label3 = font.render("le joueur " + j1 + " a " +
                         str(scorej1) + " points", True, BLUE)
    label4 = font.render("le joueur " + j2 + " a " +
                         str(scorej2) + " points", True, BLUE)
    label6 = font.render("appuyez sur c pour changer les noms dans la console", True, BLUE)
    window.blit(label, (0, 0))
    window.blit(label2, (0, 670))
    window.blit(label3, (560, 600))
    window.blit(label4, (0, 600))
    window.blit(label6, (0, 650))
    pygame.display.update()
    if rectangle_color == RED and rectangle1_color == RED and rectangle2_color == RED or rectangle_color == YELLOW and rectangle1_color == YELLOW and rectangle2_color == YELLOW:
        fin = 1

    elif rectangle_color == RED and rectangle3_color == RED and rectangle6_color == RED or rectangle_color == YELLOW and rectangle3_color == YELLOW and rectangle6_color == YELLOW:
        fin = 1

    elif rectangle1_color == RED and rectangle4_color == RED and rectangle7_color == RED or rectangle1_color == YELLOW and rectangle4_color == YELLOW and rectangle7_color == YELLOW:
        fin = 1

    elif rectangle2_color == RED and rectangle5_color == RED and rectangle8_color == RED or rectangle2_color == YELLOW and rectangle5_color == YELLOW and rectangle8_color == YELLOW:
        fin = 1

    elif rectangle3_color == RED and rectangle4_color == RED and rectangle5_color == RED or rectangle3_color == YELLOW and rectangle4_color == YELLOW and rectangle5_color == YELLOW:
        fin = 1

    elif rectangle6_color == RED and rectangle7_color == RED and rectangle8_color == RED or rectangle6_color == YELLOW and rectangle7_color == YELLOW and rectangle8_color == YELLOW:
        fin = 1

    elif rectangle_color == RED and rectangle4_color == RED and rectangle8_color == RED or rectangle_color == YELLOW and rectangle4_color == YELLOW and rectangle8_color == YELLOW:
        fin = 1

    elif rectangle6_color == RED and rectangle4_color == RED and rectangle2_color == RED or rectangle6_color == YELLOW and rectangle4_color == YELLOW and rectangle2_color == YELLOW:
        fin = 1
    elif rectangle_color != WHITE and rectangle1_color != WHITE and rectangle2_color != WHITE and rectangle3_color != WHITE and rectangle4_color != WHITE and rectangle5_color != WHITE and rectangle6_color != WHITE and rectangle7_color != WHITE and rectangle8_color != WHITE:
        fin = 2
    pygame.display.update()
    if fin == 1:
        if manche == 1:
            label5 = font3.render("Fin de la " + str(manche) +" ère manche", True, BLUE)
            window.blit(label5, (0, 100))
        elif manche == 2:
            label5 = font3.render("Fin de la " + str(manche) +" nd manche", True, BLUE)
            window.blit(label5, (0, 100))
        else:
            label5 = font3.render("Fin de la " + str(manche) +" ème manche", True, BLUE)
            window.blit(label5, (0, 100))
        pygame.display.update()
        rectangle_color = WHITE
        rectangle1_color = WHITE
        rectangle2_color = WHITE
        rectangle3_color = WHITE
        rectangle4_color = WHITE
        rectangle5_color = WHITE
        rectangle6_color = WHITE
        rectangle7_color = WHITE
        rectangle8_color = WHITE
        time.sleep(2)
        if p == 0:
            scorej1 = scorej1 + 1
        elif p == 1:
            scorej2 = scorej2 + 1
        manche = manche + 1
    elif fin == 2:
        label6 = font3.render("Égalité", True, BLUE)
        window.blit(label6, (300, 100))  
        pygame.display.update()   
        rectangle_color = WHITE
        rectangle1_color = WHITE
        rectangle2_color = WHITE
        rectangle3_color = WHITE
        rectangle4_color = WHITE
        rectangle5_color = WHITE
        rectangle6_color = WHITE
        rectangle7_color = WHITE
        rectangle8_color = WHITE  
        time.sleep(2)
        manche = manche + 1

    fin = 0
    pygame.Surface.fill(window, 0)

# az = az * az
# print(az)
