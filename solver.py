
import numpy as np

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
    
    def turn_horizontal(self, row):
        """
        Function for the horizontal turns (U, D' in Rubik's Cube notation)

        Parameters: 
            row (int): which row number to turn: 0 is the U layer, 2 is the D layer
        Return:
            None
        """
        temp = [i for i in self.cube[2][row]]

        self.cube[2][row] = self.cube[4][row][::-1]
        self.cube[4][row] = self.cube[3][row]
        self.cube[3][row] = self.cube[5][row][::-1]
        self.cube[5][row] = temp

        # self.cube[4] = np.fliplr(self.cube[4])
        # self.cube[4] = np.flipud(self.cube[4])



        if (row == 0):
            self.cube[1] = np.rot90(self.cube[1], -1)
        
        elif (row == 2):
            self.cube[0] = np.rot90(self.cube[0], 1)
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
        temp = [i for i in self.cube[0][:, col]]

        self.cube[0][:, col] = self.cube[3][:, col][::-1]
        self.cube[3][:, col] = self.cube[1][:, col][::-1]
        self.cube[1][:, col] = self.cube[2][:, col]
        self.cube[2][:, col] = temp

        # self.cube[4] = np.fliplr(self.cube[4])
        # self.cube[4] = np.flipud(self.cube[4])


        if (col == 0):
            self.cube[5] = np.rot90(self.cube[5], 1)
        
        elif (col == 2):
            self.cube[4] = np.rot90(self.cube[4], 1)
        else:
            return
    
    def turn_sideways(self, side_col):
        """
        Function for sideways turns (F, B' in Rubik's Cube Notation)
        
        Parameters: 
            side_col (int): which side_col number to turn (0 is F, 2 is B')
        """
        temp = [i for i in self.cube[1][:, 2-side_col]]
        self.cube[1][2-side_col] = self.cube[5][2-side_col]
        self.cube[5][:,2-side_col] = self.cube[0][:,2-side_col]
        self.cube[0][2-side_col] = self.cube[4][2-side_col]
        self.cube[4][:, 2-side_col] = temp


        
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