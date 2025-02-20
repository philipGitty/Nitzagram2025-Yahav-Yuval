import pygame

from classes.Comment import Comment
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
        self.comments = []
        self.comments_display_index = 0


    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        ## description:
        # display description
        description_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE, bold=True)
        description_to_display = description_font.render(self.description,
                                                         True, (50, 50, 50))
        screen.blit(description_to_display, (DESCRIPTION_TEXT_X_POS,
                                             DESCRIPTION_TEXT_Y_POS))

        ## location:
        font = pygame.font.SysFont("Calibiri", UI_FONT_SIZE)
        location = font.render(self.location, True, BLACK)
        screen.blit(location, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

        ## likes:
        like_text = "Liked by " + str(self.likes_counter) + " users"
        like_text_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        like_to_display = like_text_font.render(like_text, True, (0, 0, 0))
        screen.blit(like_to_display, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        if len(self.comments) > 0:
            self.display_comments()


    def add_like(self):
        self.likes_counter += 1


    def add_comment(self, comment):
        new_comment = Comment(comment)
        self.comments.append(new_comment)


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


    def reset_comments_display_index(self):
        self.comments_display_index = 0


    def view_more_comments(self):
        if self.comments_display_index >= len(self.comments) - 1:
            self.comments_display_index = 0
        else:
            self.comments_display_index += 1