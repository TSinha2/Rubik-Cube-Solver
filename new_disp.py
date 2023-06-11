from nicegui import ui

def button_click(row, col, grid_id):
    ui.notify(f'Button clicked: Grid {grid_id}, Row {row}, Column {col}')

# Set the background color to black using CSS style
ui.html('<style>body { background-color: black; }</style>')

# Center the white and yellow grids
with ui.row():
    ui.html('<div style="flex: 1; display: flex; justify-content: center; margin-left:160px">')
    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 1'), color='yellow')
    ui.html('</div>')
ui.html("<br>")

# Remaining grids
with ui.row():
    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 2'), color='blue')

    for _ in range(2):
        ui.html('<div style="height: 20px;"></div>')

    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 3'), color='red')

    for _ in range(2):
        ui.html('<div style="height: 20px;"></div>')

    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 3'), color='green')

    for _ in range(2):
        ui.html('<div style="height: 20px;"></div>')

    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 3'), color='orange')

ui.html("<br>")

with ui.row():
    ui.html('<div style="flex: 1; display: flex; justify-content: center; margin-left:160px">')
    with ui.grid(columns=3):
        for row in range(3):
            for col in range(3):
                ui.button('', on_click=lambda r=row, c=col: button_click(r, c, 'Grid 1'), color='white')
    ui.html('</div>')

ui.run()
