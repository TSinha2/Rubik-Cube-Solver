from tkinter import Frame
import pygame
from cube import Cube
import numpy as np
from solver import Solver

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

test_cube = Cube()
# test_cube.algorithm_parser("B' R U' D R U' D D  B' U U R' F R' L F' D' B' U F F L' B D' F' U' R R B'")
test_cube.change_orientation(4,2,3)
test_cube.algorithm_parser("R")
test_cube.change_orientation(2,5,4)
# test_cube.algorithm_parser("R")

a = Solver(test_cube)

frame_value = 5
move_ticker = frame_value


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
        if (order_to_present[i-2] == 4 or order_to_present[i-2] == 3):
            draw_face(surface, left + face_gap*(i-2), top + face_gap, np.fliplr(cube[order_to_present[i-2]]))
        else:
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


    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("R")
    
    if keys[pygame.K_l]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("L")

    if keys[pygame.K_u]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("U")

    if keys[pygame.K_d]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("D")

    if keys[pygame.K_b]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("B")

    if keys[pygame.K_f]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.algorithm_parser("F")
    if keys[pygame.K_g]:
        if move_ticker == 0:
            move_ticker = frame_value
            a.cross()


    draw_cube(screen, 18, 18, test_cube.get_cube())

    # flip() the display to put your work on screen
    pygame.display.flip()
    if move_ticker > 0:
        move_ticker -= 1

    clock.tick(30)  # limits FPS to 60

pygame.quit()
