import pygame
class Graphics:
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.orange = (255, 165, 0)
        self.margin = 5
        self.width = 60
        self.height = 60
        window_size = [525, 575]
        self.screen = pygame.display.set_mode(window_size)

    def draw_grid(self, game):
        self.screen.fill(self.black)

        for row in range(8):
            for column in range(8):
                color = self.white
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.width)
                                  * column + self.margin,
                                  (self.margin + self.height)
                                  * row + self.margin,
                                  self.width,
                                  self.height])
        for row in range(8):
            for column in range(8):
                if game.grid[row][column] == 'X':
                    pygame.draw.ellipse(self.screen, self.orange,
                                        [(self.margin + self.width)
                                         * column + self.margin,
                                         (self.margin + self.height)
                                         * row + self.margin,
                                         60, 60])
                if game.grid[row][column] == 'O':
                    pygame.draw.ellipse(self.screen, self.red,
                                        [(self.margin + self.width)
                                         * column + self.margin,
                                         (self.margin + self.height)
                                         * row + self.margin,
                                         60, 60])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Orange:" + str(game.state['X'])
                           + " Red:" + str(game.state['O']), True, self.white)
        self.screen.blit(text, [335, 540])
        if game.move_first and game.state['Empty'] != 0:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            text = font.render('You', True, self.white)
            self.screen.blit(text, [60, 520])
            pygame.draw.ellipse(self.screen, self.orange,
                                [250, 525, 40, 40])
        elif not game.move_first and game.state['Empty'] != 0:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            text = font.render("Player 2", True, self.white)
            self.screen.blit(text, [60, 520])
            pygame.draw.ellipse(self.screen, self.red,
                                [250, 525, 40, 40])
        if game.state['Empty'] == 0:
            if game.state['X'] > game.state['O']:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("Good game!!!", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Winner human!!!", True, self.white)
                self.screen.blit(text, [60, 520])
            elif game.state['X'] < game.state['O']:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("Game over!!!", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Winner robot!!!", True, self.white)
                self.screen.blit(text, [60, 520])
            else:
                font = pygame.font.SysFont('Calibri', 60, True, False)
                text = font.render("You tried...", True, self.black)
                self.screen.blit(text, [115, 210])
                font = pygame.font.SysFont('Calibri', 50, True, False)
                text = font.render("Friendship", True, self.white)
                self.screen.blit(text, [60, 520])
