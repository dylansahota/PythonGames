import random
import time
import pygame

# Initializes PyGame packages
pygame.init()

# Sets screen dimensions
screenWidth = 800
screenHeight = 900
window_dimensions = (screenWidth,screenHeight)

# Sets colours to be used
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,128,0)
blue = (0,0,255)
grey = (169,169,169)
yellow = (255,255,0)
cyan = (0,255,255)
orange = (255,140,0)
purple = (128,0,128)

# Sets Clock
clock = pygame.time.Clock()

# Creates window and caption of game
window = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("Tetris")

# Creats fonts to be used for text
titlefont = pygame.font.SysFont('Helvetica', 100)
bigfont = pygame.font.SysFont('Helvetica', 50)
smallfont = pygame.font.SysFont('Helvetica', 45)
numberfont = pygame.font.SysFont('Helvetica', 200)

# Function to draw O block
def drawOblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 2, height * 2])

# Functions to draw I block including rotation
def drawIblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 4])

def drawIblockrotate(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 4, height])

# Functions to draw Z block including rotation
def drawZblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 2, height])
    pygame.draw.rect(window, color, [xcoord + width, ycoord + height, width * 2, height])

def drawZblockrotate(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 2])
    pygame.draw.rect(window, color, [xcoord - width, ycoord + height, width, height * 2])

# Functions to draw S block including rotation
def drawSblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 2, height])
    pygame.draw.rect(window, color, [xcoord - width, ycoord + height, width * 2, height])

def drawSblockrotate(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 2])
    pygame.draw.rect(window, color, [xcoord + width, ycoord + height, width, height * 2])

# Functions to draw L block including rotations
def drawLblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 3])
    pygame.draw.rect(window, color, [xcoord + width, ycoord + (height * 2) , width, height])

def drawLblock90rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 3, height])
    pygame.draw.rect(window, color, [xcoord, ycoord + height, width, height])

def drawLblock180rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])
    pygame.draw.rect(window, color, [xcoord + width, ycoord, width, height * 3])

def drawLblock270rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])
    pygame.draw.rect(window, color, [xcoord - (width * 2), ycoord + height, width * 3, height])

# Functions to draw J block including rotations
def drawJblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord + width, ycoord, width, (height * 3)])
    pygame.draw.rect(window, color, [xcoord, ycoord + (height * 2) , width, height])

def drawJblock90rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])
    pygame.draw.rect(window, color, [xcoord, ycoord + height, width * 3, height])

def drawJblock180rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])
    pygame.draw.rect(window, color, [xcoord - width, ycoord, width, height * 3])

def drawJblock270rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width * 3, height])
    pygame.draw.rect(window, color, [xcoord + (width * 2), ycoord + height, width, height])

# Functions to draw T block including rotations
def drawTblock(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height])
    pygame.draw.rect(window, color, [xcoord - width, ycoord + height, width * 3, height])

def drawTblock90rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 3])
    pygame.draw.rect(window, color, [xcoord + width, ycoord + height, width, height])

def drawTblock180rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord - width, ycoord, width * 3, height])
    pygame.draw.rect(window, color, [xcoord, ycoord + height, width, height])

def drawTblock270rotation(xcoord, ycoord, width, height, color):
    pygame.draw.rect(window, color, [xcoord, ycoord, width, height * 3])
    pygame.draw.rect(window, color, [xcoord - width, ycoord + height, width, height])

def drawLandedPiece(xcoord,ycoord,color):
    pygame.draw.rect(window, color, [xcoord, ycoord, 40, 40])

def drawClearBoard():
    pygame.draw.rect(window, black, [200,100,400,800])

def drawClearNextPieceBox():
    pygame.draw.rect(window, black, [615,100,170,250])

def drawClearHoldPieceBox():
    pygame.draw.rect(window, black, [15,100,170,250])

def drawClearLevelbox():
    pygame.draw.rect(window, black, [615,600,170,200])

def drawClearLinesbox():
    pygame.draw.rect(window, black, [15,600,170,200])


def drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord):
    if current_piece == "O":
        drawOblock(xcoord,ycoord,40,40,black)
    elif current_piece == "I":
        if (rangle == 0 or rangle == 180):
            drawIblock(xcoord,ycoord,40,40,black)
        elif (rangle == 90 or rangle == 270):
            drawIblockrotate(xcoord,ycoord,40,40,black)
    elif current_piece == "Z":
        if (rangle == 0 or rangle == 180):
            drawZblock(xcoord,ycoord,40,40,black)
        elif (rangle == 90 or rangle == 270):
            drawZblockrotate(xcoord,ycoord,40,40,black)
    elif current_piece == "S":
        if (rangle == 0 or rangle == 180):
            drawSblock(xcoord,ycoord,40,40,black)
        elif (rangle == 90 or rangle == 270):
            drawSblockrotate(xcoord,ycoord,40,40,black)
    elif current_piece == "L":
        if rangle == 0:
            drawLblock(xcoord,ycoord,40,40,black)
        elif rangle == 90:
            drawLblock90rotation(xcoord,ycoord,40,40,black)
        elif rangle == 180:
            drawLblock180rotation(xcoord,ycoord,40,40,black)
        elif rangle == 270:
            drawLblock270rotation(xcoord,ycoord,40,40,black)
    elif current_piece == "J":
        if rangle == 0:
            drawJblock(xcoord,ycoord,40,40,black)
        elif rangle == 90:
            drawJblock90rotation(xcoord,ycoord,40,40,black)
        elif rangle == 180:
            drawJblock180rotation(xcoord,ycoord,40,40,black)
        elif rangle == 270:
            drawJblock270rotation(xcoord,ycoord,40,40,black)
    elif current_piece == "T":
        if rangle == 0:
            drawTblock(xcoord,ycoord,40,40,black)
        elif rangle == 90:
            drawTblock90rotation(xcoord,ycoord,40,40,black)
        elif rangle == 180:
            drawTblock180rotation(xcoord,ycoord,40,40,black)
        elif rangle == 270:
            drawTblock270rotation(xcoord,ycoord,40,40,black)


def drawboard(lines,level):
    # Color of outlines
    color = white

    # Box to display the held piece
    pygame.draw.line(window, color, (15, 100), (185, 100), 2)
    pygame.draw.line(window, color, (15, 100), (15, 350), 2)
    pygame.draw.line(window, color, (15, 350), (185, 350), 2)
    pygame.draw.line(window, color, (185, 100), (185, 350), 2)
    pygame.draw.line(window, color, (15, 150), (185, 150), 2)

    # Text to be displayed in the held box
    holdsurface = bigfont.render('HOLD', False, white)
    window.blit(holdsurface,(52,110))

    # Box to display next piece
    pygame.draw.line(window, color, (615, 100), (785, 100), 2)
    pygame.draw.line(window, color, (615, 100), (615, 350), 2)
    pygame.draw.line(window, color, (615, 350), (785, 350), 2)
    pygame.draw.line(window, color, (785, 100), (785, 350), 2)
    pygame.draw.line(window, color, (615, 150), (785, 150), 2)

    # Text to be displayed in the next box
    holdsurface = bigfont.render('NEXT', False, white)
    window.blit(holdsurface,(655,110))

    # Box to display the score
    pygame.draw.line(window, color, (15, 600), (185, 600), 2)
    pygame.draw.line(window, color, (15, 600), (15, 800), 2)
    pygame.draw.line(window, color, (15, 800), (185, 800), 2)
    pygame.draw.line(window, color, (185, 600), (185, 800), 2)
    pygame.draw.line(window, color, (15, 650), (185, 650), 2)

    # Text to be displayed in the score box
    holdsurface = smallfont.render('LINES', False, white)
    window.blit(holdsurface,(60,612))
    if lines < 10:
        linesurface = numberfont.render("0"+str(lines), False, white)
        window.blit(linesurface,(20,660))
    else:
        linesurface = numberfont.render(str(lines), False, white)
        window.blit(linesurface,(20,660))

    # Box to display the level
    pygame.draw.line(window, color, (615, 600), (785, 600), 2)
    pygame.draw.line(window, color, (615, 600), (615, 800), 2)
    pygame.draw.line(window, color, (615, 800), (785, 800), 2)
    pygame.draw.line(window, color, (785, 600), (785, 800), 2)
    pygame.draw.line(window, color, (615, 650), (785, 650), 2)

    # Text to be displayed in the level box
    holdsurface = smallfont.render('LEVEL', False, white)
    window.blit(holdsurface,(654,613))
    if level < 10:
        levelsurface = numberfont.render("0"+str(level), False, white)
        window.blit(levelsurface,(620,660))
    else:
        levelsurface = numberfont.render(str(level), False, white)
        window.blit(levelsurface,(620,660))

    # Text to be displayed above box
    titlesurface = titlefont.render("T",False,yellow)
    window.blit(titlesurface,(275,20))
    titlesurface = titlefont.render("E",False,orange)
    window.blit(titlesurface,(315,20))
    titlesurface = titlefont.render("T",False,red)
    window.blit(titlesurface,(362,20))
    titlesurface = titlefont.render("R",False,purple)
    window.blit(titlesurface,(403,20))
    titlesurface = titlefont.render("I",False,blue)
    window.blit(titlesurface,(452,20))
    titlesurface = titlefont.render("S",False,cyan)
    window.blit(titlesurface,(470,20))

    # Draws box to play Tetris in
    pygame.draw.line(window, color, (200, 99), (600, 99), 2)
    pygame.draw.line(window, color, (200, 899), (600, 899), 2)
    pygame.draw.line(window, color, (200, 100), (200, 900), 2)
    pygame.draw.line(window, color, (600, 100), (600, 900), 2)

    # Draws vertical grid lines
    for x in range(200, 600):
        if x % 40 == 0:
            pygame.draw.line(window, grey, (x, 100), (x, 900), 1)

    # Draws horizontal grid lines
    for y in range(100,900):
        if y % 40 == 0:
            pygame.draw.line(window, grey, (200, y + 20), (600, y + 20), 1)

def gameloop():

    # Variables to allow us to loop through game and through drawing piece loop
    game_over = False
    piece_drawn = False

    # Frame Rate
    fps = 60

    #Sets initial start time to the time of the game starting
    start_time = time.time()

    # Defines variables for level and speed of pieces dropping
    level = 1
    lines = level * 5
    line_count = 0
    drop_speed = 0.5

    # Coordinates of piece which will drop at top of screen
    xcoord = 360
    ycoord = 100
    width = 40
    height = 40
    
    # Initial Rotation angle, to be incremented by 90 when someone presses the spacebar
    rangle = 0

    # Creates variable for the current piece, which will allow us to perform different manipulations given the piece we are working with
    current_piece = ""

    # Creates variables for next and held pieces
    next_piece = "blank"
    held_piece = "blank"
    held_piece_to_draw = "blank"
    held_piece_drawn = False
    piece_moving = False

    # Creates arrays for 20 rows to be drawn when piece has landed
    landedlist = [
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]],
        [[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]]
    ]

    # Draws black screen
    window.fill(black)

    # Main game loop
    while not game_over:

        # Generates random piece
        while piece_drawn == False:
            drawClearNextPieceBox()
            if next_piece == "blank":
                next_piece_chooser = random.randint(1,7)
                piece_chooser = random.randint(1,7)
            else:
                piece_chooser = next_piece_chooser
                next_piece_chooser = random.randint(1,7)
            piece_drawn = True

        # Draws current piece given randomly generated number and coordinates and current rotation
        # Calls O block function
        if piece_chooser == 1:
            drawOblock(xcoord,ycoord,width,height,yellow)
            current_piece = "O"
        # Calls I block functions
        elif piece_chooser == 2:
            if rangle == 0 or rangle == 180:
                drawIblock(xcoord,ycoord,width,height,cyan)
            elif rangle == 90 or rangle == 270:
                drawIblockrotate(xcoord,ycoord,width,height,cyan)
            current_piece = "I"
        # Calls Z block functions
        elif piece_chooser == 3:
            if rangle == 0 or rangle == 180:
                drawZblock(xcoord,ycoord,width,height,green)
            elif rangle == 90 or rangle == 270:
                drawZblockrotate(xcoord,ycoord,width,height,green)
            current_piece = "Z"
        # Calls S block functions
        elif piece_chooser == 4:
            if rangle == 0 or rangle == 180:
                drawSblock(xcoord,ycoord,width,height,red)
            elif rangle == 90 or rangle == 270:
                drawSblockrotate(xcoord,ycoord,width,height,red)
            current_piece = "S"
        # Calls L block functions
        elif piece_chooser == 5:
            if rangle == 0:
                drawLblock(xcoord,ycoord,width,height,orange)
            elif rangle == 90:
                drawLblock90rotation(xcoord,ycoord,width,height,orange)
            elif rangle == 180:
                drawLblock180rotation(xcoord,ycoord,width,height,orange)
            elif rangle == 270:
                drawLblock270rotation(xcoord,ycoord,width,height,orange)
            current_piece = "L"
        # Calls J block functions
        elif piece_chooser == 6:
            if rangle == 0:
                drawJblock(xcoord,ycoord,width,height,blue)
            elif rangle == 90:
                drawJblock90rotation(xcoord,ycoord,width,height,blue)
            elif rangle == 180:
                drawJblock180rotation(xcoord,ycoord,width,height,blue)
            elif rangle == 270:
                drawJblock270rotation(xcoord,ycoord,width,height,blue)
            current_piece = "J"
        # Calls T block functions
        elif piece_chooser == 7:
            if rangle == 0:
                drawTblock(xcoord,ycoord,width,height,purple)
            elif rangle == 90:
                drawTblock90rotation(xcoord,ycoord,width,height,purple)
            elif rangle == 180:
                drawTblock180rotation(xcoord,ycoord,width,height,purple)
            elif rangle == 270:
                drawTblock270rotation(xcoord,ycoord,width,height,purple)
            current_piece = "T"

        # Draws Next piece given randomly generated number and coordinates and current rotation
        # Calls O block function
        if next_piece_chooser == 1:
            drawOblock(662,210,width,height,yellow)
            next_piece = "O"
        # Calls I block functions
        elif next_piece_chooser == 2:
            drawIblock(680,170,width,height,cyan)
            next_piece = "I"
        # Calls Z block functions
        elif next_piece_chooser == 3:
            drawZblock(640,205,width,height,green)
            next_piece = "Z"
        # Calls S block functions
        elif next_piece_chooser == 4:
            drawSblock(680,205,width,height,red)
            next_piece = "S"
        # Calls L block functions
        elif next_piece_chooser == 5:
            drawLblock(665,185,width,height,orange)
            next_piece = "L"
        # Calls J block functions
        elif next_piece_chooser == 6:
            drawJblock(655,185,width,height,blue)
            next_piece = "J"
        # Calls T block functions
        elif next_piece_chooser == 7:
            drawTblock(683,203,width,height,purple)
            next_piece = "T"

        # Draws Held Piece
        if held_piece_to_draw == "O":
            drawOblock(62,210,width,height,yellow)
        elif held_piece_to_draw == "I":
            drawIblock(80,170,width,height,cyan)
        elif held_piece_to_draw == "Z":
            drawZblock(40,205,width,height,green)
        elif held_piece_to_draw == "S":
            drawSblock(80,205,width,height,red)
        elif held_piece_to_draw == "L":
            drawLblock(65,185,width,height,orange)
        elif held_piece_to_draw == "J":
            drawJblock(65,185,width,height,blue)
        elif held_piece_to_draw == "T":
            drawTblock(68,203,width,height,purple)

        # Creates X and Y variables which allow us to refer to landed list set of coords
        y = int(((ycoord + 20) / 40) - 2)
        x = int((xcoord / 40) - 5)

        # Moves current piece down by 1 on the grid
        if (time.time() - start_time) > drop_speed and piece_moving == False:
            piece_moving = True
            # Allows O block to move down by 1 square
            if current_piece == "O" and ycoord < 900 - height * 2:
                drawOblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                # If piece has dropped to the bottom, then it draws the O block, appends the new coords to the landed list and changes variable to make us generate a new piece
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,yellow]
                    landedlist[y+1][x] = [xcoord,ycoord + height,yellow]
                    landedlist[y][x+1] = [xcoord + width,ycoord,yellow]
                    landedlist[y+1][x+1] = [xcoord + width, ycoord + height, yellow]
                    xcoord = 360
                    ycoord = 100
                elif landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x+1] != [-10,-10,black]:
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,yellow]
                    landedlist[y+1][x] = [xcoord,ycoord + height,yellow]
                    landedlist[y][x+1] = [xcoord + width,ycoord,yellow]
                    landedlist[y+1][x+1] = [xcoord + width, ycoord + height, yellow]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "I" and (rangle == 0 or rangle == 180) and ycoord < 900 - (height * 4):
                drawIblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 4):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,cyan]
                    landedlist[y+1][x] = [xcoord,ycoord + height,cyan]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),cyan]
                    landedlist[y+3][x] = [xcoord,ycoord + (height * 3),cyan]
                    xcoord = 360
                    ycoord = 100
                elif landedlist[y+4][x] != [-10,-10,black]:
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,cyan]
                    landedlist[y+1][x] = [xcoord,ycoord + height,cyan]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),cyan]
                    landedlist[y+3][x] = [xcoord,ycoord + (height * 3),cyan]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "I" and (rangle == 90 or rangle == 270) and ycoord < (900 - height):
                drawIblockrotate(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - height:
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,cyan]
                    landedlist[y][x+1] = [xcoord + width,ycoord,cyan]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,cyan]
                    landedlist[y][x+3] = [xcoord + (width * 3),ycoord,cyan]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+1][x+1] != [-10,-10,black] or landedlist[y+1][x+2] != [-10,-10,black] or landedlist[y+1][x+3] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,cyan]
                    landedlist[y][x+1] = [xcoord + width,ycoord,cyan]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,cyan]
                    landedlist[y][x+3] = [xcoord + (width * 3),ycoord,cyan]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "Z" and (rangle == 0 or rangle == 180) and ycoord < (900 - (height * 2)):
                drawZblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,green]
                    landedlist[y][x+1] = [xcoord + width,ycoord,green]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,green]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,green]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+1][x+1] != [-10,-10,black] or landedlist[y+2][x+1] != [-10,-10,black] or landedlist[y+2][x+2] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,green]
                    landedlist[y][x+1] = [xcoord + width,ycoord,green]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,green]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,green]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "Z" and (rangle == 90 or rangle == 270) and ycoord < (900 - (height * 3)):
                drawZblockrotate(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,green]
                    landedlist[y+1][x] = [xcoord,ycoord + height,green]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,green]
                    landedlist[y+2][x-1] = [xcoord - width,ycoord + (height * 2),green]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x-1] != [-10,-10,black] or landedlist[y+3][x-1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,green]
                    landedlist[y+1][x] = [xcoord,ycoord + height,green]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,green]
                    landedlist[y+2][x-1] = [xcoord - width,ycoord + (height * 2),green]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "S" and (rangle == 0 or rangle == 180) and ycoord < (900 - (height * 2)):
                drawSblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,red]
                    landedlist[y][x+1] = [xcoord + width,ycoord,red]
                    landedlist[y+1][x] = [xcoord,ycoord + height,red]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,red]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x-1] != [-10,-10,black] or landedlist[y+1][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,red]
                    landedlist[y][x+1] = [xcoord + width,ycoord,red]
                    landedlist[y+1][x] = [xcoord,ycoord + height,red]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,red]
                    xcoord = 360
                    ycoord = 100                    
            elif current_piece == "S" and (rangle == 90 or rangle == 270) and ycoord < (900 - (height * 3)):
                drawSblockrotate(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,red]
                    landedlist[y+1][x] = [xcoord,ycoord + height,red]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,red]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord+(height*2),red]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x] != [-10,-10,black] or landedlist[y+3][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,red]
                    landedlist[y+1][x] = [xcoord,ycoord + height,red]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,red]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord+(height*2),red]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "L" and rangle == 0 and ycoord < (900 - (height * 3)):
                drawLblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),orange]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),orange]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+3][x] != [-10,-10,black] or landedlist[y+3][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),orange]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),orange]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "L" and rangle == 90 and ycoord < (900 - (height * 2)):
                drawLblock90rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y][x+1] = [xcoord + width,ycoord,orange]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x+1] != [-10,-10,black] or landedlist[y+1][x+2] != [-10,-10,black] or landedlist[y+2][x] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y][x+1] = [xcoord + width,ycoord,orange]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "L" and rangle == 180 and ycoord < (900 - (height * 3)):
                drawLblock180rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y][x+1] = [xcoord + width,ycoord,orange]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,orange]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),orange]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+3][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y][x+1] = [xcoord + width,ycoord,orange]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,orange]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),orange]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "L" and rangle == 270 and ycoord < 900 - (height * 2):
                drawLblock270rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,orange]
                    landedlist[y+1][x-2] = [xcoord - (width * 2),ycoord + height,orange]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x-1] != [-10,-10,black] or landedlist[y+2][x-2] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,orange]
                    landedlist[y+1][x] = [xcoord,ycoord + height,orange]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,orange]
                    landedlist[y+1][x-2] = [xcoord - (width * 2),ycoord + height,orange]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "J" and rangle == 0 and ycoord < 900 - (height * 3):
                drawJblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x+1] = [xcoord + width,ycoord,blue]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,blue]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),blue]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),blue]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+3][x+1] != [-10,-10,black] or landedlist[y+3][x] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x+1] = [xcoord + width,ycoord,blue] 
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,blue ]
                    landedlist[y+2][x+1] = [xcoord + width,ycoord + (height * 2),blue]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),blue]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "J" and rangle == 90 and ycoord < 900 - (height * 2):
                drawJblock90rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y+1][x] = [xcoord,ycoord + height,blue]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,blue]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,blue]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x+1] != [-10,-10,black] or landedlist[y+2][x+2] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y+1][x] = [xcoord,ycoord + height,blue]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,blue]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,blue]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "J" and rangle == 180 and ycoord < 900 - (height * 3):
                drawJblock180rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y][x-1] = [xcoord - width,ycoord,blue]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,blue]
                    landedlist[y+2][x-1] = [xcoord - width,ycoord + (height * 2),blue]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+3][x-1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y][x-1] = [xcoord - width,ycoord,blue]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,blue]
                    landedlist[y+2][x-1] = [xcoord - width,ycoord + (height * 2),blue]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "J" and rangle == 270 and ycoord < 900 - (height * 2):
                drawJblock270rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y][x+1] = [xcoord + width,ycoord,blue]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,blue]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,blue]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x] != [-10,-10,black] or landedlist[y+1][x+1] != [-10,-10,black] or landedlist[y+2][x+2] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,blue]
                    landedlist[y][x+1] = [xcoord + width,ycoord,blue]
                    landedlist[y][x+2] = [xcoord + (width * 2),ycoord,blue]
                    landedlist[y+1][x+2] = [xcoord + (width * 2),ycoord + height,blue]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "T" and rangle == 0 and ycoord < 900 - (height * 2):
                drawTblock(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,purple ]           
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x-1] != [-10,-10,black] or landedlist[y+2][x] != [-10,-10,black] or landedlist[y+2][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,purple]        
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "T" and rangle == 90 and ycoord < 900 - (height * 3):
                drawTblock90rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,purple]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),purple]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x+1] != [-10,-10,black] or landedlist[y+3][x] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x+1] = [xcoord + width,ycoord + height,purple]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),purple]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "T" and rangle == 180 and ycoord < 900 - (height * 2):
                drawTblock180rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 2):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x-1] = [xcoord - width,ycoord,purple]
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y][x+1] = [xcoord + width,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+1][x-1] != [-10,-10,black] or landedlist[y+2][x] != [-10,-10,black] or landedlist[y+1][x+1] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x-1] = [xcoord - width,ycoord,purple]
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y][x+1] = [xcoord + width,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    xcoord = 360
                    ycoord = 100
            elif current_piece == "T" and rangle == 270 and ycoord < 900 - (height * 3):
                drawTblock270rotation(xcoord,ycoord,width,height,black)
                ycoord += 40
                start_time = time.time()
                if ycoord == 900 - (height * 3):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,purple]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),purple]
                    xcoord = 360
                    ycoord = 100
                elif (landedlist[y+2][x-1] != [-10,-10,black] or landedlist[y+3][x] != [-10,-10,black]):
                    piece_drawn = False
                    held_piece_drawn = False
                    rangle = 0
                    landedlist[y][x] = [xcoord,ycoord,purple]
                    landedlist[y+1][x] = [xcoord,ycoord + height,purple]
                    landedlist[y+1][x-1] = [xcoord - width,ycoord + height,purple]
                    landedlist[y+2][x] = [xcoord,ycoord + (height * 2),purple]
                    xcoord = 360
                    ycoord = 100
            piece_moving = False

        # Draws all landed shapes
        for count in range(20):
            for position in landedlist[count]:
                drawLandedPiece(*position)

        # Loop to update score and level and speed of pieces dropping
        if lines == 0:
            drawClearLevelbox()
            level += 1
            drawClearLinesbox()
            lines = level * 5
            if drop_speed > 0.1:
                drop_speed -= 0.025

        # Piece Movement Logic
        for event in pygame.event.get():
            # Quits game if the red cross button is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Left Key Actions
                if event.key == pygame.K_LEFT:
                    # O Block Left Movements which add to the x coordinate and overwrite the currently drawn piece
                    if current_piece == "O" and xcoord > 200 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black]):
                        drawOblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    # I Block Left Movements which add to the x coordinate and overwrite the currently drawn piece    
                    elif current_piece == "I" and xcoord > 200 and (rangle == 0 or rangle == 180) and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black] and landedlist[y+3][x-1] == [-10,-10,black]):
                        drawIblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "I" and xcoord > 200 and (rangle == 90 or rangle  == 270) and landedlist[y][x-1] == [-10,-10,black]:
                        drawIblockrotate(xcoord,ycoord,width,height,black) 
                        xcoord -= 40
                    # Z Block Left Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "Z" and xcoord > 200 and (rangle == 0 or rangle == 180) and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x] == [-10,-10,black]):
                        drawZblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "Z" and xcoord > 200 + width and (rangle == 90 or rangle == 270) and (landedlist[y+1][x-1] == [-10,-10,black] and landedlist[y+1][x-2] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black]):
                        drawZblockrotate(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    # S Block Left Movements which add to the x coordinate and overwrite the currently drawn piece                    
                    elif current_piece == "S" and xcoord > 200 + width and (rangle == 0 or rangle == 180) and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-2] == [-10,-10,black]):
                        drawSblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "S" and xcoord > 200 and (rangle == 90 or rangle == 270) and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black] and landedlist[y+2][x] == [-10,-10,black]):
                        drawSblockrotate(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    # L Block Left Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "L" and xcoord > 200 and rangle == 0 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black]):
                        drawLblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "L" and xcoord > 200 and rangle == 90 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black]):
                        drawLblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "L" and xcoord > 200 and rangle == 180 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x] == [-10,-10,black] and landedlist[y+2][x] == [-10,-10,black]):
                        drawLblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "L" and xcoord > 200 + (width * 2) and rangle == 270 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-3] == [-10,-10,black]):
                        drawLblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    # J Block Left Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "J" and xcoord > 200 and rangle == 0 and (landedlist[y][x] == [-10,-10,black] and landedlist[y+1][x] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black]):
                        drawJblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "J" and xcoord > 200 and rangle == 90 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black]):
                        drawJblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "J" and xcoord > 200 + width and rangle == 180 and (landedlist[y][x-2] == [-10,-10,black] and landedlist[y+1][x-2] == [-10,-10,black] and landedlist[y+2][x-2] == [-10,-10,black]):
                        drawJblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "J" and xcoord > 200 and rangle == 270 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black]):
                        drawJblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    # T Block Left Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "T" and xcoord > 200 + width and rangle == 0 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-2] == [-10,-10,black]):
                        drawTblock(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "T" and xcoord > 200 and rangle == 90 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black]):
                        drawTblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "T" and xcoord > 200 + width and rangle == 180 and (landedlist[y][x-2] == [-10,-10,black] and landedlist[y+1][x-1] == [-10,-10,black]):
                        drawTblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40
                    elif current_piece == "T" and xcoord > 200 + width and rangle == 270 and (landedlist[y][x-1] == [-10,-10,black] and landedlist[y+1][x-2] == [-10,-10,black] and landedlist[y+2][x-1] == [-10,-10,black]):
                        drawTblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord -= 40

                # Right Key Actions
                elif event.key == pygame.K_RIGHT:
                    # O Block Right Movements which add to the x coordinate and overwrite the currently drawn piece
                    if current_piece == "O" and xcoord < 600 - (width * 2) and (landedlist[y][x+2] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black]):
                        drawOblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # I Block Right Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "I" and xcoord < 600 - width and (rangle == 0 or rangle == 180) and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black] and landedlist[y+2][x+1] == [-10,-10,black] and landedlist[y+3][x+1] == [-10,-10,black]):
                        drawIblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "I" and xcoord < 600 - (width * 4) and (rangle == 90 or rangle == 270) and landedlist[y][x+1] == [-10,-10,black]:
                        drawIblockrotate(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # Z Block Right Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "Z" and xcoord < 600 - (width * 3) and (rangle == 0 or rangle == 180) and (landedlist[y][x+2] == [-10,-10,black] and landedlist[y+1][x+3] == [-10,-10,black]):
                        drawZblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "Z" and xcoord < 600 - width and (rangle == 90 or rangle == 270) and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black] and landedlist[y+2][x+1] == [-10,-10,black]):
                        drawZblockrotate(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # S Block Right Movements which add to the x coordinate and overwrite the currently drawn piece
                    elif current_piece == "S" and xcoord < 600 - (width * 2) and (rangle == 0 or rangle == 180) and (landedlist[y][x+2] == [-10,-10,black] and landedlist[y+1][x] == [-10,-10,black]):
                        drawSblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "S" and xcoord < 600 - (width * 2) and (rangle == 90 or rangle == 270) and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black] and landedlist[y+2][x+2] == [-10,-10,black]):
                        drawSblockrotate(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # L Block Right Movements which add to the x coordinate and overwrite the currently drawn piece                        
                    elif current_piece == "L" and xcoord < 600 - (width * 2) and rangle == 0 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black] and landedlist[y+2][x+2] == [-10,-10,black]):
                        drawLblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "L" and xcoord < 600 - (width * 3) and rangle == 90 and (landedlist[y][x+3] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black]):
                        drawLblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "L" and xcoord < 600 - (width * 2) and rangle == 180 and (landedlist[y][x+2] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black] and landedlist[y+2][x+2] == [-10,-10,black]):
                        drawLblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "L" and xcoord < 600 - width and rangle == 270 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black]):
                        drawLblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # J Block Right Movements which add to the x coordinate and overwrite the currently drawn piece   
                    elif current_piece == "J" and xcoord < 600 - (width * 2) and rangle == 0 and (landedlist[y][x+2] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black] and landedlist[y+2][x+2] == [-10,-10,black]):
                        drawJblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "J" and xcoord < 600 - (width * 3) and rangle == 90 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+3] == [-10,-10,black]):
                        drawJblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "J" and xcoord < 600 - width and rangle == 180 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x] == [-10,-10,black] and landedlist[y+2][x] == [-10,-10,black]):
                        drawJblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "J" and xcoord < 600 - (width * 3) and rangle == 270 and (landedlist[y][x+3] == [-10,-10,black] and landedlist[y+1][x+3] == [-10,-10,black]):
                        drawJblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    # T Block Right Movements which add to the x coordinate and overwrite the currently drawn piece   
                    elif current_piece == "T" and xcoord < 600 - (width * 2) and rangle == 0 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black]):
                        drawTblock(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "T" and xcoord < 600 - (width * 2) and rangle == 90 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+2] == [-10,-10,black] and landedlist[y+2][x+1] == [-10,-10,black]):
                        drawTblock90rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "T" and xcoord < 600 - (width * 2) and rangle == 180 and (landedlist[y+1][x+1] == [-10,-10,black] and landedlist[y][x+2] == [-10,-10,black]):
                        drawTblock180rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                    elif current_piece == "T" and xcoord < 600 - width and rangle == 270 and (landedlist[y][x+1] == [-10,-10,black] and landedlist[y+1][x+1] == [-10,-10,black] and landedlist[y+2][x+1] == [-10,-10,black]):
                        drawTblock270rotation(xcoord,ycoord,width,height,black)
                        xcoord += 40
                # Up Key Actions (Rotating pieces by transforming coordinates and re-drawing shape to display move in official tetris way)
                elif event.key == pygame.K_UP:
                    if current_piece == 'I':
                        if rangle == 0:
                            drawIblock(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200:
                                xcoord += 40
                            elif xcoord == 600 - width:
                                xcoord -= 80
                            elif xcoord == 600 - (width * 2):
                                xcoord -= 40                                    
                            rangle += 90
                            xcoord -= 40
                            ycoord += 40
                        elif rangle == 90:
                            drawIblockrotate(xcoord,ycoord,width,height,black)
                            rangle += 90
                            xcoord += 80
                            ycoord -= 40
                        elif rangle == 180:
                            drawIblock(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200:
                                xcoord += 80
                            elif xcoord == 600 - width:
                                xcoord -= 40
                            elif xcoord == 200 + width:
                                xcoord += 40
                            rangle += 90
                            xcoord -= 80
                            ycoord += 80
                        elif rangle == 270:
                            drawIblockrotate(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 440:
                                xcoord += 80
                            rangle = 0
                            xcoord += 40
                            ycoord -= 80
                    elif current_piece == "Z":
                        if rangle == 0:
                            drawZblock(xcoord,ycoord,width,height,black)
                            rangle += 90
                            xcoord += 80                     
                        elif rangle == 90:
                            drawZblockrotate(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200 + width:
                                xcoord += 40
                            rangle += 90
                            xcoord -= 80
                            ycoord += 40
                        elif rangle == 180:
                            drawZblock(xcoord,ycoord,width,height,black)
                            rangle += 90
                            xcoord += 40
                            ycoord -= 40     
                        elif rangle == 270:
                            drawZblockrotate(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 600 - width:
                                xcoord -= 40
                            rangle = 0
                            xcoord -= 40
                    elif current_piece == "S":
                        if rangle == 0:
                            drawSblock(xcoord,ycoord,width,height,black)
                            rangle += 90
                        elif rangle == 90:
                            drawSblockrotate(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200:
                                xcoord += 40
                            rangle += 90
                            ycoord += 40
                        elif rangle == 180:
                            drawSblock(xcoord,ycoord,width,height,black)
                            rangle += 90
                            xcoord -= 40
                            ycoord -= 40
                        elif rangle == 270:
                            drawSblockrotate(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 600 - (width * 2):
                                xcoord -= 40
                            rangle = 0
                            xcoord += 40
                    elif current_piece == "L":
                        if rangle == 0:
                            drawLblock(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200:
                                xcoord += 40
                            rangle += 90
                            xcoord -= 40
                            ycoord += 40
                        elif rangle == 90:
                            drawLblock90rotation(xcoord,ycoord,width,height,black)
                            rangle += 90
                            ycoord -= 40
                        elif rangle == 180:
                            drawLblock180rotation(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 600 - (width * 2):
                                xcoord -= 40
                            rangle += 90
                            xcoord += 80
                        elif rangle == 270:
                            drawLblock270rotation(xcoord,ycoord,width,height,black)
                            rangle = 0
                            xcoord -= 40
                    elif current_piece == "J":
                        if rangle == 0:
                            drawJblock(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 600 - (width * 2):
                                xcoord -= 40
                            rangle += 90
                        elif rangle == 90:
                            drawJblock90rotation(xcoord,ycoord,width,height,black)
                            rangle += 90
                            xcoord += 80
                        elif rangle == 180:
                            drawJblock180rotation(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200 + width:
                                xcoord += 40
                            rangle += 90
                            xcoord -= 80
                            ycoord += 40
                        elif rangle == 270:
                            drawJblock270rotation(xcoord,ycoord,width,height,black)
                            rangle = 0
                            ycoord -= 40
                    elif current_piece == "T":
                        if rangle == 0:
                            drawTblock(xcoord,ycoord,width,height,black)
                            rangle += 90
                        elif rangle == 90:
                            drawTblock90rotation(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 200:
                                xcoord += 40
                            rangle += 90
                            ycoord += 40
                        elif rangle == 180:
                            drawTblock180rotation(xcoord,ycoord,width,height,black)
                            rangle += 90
                            ycoord -= 40
                        elif rangle == 270:
                            drawTblock270rotation(xcoord,ycoord,width,height,black)
                            # Bug Fix to ensure piece doesnt go out of screen when rotating
                            if xcoord == 600 - width:
                                xcoord -= 40
                            rangle = 0
                elif event.key == pygame.K_SPACE:
                    if held_piece == "blank":
                        held_piece_to_draw = current_piece
                        held_piece = current_piece
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        xcoord = 360
                        ycoord = 100
                        rangle = 0
                        piece_drawn = False
                        held_piece_drawn = True
                    elif held_piece_drawn == False:
                        drawClearHoldPieceBox()
                        held_piece_to_draw = current_piece
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        if held_piece == "O":
                            piece_chooser = 1
                        elif held_piece == "I":
                            piece_chooser = 2
                        elif held_piece == "Z":
                            piece_chooser = 3
                        elif held_piece == "S":
                            piece_chooser = 4
                        elif held_piece == "L":
                            piece_chooser = 5
                        elif held_piece == "J":
                            piece_chooser = 6
                        elif held_piece == "T":
                            piece_chooser = 7
                        held_piece = held_piece_to_draw
                        xcoord = 360
                        ycoord = 100
                        rangle = 0
                        held_piece_drawn = True
                elif event.key == pygame.K_DOWN and piece_moving == False:
                    piece_moving = True
                    if current_piece == "O" and ycoord < 900 - height * 3:
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "I" and (rangle == 0 or rangle == 180) and ycoord < 900 - (height * 5):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "I" and (rangle == 90 or rangle == 270) and ycoord < (900 - (height * 2)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "Z" and (rangle == 0 or rangle == 180) and ycoord < (900 - (height * 3)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "Z" and (rangle == 90 or rangle == 270) and ycoord < (900 - (height * 4)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "S" and (rangle == 0 or rangle == 180) and ycoord < (900 - (height * 3)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "S" and (rangle == 90 or rangle == 270) and ycoord < (900 - (height * 4)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "L" and rangle == 0 and ycoord < (900 - (height * 4)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "L" and rangle == 90 and ycoord < (900 - (height * 3)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "L" and rangle == 180 and ycoord < (900 - (height * 4)):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "L" and rangle == 270 and ycoord < 900 - (height * 3):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "J" and rangle == 0 and ycoord < 900 - (height * 4):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "J" and rangle == 90 and ycoord < 900 - (height * 3):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "J" and rangle == 180 and ycoord < 900 - (height * 4):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "J" and rangle == 270 and ycoord < 900 - (height * 3):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "T" and rangle == 0 and ycoord < 900 - (height * 3):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "T" and rangle == 90 and ycoord < 900 - (height * 4):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "T" and rangle == 180 and ycoord < 900 - (height * 3):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    elif current_piece == "T" and rangle == 270 and ycoord < 900 - (height * 4):
                        drawClearCurrentPiece(current_piece,rangle,xcoord,ycoord)
                        ycoord += 40
                    piece_moving = False
     
        # Finds any rows where there are no black spaces and sets the row back to black and the coords back to the default
        for count in range(19,0,-1):
            # Cleared out full rows from the bottom upwards
            if [-10,-10,black] not in landedlist[count]:
                # Colors board black to update it
                drawClearBoard()
                # Colors lines box in black to update it
                drawClearLinesbox()
                # Updates number of lines needed until next level
                lines -= 1
                # Deletes old full line
                landedlist.pop(count)
                # Adds new line at top
                landedlist.insert(0,[[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black],[-10,-10,black]])
            # Adds 40 to y coordinates of all other settled pieces.
                for c in range(count,0,-1):
                    for pos2 in landedlist[c]:
                        if pos2[1] != -10:
                            pos2[1] += 40
                
        # Draws board
        drawboard(lines,level)

        # Updates screen, with a 60FPS rate
        pygame.display.update()
        clock.tick(fps)
        
# Calls Game Loop
gameloop()
# Quits pygame and python
pygame.quit()
quit()