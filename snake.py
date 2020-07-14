import pygame
import random
import time

# Initializes PyGame packages
pygame.init()

# Sets screen dimensions
screenWidth = 691
screenHeight = 691
window_dimensions = (screenWidth,screenHeight)

# Sets colours to be used
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (169,169,169)

# Sets Clock
clock = pygame.time.Clock()

# Creates window and caption of game
window = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("Snake")

# Function which creates snake body, by looping through a list of coordinates
def createbody(snake_position,width,height,color):
    for position in snake_position:
        pygame.draw.rect(window, color, [position[0], position[1], width, height])

# Function which creates grid lines for game
def createlines(xcoord,ycoord,width,height,color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])

# Function which creates the food which the snake chases
def createfood(xcoord,ycoord,color):
    pygame.draw.circle(window,color,[xcoord,ycoord],6)

# Rounds any number to the nearest 15
def myround(x, base=15):
    return int(base * round(float(x)/base))

# Creates a random number that is used as the x and y coordinates of the food, which is placed randomly in the game
def foodcoordgenerator():
    return (myround(random.randint(45,660)) + 8)

# game loop
def gameloop():

    # Creates variable to allow game to loop
    dead = False

    # Creates variables to control movement of snake
    x_move = 0
    y_move = 0

    # Create variables for the size of the body of snake
    width = 15
    height = 15

    # Creating variable to count food eaten
    eaten = 0

    # Create variables of food for snake (we add 8 so that it centers the food in the middle of the cell)
    foodxcoord = foodcoordgenerator()
    foodycoord = foodcoordgenerator()

    # Sets variable at the starting bottom frame rate, to increase ever time the food is eaten
    fps = 14

    # Drawing Snake
    snake_position = [[90,90]]
    snake_head = snake_position[0]

    direction = 'Z'

    while not dead:

        # Changes variable to true if the person presses X, allowing us to break out of the loop and end the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = - 15
                    y_move = 0
                    direction = 'L'
                elif event.key == pygame.K_RIGHT:
                    x_move = 15
                    y_move = 0
                    direction = 'R'
                elif event.key == pygame.K_DOWN:
                    y_move = 15
                    x_move = 0
                    direction = 'D'
                elif event.key == pygame.K_UP:
                    y_move = -15
                    x_move = 0
                    direction = 'U'
    
        snake_head[0] += x_move
        snake_head[1] += y_move

        # Adds the value of the snake head to the snake ID array and removes the last value in the array
        snake_position.insert(0,list(snake_head))
        snake_position.pop()
        
        # Updates screen to make it black
        window.fill(black)

        # Draws grid lines
        for count in range(700):
            if count % 15 == 0:
                createlines(count,0,1,700,grey)
                createlines(0,count,700,1,grey)
         
        # Loop to see if snake has eaten the food, changes coordinates of food, updates eaten by 1 and increases FPS by 1
        if snake_head[0] == foodxcoord-8 and snake_head[1] == foodycoord-8:
            eaten += 1
            fps += 0.5
            if direction == 'L':
                snake_position.append([(foodxcoord-8)-(eaten * 15),foodycoord-8])
            if direction == 'R':
                snake_position.append([(foodxcoord-8)+(eaten * 15),foodycoord-8])
            if direction == 'U':
                snake_position.append([foodxcoord-8,(foodycoord-8)-(eaten * 15)])
            if direction == 'D':
                snake_position.append([foodxcoord-8,(foodycoord-8)+(eaten * 15)])
            # Creates new coordinates for food once snake has eaten food in first position
            foodxcoord = foodcoordgenerator()
            foodycoord = foodcoordgenerator()

        # Loop to restart game if we go out of bounds
        if snake_head[0] < 0 or snake_head[0] + width > screenWidth or snake_head[1] < 0 or snake_head[1] + height > screenHeight:
            time.sleep(1)
            gameloop()

        # Loop to restart game if we crash into our body
        for pos in range(len(snake_position)):
            if pos == 0:
                continue
            elif snake_head == snake_position[pos]:
                time.sleep(1)
                gameloop()

        # Creates body and food of snake over black screen in new position
        body = createbody(snake_position,width,height,red)
        food = createfood(foodxcoord,foodycoord,green)
            
        # Updates screen, with a 60FPS rate
        pygame.display.update()
        clock.tick(fps)
        
# Calls Game Loop
gameloop()
# Quits pygame and python
pygame.quit()
quit()