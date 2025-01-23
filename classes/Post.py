import pygame

from constants import *
from helpers import screen


class Post:
    username = "Yahav Geresyuk"
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = ["Yuval so handsome"]


    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        ## description:
        font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        description = font.render(self.description, True, BLACK)
        screen.blit(description, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

        ## location:
        font = pygame.font.SysFont("Calibiri", UI_FONT_SIZE)
        location = font.render(self.location, True, BLACK)
        screen.blit(location, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        ## likes:


        ## comments:
        font = pygame.font.SysFont("Arial", COMMENT_TEXT_SIZE)
        comments = font.render(self.comments[0], True, BLACK)
        screen.blit(comments, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS])



    def add_like(self):
        self.likes_counter += 1


    def add_comment(self, comment):
        self.comments.append(comment)


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont("chalkduster.ttf",
                                                   COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                                True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                        VIEW_MORE_COMMENTS_Y_POS))

            # Display 4 comments starting from comments_display_index
            for i in range(0, len(self.comments)):
                if position_index >= len(self.comments):
                    position_index = 0
                self.comments[position_index].display(i)
                position_index += 1
                if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                    break



