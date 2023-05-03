from tkinter.tix import ROW


class Cube:
    def __init__(self):
        DIM = 3
        SIDE_SIZE = 9
        ROW_SIZE = 3
        COL_SIZE = ROW_SIZE
        cube = []


        self.row1 = [i for i in range(ROW_SIZE)]
        self.row2 = [i+(DIM) for i in range(ROW_SIZE)]
        self.row3 = [i+(2*DIM) for i in range(ROW_SIZE)]

        self.col1 = [(DIM*i) for i in range(COL_SIZE)]
        self.col2 = [1+(DIM*i) for i in range(COL_SIZE)]
        self.col3 = [2+(DIM*i) for i in range(COL_SIZE)]


        white = ['W' for i in range(SIDE_SIZE)] 
        yellow = ['Y' for i in range(SIDE_SIZE)] 
        orange = ['O' for i in range(SIDE_SIZE)]
        red = ['R' for i in range(SIDE_SIZE)]
        blue = ['B' for i in range(SIDE_SIZE)]
        green = ['G' for i in range(SIDE_SIZE)]


        cube.extend((white, yellow, orange, red, blue, green))
        self.cube = cube

    # def orient(self, front, right, top):
    #     self.front = front
    #     self.back = (front+1)
    #     self.y = right
    #     self.z = top





test = Cube()
for i in test.get_cube():
    for j in i:
        print(j)

    

        
    
