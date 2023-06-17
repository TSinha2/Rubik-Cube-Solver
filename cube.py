import numpy as np
from copy import deepcopy

class Cube:
    def __init__(self, cubeState=None):
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

        If the user inputs the state of their own cube to be solved:
        It should be in 'www...>' format (i.e. a string of length 54)

        The first 9 colors represent the white face (with blue side facing upwards)
        in the following format
        1 2 3
        4 5 6
        7 8 9

        The next 9 represent the yellow face (with blue facing downwards) -- using the same format mentioned earlier

        Following are the blue face, green face, red face, orange face -- all in the aforementioned format. Note that for each of 
        these faces, yellow is on the top, and white is on the bottom

        """        
        if cubeState == None:
            white_face = np.array([['w' for i in range(3)] for i in range(3)])
            yellow_face = np.array([['y' for i in range(3)] for i in range(3)])
            blue_face = np.array([['b' for i in range(3)] for i in range(3)])
            green_face = np.array([['g' for i in range(3)] for i in range(3)])
            red_face = np.array([['r' for i in range(3)] for i in range(3)])
            orange_face = np.array([['o' for i in range(3)] for i in range(3)])
        else:
            assert(len(cubeState) == 54)
            white_face = self.convert_face(cubeState[0:9])
            yellow_face = self.convert_face(cubeState[9:18])
            blue_face = self.convert_face(cubeState[18:27])
            green_face = np.fliplr(self.convert_face(cubeState[27:36]))
            red_face = np.fliplr(self.convert_face(cubeState[36:45]))
            orange_face = self.convert_face(cubeState[45:54])



        cube = []
        cube.extend((white_face, yellow_face, blue_face, green_face, red_face, orange_face))
        self.cube = np.stack(cube, 0)
        self.top = 1
        self.bot = 0
        self.right = 5
        self.left = 4
        self.face = 2
        self.back = 3
        self.orientation_ranges = {'r': 1, 'g': 2, 'o': 3}


        #

    def convert_face(self, state):
        """
        Given the string version of a face, turn it into a suitable numpy array
        """
        assert len(state) == 9
        assert type(state) == str
        row1 = [i for i in state[0:3]]
        row2 = [i for i in state[3:6]]
        row3 = [i for i in state[6:9]]
        face = np.array((row1, row2, row3))
        return face


        pass
    def turn_horizontal(self, row: int) -> None:
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

    def turn_vertical(self, col: int) -> None:
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
    
    def turn_sideways(self, side_col: int) -> None:
        """
        Function for sideways turns (F, B' in Rubik's Cube Notation)
        
        Parameters: 
            side_col (int): which side_col number to turn (2 is F, 0 is B')

        Return: None
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


        
    def display_cube(self) -> None:
        """
        Display the cube  as text in the shell
        """

        for i in range(6):
            if (i == 4 or i == 3):
                print(np.fliplr(self.cube[i]))
                print("")                
            else:
                print(self.cube[i])
                print("")
            # print(self.cube[i])
            # print("")
    
    def algorithm_parser(self, algorithm: str) -> None:
        """
        Allows for user to use normal cube notation to modify the cube

        Parameters:
            algorithm (str): The algorithm to be executed on the cube
        
        Return: None
        """
        algorithm = algorithm.split()
        moves = "R Ri Li L F Fi B Bi U Ui D Di R' L' F' B' U' D' U2 D2 F2 B2 R2 L2 Y".split()
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
            
            elif (move == 'Y'):
                self.turn_horizontal(0)
                self.turn_horizontal(1)
                self.turn_horizontal(2)
            
            elif (move == 'Yi' or move == 'Y'):
                for i in range(3):
                    self.turn_horizontal(0)
                    self.turn_horizontal(1)
                    self.turn_horizontal(2)

            else:
                pass

    def save_state(self, given_state=''):
        """
        Saves the state (i.e. each face) of the cube
        
        Return: None
        """
        if len(given_state) != 6:
            self.save = deepcopy(self.cube)
        else:
            self.save = deepcopy(given_state)

        return self.save            

        
    def restore_state(self, given_state='') -> None:
        """
        Restores the previously saved state

        Return: None
        """
        if len(given_state) != 6:
            self.cube = deepcopy(self.save)
        else:
            self.cube = deepcopy(given_state)
    
    def change_orientation(self, front: str) -> None:
        """
        Modifies the side that is facing the users (and consequently other sides as well). Note that it only supports orientation in the horizontal direction.

        Parameters: 
            front (str): The color that should be at the front, facing the user
        
        Return: None
        """
        assert front in ['r', 'g', 'o', 'b']
        counter = 0
        moves = ''
        while self.get_cube()[2][1][1] != front:
            counter += 1
            self.algorithm_parser("Y")
        
        return moves.join(' Y' for i in range(counter))
        
    def default_orientation(self) -> None:
        """
        Restores  the initial orientation (i.e. Blue facing the user)
        """
        return(self.change_orientation('b'))
    
    def get_cube(self):
        return self.cube
    
    def str_cube_state(self):
        state = ''
        for face_index in range(6):
            for row in self.cube[face_index]:
                if face_index == 3 or face_index == 4:
                    for color in row[::-1]:
                        state += color
                else:
                    for color in row:
                        state += color
        
        return state




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