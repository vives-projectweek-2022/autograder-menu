from numpy import size
import pygame
import pygame.camera
import pygame_menu
# import cv2

# vid = cv2.VideoCapture(0)
  
# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
  
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
      
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


pygame.init()
pygame.camera.init()



cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
size = (600,400)

surface = pygame.display.set_mode((1920, 1280), pygame.RESIZABLE)
snapshot = pygame.surface.Surface(size, 0, surface)
menu = pygame_menu.Menu('Welcome', 1540,845,theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.button('Camera', cam.start())
menu.add.button('New File')
menu.add.button('Answers')
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(surface)