# Video 4 - More Events

import pygame

# Initialize PyGame and draw game surface
pygame.init()
game_display = pygame.display.set_mode((800,600))
pygame.display.update()


pygame.display.set_caption("Slither - by thenewboston")     # Changes the title of the display window
game_exit = False



while not game_exit:        # begin the main game loop

    # creates the event handling
    for event in pygame.event.get():
        print (event)

        # begin logic about snake
        if event.type == pygame.QUIT:           #if they close the game window
            game_exit = True







# Exit PyGame & Python
pygame.quit()
quit()

