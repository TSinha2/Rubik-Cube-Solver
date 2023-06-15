import customtkinter as ctk
from cube import Cube
from numpy import fliplr
from solver import Solver

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")

# Create a 2D net representing the colors of a Rubik's Cube
cube = [
    [["yellow", "yellow", "yellow"],
     ["yellow", "yellow", "yellow"],
     ["yellow", "yellow", "yellow"]],

    [["green", "green", "green"],
     ["green", "green", "green"],
     ["green", "green", "green"]],

    [["orange", "orange", "orange"],
     ["orange", "orange", "orange"],
     ["orange", "orange", "orange"]],

    [["blue", "blue", "blue"],
     ["blue", "blue", "blue"],
     ["blue", "blue", "blue"]],

    [["red", "red", "red"],
     ["red", "red", "red"],
     ["red", "red", "red"]],

    [["white", "white", "white"],
     ["white", "white", "white"],
     ["white", "white", "white"]],
]

test_cube = Cube()

sides = []
letter2Color = {'g': 'green', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white', 'y': 'yellow'}

def CubeFace2NiceGUIside(CubeFace):
    side = []
    for row in CubeFace:
        side.append(list(map(lambda i: letter2Color[i], row)))

    return side

cube = []
order = [1, 5, 2, 4, 3, 0]
for i in order:
    if not (i == 3 or i == 4):
        cube.append(CubeFace2NiceGUIside(test_cube.get_cube()[i]))
    else:
        cube.append(CubeFace2NiceGUIside(fliplr(test_cube.get_cube()[i])))

# Constants for layout management
TOP_FACE_ROW = 3
BOTTOM_FACE_ROW = 6
SQUARE_SIZE = 50
PADX = 5
PADY = 5

def handle_button_click(face, row, column):
    print(f"Button pressed: Face {face}, Row {row}, Column {column}")

def create_button(face, row, column):
    color = cube[face][row][column]
    return ctk.CTkButton(
        text='', master=app, width=SQUARE_SIZE, height=SQUARE_SIZE,
        command=lambda f=face, r=row, c=column: handle_button_click(f, r, c),
        fg_color=color
    )

def create_cube_ui():
    buttons = []

    for face in range(6):
        face_buttons = []

        for i in range(3):
            row_buttons = []

            for j in range(3):
                if face == 0:  # Yellow face (top)
                    square = create_button(face, i, j)
                    square.grid(row=i, column=j + 3, padx=PADX, pady=PADY)
                elif face == 5:  # White face (bottom)
                    square = create_button(face, i, j)
                    square.grid(row=i + BOTTOM_FACE_ROW, column=j + 3, padx=PADX, pady=PADY)
                else:  # Other faces (horizontal line)
                    square = create_button(face, i, j)
                    square.grid(row=i + TOP_FACE_ROW, column=(face - 1) * 3 + j, padx=PADX, pady=PADY)

                row_buttons.append(square)

            face_buttons.append(row_buttons)

        buttons.append(face_buttons)

    return buttons

def handle_parse_algorithm():
    algorithm = input_field.get()
    test_cube.algorithm_parser(algorithm)
    update_cube_state()
    update_cube_ui()

def handle_solve():
    solver = Solver(test_cube)
    solution = solver.human_readable_solver()  # Assuming the solve() function returns the solution
    solution_text.configure(state='normal')
    solution_text.delete('1.0', 'end')
    solution_text.insert('end', solution)
    solution_text.configure(state='disabled')
    update_cube_state()
    update_cube_ui()


def update_cube_state():
    global cube
    cube = []
    order = [1, 5, 2, 4, 3, 0]
    for i in order:
        if not (i == 3 or i == 4):
            cube.append(CubeFace2NiceGUIside(test_cube.get_cube()[i]))
        else:
            cube.append(CubeFace2NiceGUIside(fliplr(test_cube.get_cube()[i])))

def update_cube_ui():
    for face in range(6):
        for i in range(3):
            for j in range(3):
                button = cube_buttons[face][i][j]
                color = cube[face][i][j]
                button.configure(fg_color=color)

cube_buttons = create_cube_ui()

# Create text input field for algorithm
input_field = ctk.CTkEntry(app, width=500)
input_field.grid(row=14, column=1, columnspan=8, padx=PADX, pady=PADY)

# Create button to parse algorithm
parse_button = ctk.CTkButton(
    text="Parse Algorithm", master=app,
    command=handle_parse_algorithm
)
parse_button.grid(row=15, column=1, columnspan=6, padx=PADX, pady=PADY)

# Create button to solve the cube
solve_button = ctk.CTkButton(
    text="Solve", master=app,
    command=handle_solve
)
solve_button.grid(row=16, column=1, columnspan=6, padx=PADX, pady=PADY)

# Create text widget to display solution
solution_text = ctk.CTkTextbox(app, width=500, height=100, state='disabled')
solution_text.grid(row=17, column=1, columnspan=8, padx=PADX, pady=PADY)

app.mainloop()
