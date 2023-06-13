from cgi import test
from nicegui import ui
from cube import Cube
from numpy import fliplr

# ui.add_head_html('<style>body {background-color: #c9c5c5; }</style>')

def create_side_buttons(side, grid_id, color):
    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                button_color = side[row][col]
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, grid_id), color=button_color)

def button_click(row, col, grid_id):
    ui.notify(f'Button clicked: Grid {grid_id}, Row {row}, Column {col}')

def create_rubiks_cube(sides):
    # Set the background color to black using CSS style
    #ui.html('<style>body { background-color: black; }</style>')

    # Center the white and yellow grids
    with ui.row():
        ui.html('<div style="flex: 1; display: flex; justify-content: center; margin-left:180px">')
        create_side_buttons(sides[1], 'Grid 1', 'yellow')
        ui.html('</div>')
    ui.html("<br>")

    # Create a single row for blue, green, red, and orange grids
    with ui.row():
        ui.html('<div style="flex: 1; display: flex; justify-content: center; margin-left:0px">')
        create_side_buttons(sides[5], 'Grid 2', 'blue')
        ui.html('<div style="width: 20px;"></div>')
        create_side_buttons(sides[2], 'Grid 4', 'green')
        ui.html('<div style="width: 20px;"></div>')
        create_side_buttons(fliplr(sides[4]), 'Grid 3', 'red')
        ui.html('<div style="width: 20px;"></div>')
        create_side_buttons(fliplr(sides[3]), 'Grid 5', 'orange')
        ui.html('</div>')

    ui.html("<br>")

    with ui.row():
        ui.html('<div style="flex: 1; display: flex; justify-content: center; margin-left:180px">')
        create_side_buttons(sides[0], 'Grid 6', 'white')
        ui.html('</div>')

    ui.run()


sides = [
    [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']],  # Side 1
    [['blue', 'blue', 'blue'], ['blue', 'blue', 'blue'], ['blue', 'blue', 'blue']],  # Side 2
    [['red', 'red', 'red'], ['red', 'red', 'red'], ['red', 'red', 'red']],  # Side 3
    [['green', 'green', 'green'], ['green', 'green', 'green'], ['green', 'green', 'green']],  # Side 4
    [['orange', 'orange', 'orange'], ['orange', 'orange', 'orange'], ['orange', 'orange', 'orange']],  # Side 5
    [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']]  # Side 6
]
test_cube = Cube()
# test_cube.algorithm_parser("R")
test_cube.algorithm_parser("D' L2 F' R2 B2 L U2 D' L' R' U2 D L' F' B' R F2 D B D' R U2 R2 U L2")
sides = []
letter2Color = {'g': 'green', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white', 'y': 'yellow'}
def CubeFace2NiceGUIside(CubeFace):
    side = []
    for row in CubeFace:
        side.append(list(map(lambda i: letter2Color[i], row)))
    
    return side

sides = [CubeFace2NiceGUIside(i) for i in test_cube.get_cube()]      


# ui.colors(primary="#ffffff")
#ui.input('Algorithm', placeholder='Enter your algorithm here').style('color: white; background-color: #333; border: 1px solid #777; padding: 8px; font-family: monospace; font-size: 14px;')
ui.input("Algorithm", placeholder='Enter your algorithm here')

# a = {'g': 'green', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white', 'y': 'yellow'}
# for side in test_cube.get_cube():
#     for row in side:
#         s = list(map(lambda i: a[i], row))
#         s.append



create_rubiks_cube(sides)
