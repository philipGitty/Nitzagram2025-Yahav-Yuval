from classes.Post import *
from helpers import screen, center_text


class TextPost(Post):
    def __init__(self, location, description, bg_color, txt_color, text):
        super().__init__(location, description)
        self.bg_color = bg_color
        self.txt_color = txt_color
        self.background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        self.text = text


    def change_text(self, text):
        self.text = text

    def display(self):
        super().display()
        pygame.draw.rect(screen, self.bg_color, self.background)
        font = pygame.font.SysFont("Calibri", TEXT_POST_FONT_SIZE)
        text = font.render(self.text, True, self.txt_color)
        screen.blit(text, center_text(1, text, 0))
