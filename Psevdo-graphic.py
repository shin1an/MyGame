import pygame
import sys

pygame.init()
pygame.display.set_caption('Reversy')


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 186, 254)
red = (255, 0, 0)
margin = 5
width = 80
height = 80
win = pygame.display.set_mode((685, 800))

run = True
while run:
    #pygame.draw.rect(700)
    for row in range(8):
        for column in range(8):
            color = white
            pygame.draw.rect(win,
                                color,
                                 [(margin + width)
                                  * column + margin,
                                  (margin + height)
                                  * row + margin,
                                  width,
                                  height])
    row = 4
    column = 4
    pygame.draw.ellipse(win, red,
                                        [(margin + width)
                                         * column + margin,
                                         (margin + height)
                                         * row + margin,
                                         80, 80])
    
    row = 3
    column = 3
    pygame.draw.ellipse(win, red,
                                        [(margin + width)
                                         * column + margin,
                                         (margin + height)
                                         * row + margin,
                                         80, 80])
    row = 3
    column = 4
    pygame.draw.ellipse(win, black,
                                        [(margin + width)
                                         * column + margin,
                                         (margin + height)
                                         * row + margin,
                                         80, 80])


    row = 4
    column = 3
    pygame.draw.ellipse(win, black,
                                        [(margin + width)
                                         * column + margin,
                                         (margin + height)
                                         * row + margin,
                                         80, 80])    
                                         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()


    pygame.display.flip()
    
pygame.quit()
