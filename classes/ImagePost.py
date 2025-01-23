from classes.Post import *
from Images import *

class ImagePost(Post):
    def __init__(self, location, description, image_src):
        super().__init__(location, description)
        self.image = pygame.image.load(image_src)
        self.image = pygame.transform.scale(self.image,
                             (POST_WIDTH, POST_HEIGHT))

    def set_image(self, image_src):
        self.image = pygame.image.load(image_src)
        self.image = pygame.transform.scale(self.image,
                                        (POST_WIDTH, POST_HEIGHT))

    def default_an_image(self):
        self.image = pygame.image.load("Images/ronaldo.jpg")
        self.image = pygame.transform.scale(self.image,
                                            (POST_WIDTH, POST_HEIGHT))

    def display(self):
        super().display()
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))