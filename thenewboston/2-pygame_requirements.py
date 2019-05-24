# SKELETON & REQUIREMENTS OF PYGAME

import pygame

pygame.init()           # initializes all the pygame module

game_display = pygame.display.set_mode((800,600),)      # This is the game surface or canvas
    # first param MUST be a tuple or a list

pygame.display.update()         # can also interchange with pygame.display.flip.

## Think of flip like a flipbook.  Motion is just a percieved motion using various frames and flipped through.  Flip updates entire surface at once.
# Update only updates the parameters that are indicated in the call.


pygame.quit()       # un-initializes pygame library
quit()              # exits out of python