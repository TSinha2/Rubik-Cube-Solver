import pygame

dimension = 30
sticker_gap = 2
face_gap = 100


def draw_row(surface, color, left, top):
    for i in range(3):
        pygame.Surface.fill(surface, color, [left + (dimension + sticker_gap)*i , top , dimension, dimension]) 

def draw_face(surface, color, left, top):
    for i in range(3):
        draw_row(surface, color, left, top+ (dimension + sticker_gap)*i) 

def draw_cube(surface, left, top):
    colors = [(255, 255, 0), (242, 140, 40), (0,0,255), (255,0,0), (0,255,0), (255,255,255)]
    draw_face(surface, colors[0], left + face_gap, top)
    for i in range(4):
        draw_face(surface, colors[i+1], left + face_gap*i, top + face_gap)

    draw_face(surface, colors[5], left + face_gap, top + 2*face_gap)


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
    draw_cube(screen, 18, 18)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
