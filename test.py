import pygame
import paint_functions as pf
pygame.init()

width, height = (960, 960)
screen = pygame.display.set_mode((width, height))
#Important variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
dimension = 30
#Create the list that will contain the rectangles
rectangles = [[]]
#Create a flag
active = True
#Create the painting space
for y in range(0, 60):
    rectangles.append([])
    nested_list = rectangles[y]
    for x in range(0, 60):
        
        nested_list.append(pf.Rectangles(x * 17, y * 17 , 16, 16, BLACK))

#Create the clock that will measure the fps
clock = pygame.time.Clock()
############
while active:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    screen.fill(WHITE)
    #Draw the rectangles
    for i in range(0, 60):
        for j in range(0, 60):
            if rectangles[i][j].mouse_pressed() and dimension == 10:
                rectangles[i][j].color = RED
            elif rectangles[i][j].mouse_pressed() and dimension == 30:
                rectangles[i - 1][j].color = RED
                rectangles[i + 1][j].color = RED
                rectangles[i][j - 1].color = RED
                rectangles[i][j + 1].color = RED
            else:
                pass 
            rectangles[i][j].Draw(screen)
    #Check for the circle around the cursor
    pf.mouse_rect(dimension, screen, RED)
    dimension = pf.get_dimension(dimension)
    pygame.display.flip()