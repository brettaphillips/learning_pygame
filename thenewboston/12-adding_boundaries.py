# Video 12 - Adding boundaries

import pygame

# Initialize PyGame and draw game surface
pygame.init()
game_display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Slither - by thenewboston")     # Changes the title of the display window
clock = pygame.time.Clock()


game_exit = False

# Define colors using rgb values - can use list or tuple
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



lead_x = 300  # of groups of blocks (head of the snake)
lead_y = 300
lead_x_change = 0
lead_y_change = 0


while not game_exit:        # begin the main game loop

    # creates the event handling
    for event in pygame.event.get():
        print (event)

        # event processing
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 10
                lead_y_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_RIGHT:
                lead_x_change += 10
                lead_y_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_UP:
                lead_y_change -= 10
                lead_x_change = 0                   # Prevent diagonal movement
            elif event.key == pygame.K_DOWN:
                lead_y_change += 10
                lead_x_change = 0                   # Prevent diagonal movement

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0


    # Boundaries - Exit game if you go off screen

    if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0:
        game_exit = True



    # clear the screen
    game_display.fill(white)

    lead_x += lead_x_change
    lead_y += lead_y_change
    pygame.draw.rect(game_display,black, [lead_x,lead_y,10, 10])



    pygame.display.update()

    clock.tick(15)







# Exit PyGame & Python
pygame.quit()
quit()

