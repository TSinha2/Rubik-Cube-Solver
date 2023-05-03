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


        white = ['W' for i in range(SIDE_SIZE)] #0
        yellow = ['Y' for i in range(SIDE_SIZE)] #1
        orange = ['O' for i in range(SIDE_SIZE)] #2
        red = ['R' for i in range(SIDE_SIZE)] #3
        blue = ['B' for i in range(SIDE_SIZE)] #4
        green = ['G' for i in range(SIDE_SIZE)] #5


        cube.extend((white, yellow, orange, red, blue, green))
        self.cube = cube
    
    def __get_opposite_side(self, side):
        if (side % 2 == 0):
            return (side+1)
        else:
            return (side-1)
    

    def orient(self, front, right, top):
        self.front = front 
        self.right = right
        self.top = top
        self.bottom = self.__get_opposite_side(top)
        self.left = self.__get_opposite_side(right)
        self.back = self.__get_opposite_side(front)


    # Right and left faces will not be affected
    def turn_right(self):
        print("Bottom: ", self.bottom)
        print("Front: ", self.front)
        temp = [i for i in self.cube[self.back]]
        for i in self.col3:
            self.cube[self.back][i] = self.cube[self.top][i]
            self.cube[self.top][i] = self.cube[self.front][i]
            self.cube[self.front][i] = self.cube[self.bottom][i]
            self.cube[self.bottom][i] = temp[i]

        

    def get_cube(self):
        return self.cube
    
    def __display_side(self, side):
        for i in range(9):
            print(side[i],end="")
            if (i-1 in self.col2):
                print("")
    
    def display_cube(self):
        for side in self.cube:
            self.__display_side(side)
            print("")
        





test = Cube()
test.display_cube()
test.orient(4, 2, 0)
test.turn_right()
print("----------")
test.display_cube()

    

        
    
