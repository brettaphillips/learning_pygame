# Video 7 - How to move drawings using the keyboard

import pygame

# Initialize PyGame and draw game surface
pygame.init()
game_display = pygame.display.set_mode((800,600))


pygame.display.set_caption("Slither - by thenewboston")     # Changes the title of the display window
game_exit = False

lead_x = 300  # of groups of blocks (head of the snake)
lead_y = 300



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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            elif event.key == pygame.K_RIGHT:
                lead_x += 10


    # clear the screen
    game_display.fill(white)


    pygame.draw.rect(game_display,black, [lead_x,lead_y,10, 100])



    pygame.display.update()






# Exit PyGame & Python
pygame.quit()
quit()

