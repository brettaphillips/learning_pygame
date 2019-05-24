# Video 13 - Replace hardcoded values with variables

import pygame

game_exit = False

# Define colors using rgb values - can use list or tuple
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Environment Variables
display_width = 800
display_height = 600
fps = 15

block_size = 10     # this also controls movement speed since

lead_x = display_width /2  # (0,0) for head of snake starts
lead_y = display_height / 2

lead_x_change = 0   # initialize variables to not move
lead_y_change = 0





# Initialize PyGame and draw game surface
pygame.init()
game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither - by thenewboston")     # Changes the title of the display window
clock = pygame.time.Clock()



# begin the main game loop

while not game_exit:

    # creates the event handling
    for event in pygame.event.get():
        print (event)

        # event processing
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= block_size
                lead_y_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_RIGHT:
                lead_x_change += block_size
                lead_y_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_UP:
                lead_y_change -= block_size
                lead_x_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_DOWN:
                lead_y_change += block_size
                lead_x_change = 0                   # Prevent diagonal movement

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0


    # Boundaries - Exit game if you go off screen

    if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
        game_exit = True



    # clear the screen
    game_display.fill(white)

    lead_x += lead_x_change
    lead_y += lead_y_change
    pygame.draw.rect(game_display,black, [lead_x,lead_y,block_size, block_size])



    pygame.display.update()

    clock.tick(fps)







# Exit PyGame & Python
pygame.quit()
quit()

