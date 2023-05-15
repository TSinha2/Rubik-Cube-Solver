import numpy as np
from copy import deepcopy

class Cube:
    def __init__(self):
        """
        Instantiate the Rubik's cube as a 6x3x3 using Numpy arrays
            Cube[0] -> White
            Cube[1] -> Yellow
            Cube[2] -> Blue
            Cube[3] -> Green
            Cube[4] -> Red
            Cube[5] -> Orange
 
        Assuming the cube is in oriented in the following manner:
            Blue facing the user, Green behind
            Orange on the left, Red on the right
            Yellow on the top, White on the bottom
        """        
        white_face = np.array([['w' for i in range(3)] for i in range(3)])
        yellow_face = np.array([['y' for i in range(3)] for i in range(3)])
        blue_face = np.array([['b' for i in range(3)] for i in range(3)])
        green_face = np.array([['g' for i in range(3)] for i in range(3)])
        red_face = np.array([['r' for i in range(3)] for i in range(3)])
        orange_face = np.array([['o' for i in range(3)] for i in range(3)])
        cube = []
        cube.extend((white_face, yellow_face, blue_face, green_face, red_face, orange_face))
        self.cube = np.stack(cube, 0)
        self.top = 1
        self.bot = 0
        self.right = 5
        self.left = 4
        self.face = 2
        self.back = 3


        #

    def turn_horizontal(self, row):
        """
        Function for the horizontal turns (U, D' in Rubik's Cube notation)

        Parameters: 
            row (int): which row number to turn: 0 is the U layer, 2 is the D layer
        Return:
            None
        """
        temp = [i for i in self.cube[self.face][row]]

        self.cube[self.face][row] = self.cube[self.left][row][::-1]
        self.cube[self.left][row] = self.cube[self.back][row]
        self.cube[self.back][row] = self.cube[self.right][row][::-1]
        self.cube[self.right][row] = temp

        # self.cube[4] = np.fliplr(self.cube[4])
        # self.cube[4] = np.flipud(self.cube[4])



        if (row == 0):
            self.cube[self.top] = np.rot90(self.cube[self.top], -1)
        
        elif (row == 2):
            self.cube[self.bot] = np.rot90(self.cube[self.bot], 1)
        else:
            return

    def turn_vertical(self, col):
        """
        Function for the vertical turns (R, L' in Rubik's cube notation)

        Parameters: 
            col (int): which col number to turn: 0 is the L layer, 2 is the R layer
        
        Return: 
            None
        """
        temp = [i for i in self.cube[self.bot][:, col]]

        self.cube[self.bot][:, col] = self.cube[self.back][:, col][::-1]
        self.cube[self.back][:, col] = self.cube[self.top][:, col][::-1]
        self.cube[self.top][:, col] = self.cube[self.face][:, col]
        self.cube[self.face][:, col] = temp

        # self.cube[4] = np.fliplr(self.cube[4])
        # self.cube[4] = np.flipud(self.cube[4])


        if (col == 0):
            self.cube[self.right] = np.rot90(self.cube[self.right], 1)
        
        elif (col == 2):
            self.cube[self.left] = np.rot90(self.cube[self.left], 1)
        else:
            return
    
    def turn_sideways(self, side_col):
        """
        Function for sideways turns (F, B' in Rubik's Cube Notation)
        
        Parameters: 
            side_col (int): which side_col number to turn (2 is F, 0 is B')
        """
        temp = [i for i in self.cube[self.top][side_col]]
        self.cube[self.top][side_col] = self.cube[self.right][:,side_col][::-1]
        self.cube[self.right][:,side_col] = self.cube[self.bot][2-side_col]
        self.cube[self.bot][2-side_col] = self.cube[self.left][:,side_col][::-1]
        self.cube[self.left][:, side_col] = temp

        if (side_col == 0):
            self.cube[self.back] = np.rot90(self.cube[self.back], -1)
        
        elif (side_col == 2):
            self.cube[self.face] = np.rot90(self.cube[self.face], -1)
        else:
            return


        
    def display_cube(self):
        for i in range(6):
            if (i == 4 or i == 3):
                print(np.fliplr(self.cube[i]))
                print("")                
            else:
                print(self.cube[i])
                print("")
            # print(self.cube[i])
            # print("")
    
    def algorithm_parser(self, algorithm):
        algorithm = algorithm.split()
        moves = "R Ri Li L F Fi B Bi U Ui D Di R' L' F' B' U' D' U2 D2 F2 B2 R2 L2".split()
        for move in algorithm:
            assert (move in moves)
            if (move == 'R'):
                self.turn_vertical(2)

            elif (move == 'Ri' or move == "R'"):
                for i in range(3):
                    self.turn_vertical(2)

            elif (move == 'R2'):
                for i in range(2):
                    self.turn_vertical(2)
            
            elif (move == 'Li' or move == "L'"):
                self.turn_vertical(0)
            
            elif (move == 'L'):
                for i in range(3):
                    self.turn_vertical(0)

            elif (move == 'L2'):
                for i in range(2):
                    self.turn_vertical(0)

            elif (move == 'U'):
                self.turn_horizontal(0)
            
            elif (move == 'Ui' or move == "U'"):
                for i in range(3):
                    self.turn_horizontal(0)

            elif (move == 'U2' ):
                for i in range(2):
                    self.turn_horizontal(0)

            
            elif (move == 'Di' or move == "D'") :
                self.turn_horizontal(2)
            
            elif (move == 'D'):
                for i in range(3):
                    self.turn_horizontal(2)

            elif (move == 'D2'):
                for i in range(2):
                    self.turn_horizontal(2)
            
            elif (move == 'F'):
                self.turn_sideways(2)
            
            elif (move == 'Fi' or move == "F'"):
                for i in range(3):
                    self.turn_sideways(2)

            elif (move == 'F2'):
                for i in range(2):
                    self.turn_sideways(2)                    
            
            elif (move == 'B'):
                for i in range(3):
                    self.turn_sideways(0)

            elif (move == 'Bi' or move == "B'"):
                self.turn_sideways(0)

            elif (move == 'B2'):
                for i in range(2):
                    self.turn_sideways(0)

            else:
                pass

    def save_state(self):
            self.save = deepcopy(self.cube)
        
    def restore_state(self):
            self.cube = deepcopy(self.save)
    
    def change_orientation(self, front, left, right):
        # Assuming bot/top are fixed
        a = [self.face, self.back, self.right, self.left]
        for i in a:
            print("Initial: " + str(i))
        assert front in [2,3,4,5] 
        self.face = front
        self.back = front+1 if (front == 2 or front == 4) else front-1
        self.right = right
        self.left = left
        for i in a:
            print("New: " + str(i))


    
    def get_cube(self):
        return self.cube



"""
Test cases planned so far:
i) R
ii) U
iii) R U 
iv) U R 
v) R U R 
vi) U R U 
vii) U' R' U'

Way to check test case output: 
--> Look at the self.cube 
"""