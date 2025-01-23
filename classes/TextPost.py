from classes.Post import *

class TextPost(Post):
    background = ()
    def __init__(self, location, description, text):
        super().__init__(location, description)
        font = pygame.font.SysFont("Calibiri", UI_FONT_SIZE)
        self.text = font.render(self.location, True, BLACK)


    def change_text(self, text):
        self.text = "Goo Goo Gaa Gaa"

    def display(self):
        super().display()
        screen.blit(self.text, (POST_X_POS, POST_Y_POS))