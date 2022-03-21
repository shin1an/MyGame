import pygame
import pygame_menu

import PlayWithRobot

pygame.init()
play = PlayWithRobot.Play()

surface = pygame.display.set_mode((800, 600))

def start_the_game():
    play.play_game()
    pass

menu = pygame_menu.Menu('Hello', 500, 600, 
                        theme=pygame_menu.themes.THEME_DARK)

menu.add.text_input('Name :', indicult_name='')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)