import pygame

from constants import FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS, \
    COMMENT_LINE_HEIGHT, UI_FONT_SIZE
from helpers import screen
class Comment:
    def __init__(self, text):
        self.comment = text


    def display(self, comment_number):
        comment_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        comment_to_display = comment_font.render(self.comment, True, (0, 0, 0))
        screen.blit(comment_to_display,
                    (FIRST_COMMENT_X_POS,
                     FIRST_COMMENT_Y_POS +
                     (comment_number * COMMENT_LINE_HEIGHT)))

