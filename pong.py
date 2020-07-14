import pygame

# Initializes PyGame packages
pygame.init()

# Sets screen dimensions
screenWidth = 1200
screenHeight = 800
window_dimensions = (screenWidth,screenHeight)

# Sets colours to be used
black = (0,0,0)
white = (255,255,255)
grey = (169,169,169)

# Creats fonts to be used for text
numberfont = pygame.font.SysFont('Helvetica', 200)

# Sets Clock
clock = pygame.time.Clock()

# Creates window and caption of game
window = pygame.display.set_mode(window_dimensions)
pygame.display.set_caption("Pong")

def drawboard(p1score,p2score):
    # Defines width of line in middle of screen
    width = 10

    # Defines surfaces for player scores
    p1surface = numberfont.render(str(p1score), False, white)
    p2surface = numberfont.render(str(p2score), False, white)

    # Draws line in middle of screen
    pygame.draw.rect(window, white, [(screenWidth/2)-5, 0, width, screenHeight])
    
    # Draws surfaces for player scores
    window.blit(p1surface,((screenWidth/4)+2.5,30))
    window.blit(p2surface,(((screenWidth/4)*3)+2.5,30))


def gameloop():

    dead = False
    fps = 60

    p1score = 0
    p2score = 0

    while not dead:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draws Lines and score on board
        drawboard(p1score,p2score)

        # Updates screen, with a 60FPS rate
        pygame.display.update()
        clock.tick(fps)
        
# Calls Game Loop
gameloop()
# Quits pygame and python
pygame.quit()
quit()