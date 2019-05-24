# Video 5 - How to draw on the screen (Sprites and drawing shapes using pygame)

import pygame

# Initialize PyGame and draw game surface
pygame.init()
game_display = pygame.display.set_mode((800,600))


pygame.display.set_caption("Slither - by thenewboston")     # Changes the title of the display window
game_exit = False

# Define colors using rgb values - can use list or tuple


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



while not game_exit:        # begin the main game loop

    # creates the event handling
    for event in pygame.event.get():
        print (event)

        # event processing
        if event.type == pygame.QUIT:
            game_exit = True



    game_display.fill(blue)
    pygame.display.update()






# Exit PyGame & Python
pygame.quit()
quit()

