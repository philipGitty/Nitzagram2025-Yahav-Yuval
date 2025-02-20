import pygame

from buttons import like_button, comment_button, click_post_button, \
    view_more_comments_button
from classes.ImagePost import ImagePost
from classes.Post import Post
from classes.TextPost import TextPost
from constants import *
from helpers import screen, mouse_in_button, read_comment_from_user


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption("Nitzagram")

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load("Images/background.png")
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    nati_pov = TextPost("Paris", "A nice post to our world!", BLACK, LIGHT_GRAY, "Hi Nati!")
    ronaldo = ImagePost("England", "Happy Birthday!", "Images/ronaldo.jpg")
    noa_camel = ImagePost("Desert", "Love Beer Sheva", "Images/noa_kirel.jpg")

    post_list = [nati_pov, ronaldo, noa_camel]
    # Position var is the post number in the list that now display
    current_index = 0
    # The presented post, hold the Post object that now display
    current_post = post_list[current_index]

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse pressed events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position (x,y) of the mouse press
                pos = event.pos
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                # If the mouse pressed on the add comment icon
                elif mouse_in_button(comment_button, pos):
                    comment_to_add = read_comment_from_user()
                    current_post.add_comment(comment_to_add)
                # If the mouse pressed on the Image - change Image event
                elif mouse_in_button(click_post_button, pos):
                    # If the presented post is the last post in the list,
                    # Change to the first post in the list
                    if current_index == len(post_list) - 1:
                        current_index = 0
                    else:
                        current_index += 1
                    current_post = post_list[current_index]
                    current_post.reset_comments_display_index()
                elif mouse_in_button(view_more_comments_button, pos):
                    current_post.view_more_comments()

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()
