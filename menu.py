from numpy import size
import pygame
import pygame_menu
import cv2

cap = cv2.VideoCapture(0) 
pygame.init()
size = (600,400)

surface = pygame.display.set_mode((780, 540), pygame.RESIZABLE)
menu = pygame_menu.Menu('Welcome', 780, 540,theme=pygame_menu.themes.THEME_SOLARIZED)
help_menu = pygame_menu.Menu('Help', 780, 540, theme=pygame_menu.themes.THEME_SOLARIZED)



def video():
    while (True):
        _, frame = cap.read()
        cv2.imshow('frame', frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

menu.add.button('Camera', video)
menu.add.button('New File')
menu.add.button('Answers')
menu.add.button('Print Scores')
menu.add.button('Help', help_menu)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(surface)

