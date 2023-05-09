import pygame
from cube import Cube
from test import fix_orientation

dimension = 30
sticker_gap = 2
face_gap = 100
colors = {'y': (255, 255, 0),
          'o': (242, 140, 40),
          'b': (0,0,255),
          'r': (255,0,0),
          'g': (0,255,0),
          'w':(255,255,255)
            }




def draw_row(surface, left, top, row):
    for i in range(3):
        pygame.Surface.fill(surface, colors[row[i]], [left + (dimension + sticker_gap)*i , top , dimension, dimension]) 

def draw_face(surface, left, top,face):
    for i in range(3):
        draw_row(surface, left, top + (dimension + sticker_gap)*i, face[i]) 

def draw_cube(surface, left, top, cube):
    draw_face(surface, left + face_gap, top, cube[1])
    order_to_present = [5, 2, 4, 3]
    for i in range(2, 6):
        draw_face(surface, left + face_gap*(i-2), top + face_gap, cube[order_to_present[i-2]])

    draw_face(surface, left + face_gap, top + 2*face_gap, cube[0])


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER the game
    # draw_cube(screen, 18, 18)
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    test_cube.turn_horizontal(0)
    

    draw_cube(screen, 18, 18, fix_orientation(test_cube.get_cube()))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
