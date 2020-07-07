import pygame


class Rectangles:
    def __init__(self, pos_x, pos_y, width, height, color):
        """Creates the rectangles that have x,y,width,height,color"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
    
    def Draw(self, screen):
        """Draw function for drawing the rectangles"""
        pygame.draw.rect(screen, self.color,(self.pos_x, self.pos_y, self.width, self.height))

    def mouse_pressed(self, radius = 0):
        """This functions takes the position of the mouse and the fact that is pressed or not"""
        if (pygame.mouse.get_pos()[0] - radius >= self.pos_x and pygame.mouse.get_pos()[1] - radius >= self.pos_y) and (pygame.mouse.get_pos()[0] + radius <= self.pos_x + self.width and pygame.mouse.get_pos()[1] + radius <= self.pos_y + self.height):
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
    
def mouse_rect(dimension, screen, color):
    pygame.draw.rect(screen, color, (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 10, dimension, dimension ), 3)

def get_dimension(dimension):
    key = pygame.key.get_pressed()

    if key[pygame.K_n]:
        dimension += 10
        return dimension
    elif key[pygame.K_m]:
        dimension -= 10
        return dimension
    else:
        return dimension
def mouse_pos(Rectangles, dimension):
    if (pygame.mouse.get_pos()[0] - dimension >= Rectangles.pos_x and pygame.mouse.get_pos()[1] - dimension >= Rectangles.pos_y) and (pygame.mouse.get_pos()[0] + dimension <= Rectangles.pos_x + Rectangles.width and pygame.mouse.get_pos()[1] + dimension <= Rectangles.pos_y + Rectangles.height):
        if pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False    
