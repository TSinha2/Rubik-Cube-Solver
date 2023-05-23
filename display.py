from cgi import test
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
test_cube.algorithm_parser("D' B F U F2 D' B R U L' U L F L F' U' D' R' B' R' B D2 L' R U")
test_cube.algorithm_parser("Li Fi R Y Y Y Y Y Y F U R Li Y Y  U F2 U B2 U U U U R2 U L2")
test_cube.algorithm_parser("Y Y U U U U' L' U L R U' R' U R U' R' Y R U' R' Y U U' L' U L Y Y Y U U U U' L' U L Y U U U R U' R'")
test_cube.algorithm_parser("Y U R U' R' U' F' U F Y Y Y U U' L' U L U F U' F' Y U' L' U L U F U' F' Y U R U' R' U' F' U F Y U' L' U L U F U' F' U U U U' L' U L U F U' F' Y Y U' L' U L U F U' F' U U U U' L' U L U F U' F' Y Y Y")

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
    
    if keys[pygame.K_z]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.change_orientation('g')

    if keys[pygame.K_x]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.change_orientation('r')

    if keys[pygame.K_c]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.change_orientation('o')

    if keys[pygame.K_a]:
        if move_ticker == 0:
            move_ticker = frame_value
            print(a.second_layer_not_complete())


    if keys[pygame.K_q]:
        if move_ticker == 0:
            move_ticker = frame_value
            test_cube.default_orientation()


    if keys[pygame.K_w]:
        if move_ticker == 0:
            move_ticker = frame_value
            a.white()

    if keys[pygame.K_s]:
        if move_ticker == 0:
            move_ticker = frame_value
            a.second_layer()


    if keys[pygame.K_p]:
        if move_ticker == 0:
            move_ticker = frame_value
            a.orient_yellow_edges()




    draw_cube(screen, 18, 18, test_cube.get_cube())

    # flip() the display to put your work on screen
    pygame.display.flip()
    if move_ticker > 0:
        move_ticker -= 1

    clock.tick(30)  # limits FPS to 60

pygame.quit()
