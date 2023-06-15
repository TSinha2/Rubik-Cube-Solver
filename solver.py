from cgi import test
from itertools import count, permutations
from turtle import right
from cube import Cube
import numpy as np

from test import test_twelve

edges = [(0, 1), (1, 0), (1, 2), (2, 1)]


class Solver:
    def __init__(self, unsolved_cube) -> None:
        self.unsolved_cube = unsolved_cube
        self.solved =             correct_array = np.array(
                [[['w' ,'w', 'w'],
                ['w', 'w' ,'w'],
                ['w', 'w' , 'w']],

                [['y', 'y' ,'y'],
                ['y', 'y', 'y'],
                ['y', 'y' ,'y']],

                [['b', 'b' ,'b'],
                ['b', 'b' ,'b'],
                ['b', 'b', 'b']],

                [['g' ,'g' ,'g'],
                ['g', 'g' ,'g'],
                ['g' ,'g' ,'g']],

                [['r', 'r' ,'r'],
                ['r', 'r' ,'r'],
                ['r', 'r' ,'r']],

                [['o','o','o'],
                ['o', 'o' ,'o'],
                ['o' ,'o' ,'o']]]
                )
        self.cross_solved   = False
        self.white_solved    = False
        if not type(unsolved_cube) == Cube:
            raise ValueError("Please pass a cube object")

        
    def find_white_edges(self):
        """
        Return array of white edges in following format: 
        [  (face_index, row, row_index)   ]
        """
        faces = self.unsolved_cube.get_cube()
        white_edges = []
        for face_index in range(6):
            face = faces[face_index]
            for row, edge in edges:
                if face[row][edge] == 'w':
                    white_edges.append((face_index, row, edge))
        
        return white_edges

    def white_edge_count(self):
        """
        Returns the number of white edges on yellow faces
        """
        count = 0
        faces = self.unsolved_cube.get_cube()
        yellow_face = faces[1]
        for row, edge in edges:
            if yellow_face[row][edge] == 'w':
                count += 1
        
        return count
    
    def white_to_yellow_helper(self, move):
        moves = ""
        counter = 0
        initial_edge_count = self.white_edge_count()
        # while True:
        #     print(self.unsolved_cube.get_cube())
        #     self.unsolved_cube.algorithm_parser(move)
        #     if (self.white_edge_count() >= initial_edge_count):
        #         break
        #     else:
        #         if len(move) == 2 and move[1] != '2':
        #             self.unsolved_cube.algorithm_parser(move[0])
        #         if len(move) == 2 and move[1] == '2':
        #             self.unsolved_cube.algorithm_parser(move)
        #         else:
        #             self.unsolved_cube.algorithm_parser(move[0] + "i")
        
        #     self.unsolved_cube.algorithm_parser("U")
        #     moves += " U"

        self.unsolved_cube.save_state()       
        for i in range(4):
            self.unsolved_cube.algorithm_parser(move)       
            if (self.white_edge_count() > initial_edge_count):
                moves+= " " + move
                return moves
            else:
                self.unsolved_cube.restore_state()       
                # if len(move) == 2 and move[1] != '2':
                #     self.unsolved_cube.algorithm_parser(move[0])
                # print("Iteration: ", i)
                # print("YELLOW face:\n ", self.unsolved_cube.get_cube()[1])
                # print("BLUE face:\n ", self.unsolved_cube.get_cube()[2])
                # if len(move) == 2 and move[1] == '2':
                #     self.unsolved_cube.algorithm_parser(move)
                # else:
                #     self.unsolved_cube.algorithm_parser(move[0] + "i")
                self.unsolved_cube.algorithm_parser("U")
                moves += " U"
                self.unsolved_cube.save_state()       


    

    
    def white_to_yellow(self):
        moves = ""
        white_face = self.unsolved_cube.get_cube()[0]
        for edge in edges:
            if white_face[edge[0]][edge[1]] == 'w':
                match edge:
                    case (0,1):
                        moves += self.white_to_yellow_helper("F2")
                    case (1,0):
                        moves += self.white_to_yellow_helper("L2")
                    case (1,2):
                        moves += self.white_to_yellow_helper("R2")
                    case (2,1):
                        moves += self.white_to_yellow_helper("B2")
        
        for face in 'b r o g'.split():
            moves += self.unsolved_cube.change_orientation(face)
            front_face = self.unsolved_cube.get_cube()[2]
            for edge in edges:
                if front_face[edge[0]][edge[1]] == 'w':
                    match edge:
                        case (1,0):
                            moves += self.white_to_yellow_helper("Li")
                        case (1, 2):
                            moves += self.white_to_yellow_helper("R")
                        case (0, 1):
                            flag = False
                            initial_edge_count = self.white_edge_count()
                            self.unsolved_cube.algorithm_parser("F")
                            moves += " F"
                            if (initial_edge_count > self.white_edge_count()):
                                flag = True
                            moves += self.white_to_yellow_helper("R")
                            if (flag):
                                moves+=self.white_to_yellow_helper("Fi")
                        case (2, 1):
                            flag = False
                            initial_edge_count = self.white_edge_count()
                            self.unsolved_cube.algorithm_parser("Fi")
                            moves += " Fi"
                            if (initial_edge_count > self.white_edge_count()):
                                flag = True
                            moves += self.white_to_yellow_helper("R")
                            if (flag):
                                moves+=self.white_to_yellow_helper("F")

        moves += self.unsolved_cube.default_orientation()
        
        #print("B: ", moves)
        return moves

    def one_yellow_to_white(self, face_index, color, position):
        moves = ""
        while True:
            self.unsolved_cube.algorithm_parser("U")
            moves += " U"
            if ((self.unsolved_cube.get_cube()[face_index][0][1] == color) and self.unsolved_cube.get_cube()[1][position[0]][[position[1]]] == 'w'):
                break

        return moves
        
    def yellow_to_white(self):
        moves = " "
        faces = self.unsolved_cube.get_cube()
        for face_index in range(2, 6):
            if face_index == 2:
                moves += self.one_yellow_to_white(face_index,'b', (2,1))
                self.unsolved_cube.algorithm_parser("F F")
                moves += " F2"
            if face_index == 3:
                moves += self.one_yellow_to_white(face_index,'g', (0, 1))
                self.unsolved_cube.algorithm_parser("B B")
                moves += " B2"
            if face_index == 4:
                moves += self.one_yellow_to_white(face_index,'r', (1,2))
                self.unsolved_cube.algorithm_parser("R R")
                moves += " R2"
            if face_index == 5:
                moves += self.one_yellow_to_white(face_index,'o', (1,0))
                self.unsolved_cube.algorithm_parser("L L")
                moves += " L2"
            
        return moves
    
    def cross(self):
        moves = " "
        while (self.white_edge_count() != 4):
            moves += self.white_to_yellow()
        
        # print("TEST: ", moves)
        moves += self.yellow_to_white()
        self.cross_solved = True
        return moves
    
    def white_insert(self) -> str:
        moves = ''
        face_to_check = self.unsolved_cube.get_cube()[2]
        for i in range(4):
            #print(face_to_check[0])
            if (face_to_check[0][0] == 'w'):
                if (self.unsolved_cube.get_cube()[1][2][0] == face_to_check[1][1]):
                    self.unsolved_cube.algorithm_parser("U' L' U L")
                    moves += " U' L' U L"
                    return moves

                
            if (face_to_check[0][2] == 'w'):
                # print(face_to_check[1][1])
                # print(self.unsolved_cube.get_cube()[1][2][2])
                if (self.unsolved_cube.get_cube()[1][2][2] == face_to_check[1][1]):
                    self.unsolved_cube.algorithm_parser("U R U' R'")
                    moves += " U R U' R'"
                    return moves


            self.unsolved_cube.algorithm_parser('U')
            moves += " U"
        
        return ''

    def white_complex(self) -> str:
        """
        If a white piece is at the U layer (but not correctly oriented), orient it so it can be solved using white_insert
        """
        moves = ''
        face_to_check = self.unsolved_cube.get_cube()[2] #  Get the side facing the user
        for i in range(4):
            if 'w' in self.unsolved_cube.get_cube()[1][2]: 
                if (self.unsolved_cube.get_cube()[0][0][0] != 'w' and self.unsolved_cube.get_cube()[1][2][0] == 'w'):
                    self.unsolved_cube.algorithm_parser("L' U L")
                    moves += " L' U L"
                    return moves
                if (self.unsolved_cube.get_cube()[0][0][2] != 'w' and self.unsolved_cube.get_cube()[1][2][2] == 'w'):
                    self.unsolved_cube.algorithm_parser("R U' R'")
                    moves += " R U' R'"
                    return moves


            self.unsolved_cube.algorithm_parser('U')
            moves += ' U'
        
        return ""

    def white_bottom(self) -> str:
        moves = ''
        face_to_check = self.unsolved_cube.get_cube()[2]
        for i in range(4):
            if 'w' in face_to_check[2]:
                if (face_to_check[2][2] == 'w'):
                    self.unsolved_cube.algorithm_parser("R U' R'")
                    moves += " R U' R'"
                    return moves

                if (face_to_check[2][0] == 'w'):
                    self.unsolved_cube.algorithm_parser("L' U L")
                    moves += " L' U L"
                    return moves
                    
            self.unsolved_cube.algorithm_parser('U')
            moves += ' U'
        
        return ''

    def white_incorrectly_solved(self):
        moves = ''
        front_face = self.unsolved_cube.get_cube()[2]
        # for i in range(4):

        #     if 'w' in self.unsolved_cube.get_cube()[1][2]:
        #         if (self.unsolved_cube.get_cube()[2][1] != face_to_check[2][2]):
        #             self.unsolved_cube.algorithm_parser("R U' R'")
        #             moves += " R U' R'"
        #             return moves

        #         if (face_to_check[2][0] == face_to_check[1][1]):
        #             self.unsolved_cube.algorithm_parser("L' U' L")
        #             moves += " L' U' L"
        #             return moves


        #     self.unsolved_cube.algorithm_parser('U')
        #     moves += ' U'
        # print("White face message ", self.unsolved_cube.get_cube()[0][0][0])
        # print("Front face corner ", front_face[2][0])
        # print("Front face edge ", front_face[2][1])


        if 'w' == self.unsolved_cube.get_cube()[0][0][0] and front_face[2][0] != front_face[2][1]:
            self.unsolved_cube.algorithm_parser("L' U' L")   
            moves += " L' U' L"         
            return moves

        
        return ''

    def white(self):
        cross = ''
        moves = ''
        if (self.cross_solved):
            pass
        else:
            cross += self.cross()
            self.white_solved = True
        #print("Cross: ", cross)
        faces = ['r', 'g', 'o', 'b']

        for face in faces:
            moves += self.unsolved_cube.change_orientation(face)
            moves += self.white_incorrectly_solved()

        while not np.array_equal(self.unsolved_cube.get_cube()[0], self.solved[0]):
            for face in faces:
                moves += self.unsolved_cube.change_orientation(face)
                moves += self.white_insert()
                moves += self.white_bottom()
                moves += self.white_insert()
                moves += self.white_complex()
                moves += self.white_insert()
                moves += self.white_incorrectly_solved()
                moves += self.white_insert()
        
        #print("Put the white corners: ",  moves)
        return moves




    
    def second_layer_insert(self):
        yellow_face = self.unsolved_cube.get_cube()[1]
        front_face = self.unsolved_cube.get_cube()[2]
        left_face = self.unsolved_cube.get_cube()[5]
        right_face = self.unsolved_cube.get_cube()[4]

        moves = ''

        for i in range(4):
            # Identify if piece should be inserted in at all or not
            if (yellow_face[2][1] != 'y' and front_face[0][1] == front_face[1][1]):
                # Insert edge to the left
                if (yellow_face[2][1] == left_face[1][1]):
                    self.unsolved_cube.algorithm_parser("U' L' U L U F U' F'")
                    moves += " U' L' U L U F U' F'"
                    return moves
                # Insert edge to the right
                if (yellow_face[2][1] == right_face[1][1]):
                    self.unsolved_cube.algorithm_parser("U R U' R' U' F' U F")
                    moves += " U R U' R' U' F' U F"
                    return moves
            
            self.unsolved_cube.algorithm_parser("U")
            moves += " U"
        
        return ""  

    
    def only_yellow_pieces(self):
        yellow_face = self.unsolved_cube.get_cube()[1]
        front_face = self.unsolved_cube.get_cube()[2]
        self.unsolved_cube.save_state()

        for i in range(4):
            self.unsolved_cube.algorithm_parser("U")
            if (yellow_face[2][1] != 'y' and front_face[0][1] != 'y'):
                self.unsolved_cube.restore_state()
                return False
        self.unsolved_cube.restore_state()
        return True

    def second_layer_not_complete(self):
        counter = 0
        for face  in ['r', 'g', 'o', 'b']:
            self.unsolved_cube.change_orientation(face)
            current_face = self.unsolved_cube.get_cube()[2]
            if (current_face[1][1] == current_face[1][2] == current_face[1][0]):
                counter += 1
                #self.unsolved_cube.default_orientation()

        if counter == 4:            
            return True
        else:
            return False



    def solve_incomp_second_layer(self):
        front_face = self.unsolved_cube.get_cube()[2]
        moves = ""
        for face in ['r', 'g', 'o','b']:
            moves += self.unsolved_cube.change_orientation(face)
            if front_face[1][1] != front_face[1][0]:
                self.unsolved_cube.algorithm_parser("U' L' U L U F U' F'")
                moves += " U' L' U L U F U' F'"
            if front_face[1][1] != front_face[1][2]:
                self.unsolved_cube.algorithm_parser("U R U' R' U' F' U F")
                moves += " U R U' R' U' F' U F"

            moves += self.second_layer_insert()
        return moves
        
    def second_layer(self):
        moves = ""
        if not self.white_solved:
            self.white()
        
        self.second_layer_solved = True

        yellow_face = self.unsolved_cube.get_cube()[1]
        front_face = self.unsolved_cube.get_cube()[2]

        while (not self.only_yellow_pieces()):
            for face in ['r', 'g', 'o', 'b']:
                moves += self.unsolved_cube.change_orientation(face)
                moves += self.second_layer_insert()
        
        # self.solve_incomp_second_layer()
        while (not self.second_layer_not_complete()):
            moves += self.solve_incomp_second_layer()            
        #     for face in ['r', 'g', 'o','b']:
        #         moves += self.unsolved_cube.change_orientation(face)
        #         if front_face[1][1] != front_face[1][0]:
        #             self.unsolved_cube.algorithm_parser("U' L' U L U F U' F'")
        #             moves += " U' L' U L U F U' F'"
        #         if front_face[1][1] != front_face[1][2]:
        #             self.unsolved_cube.algorithm_parser("U R U' R' U' F' U F")
        #             moves += " U R U' R' U' F' U F"

        #         moves += self.second_layer_insert()
        #         print('Loop')
        
        # print("Second Layer: ", moves)
        return moves
    
    def check_yellow_edges(self, edges):            
        for edge in edges:
            if self.unsolved_cube.get_cube()[1][edge[0]][edge[1]] != 'y':
                return False
        
        return True
        
    
    def yellow_edge_state(self):
        counter = 0
        for i in range(4):
            # Cross
            if self.check_yellow_edges( [(0, 1), (2, 1), (1,0), (1,2)] ):
                return [0, counter]

            # Line            
            if self.check_yellow_edges( [(1, 0), (1, 2)]    ):
                return [1, counter]
            
            # L
            if self.check_yellow_edges( [(0, 1), (1,0)] ):
                return [2, counter]
            
            counter+=1
            self.unsolved_cube.algorithm_parser("U")

            
        return [3, counter]
    
    def orient_yellow_edges(self):
        moves = ""
        yellow_edge_state =  self.yellow_edge_state()
        moves += " ".join(" U" for i in range(yellow_edge_state[1]))
        match yellow_edge_state[0]:
            case 0:
                return moves
            case 1:
                self.unsolved_cube.algorithm_parser("F R U R' U' F'")
                moves += " F R U R' U' F'"
                # print("Yellow Cross: ", moves)
                return moves
            case 2:
                self.unsolved_cube.algorithm_parser(" F U R U' R' F'")
                moves += " F U R U' R' F'"
                # print("Yellow Cross: ", moves)
                return moves
            case 3:
                self.unsolved_cube.algorithm_parser(" F U R U' R' F'")
                moves += " F U R U' R' F'"
                #print("TEST: ", moves)
                moves += self.orient_yellow_edges()
                # print("Yellow Cross: ", moves)
                return moves



    def no_of_yellow_edges_permuted(self):
        counter=0
        moves = ''
        self.unsolved_cube.save_state()
        for face in ['r', 'g', 'o', 'b']:
            self.unsolved_cube.change_orientation(face)
            front_face = self.unsolved_cube.get_cube()[2]
            temp_counter = 0
            while (front_face[0][1] != front_face[1][1]):
                self.unsolved_cube.algorithm_parser('U')
                moves += ' U'
            for i in self.unsolved_cube.get_cube()[2:]:
                if i[0][1] == i[1][1]:
                    temp_counter+=1
                    if temp_counter > counter:
                        counter = temp_counter
        self.unsolved_cube.restore_state()
        return [counter, moves]

        #return counter


    def permute_yellow_edges_helper(self):
        """
        Look here for the error
        """
        moves = ""
        flag = False
        noted = []
        self.unsolved_cube.save_state()
        for face in ['r', 'g', 'o', 'b']:
            temp_moves = self.unsolved_cube.change_orientation(face)
            right_face = self.unsolved_cube.get_cube()[4]
            back_face = self.unsolved_cube.get_cube()[3]
            for i in range(4):
                if back_face[1][1] == back_face[0][1] and right_face[1][1] == right_face[0][1]:
                    #print("RESULTS: ", face, back_face[0][1], right_face[0][1])
                    noted.extend((face, right_face[0][1]))
                    #self.unsolved_cube.display_cube()
                    flag = True
                    break
                self.unsolved_cube.algorithm_parser("U")                        
                #moves += " " + "U"


        self.unsolved_cube.restore_state()
        if len(noted) != 0:
            moves += self.unsolved_cube.change_orientation(noted[1])
            front_face = self.unsolved_cube.get_cube()[2]
            while (front_face[0][1] != front_face[1][1]):
                self.unsolved_cube.algorithm_parser('U')
                moves += ' U'
            moves += self.unsolved_cube.change_orientation(noted[0])

        return moves

                            


    def permute_yellow_edges(self):
        moves = ""
        sune = " R U R' U R U2 R'"
        flag = False
        yellow_edges_permuted = self.no_of_yellow_edges_permuted()
        #moves += yellow_edges_permuted[1]
        match yellow_edges_permuted[0]:
            case 4:
                return moves
            case 1:
                self.unsolved_cube.algorithm_parser(sune)
                moves += sune
                return moves
                #self.permute_yellow_edges()
            case 2:
                moves += self.permute_yellow_edges_helper()        
                moves += sune
                self.unsolved_cube.algorithm_parser(sune)
                return moves
    

    def p_y_e(self):
        moves = ""
        while self.no_of_yellow_edges_permuted()[0] != 4:
            #moves += " " + self.no_of_yellow_edges_permuted()[1]            
            moves += " " + self.permute_yellow_edges()
        # print("Permute Yellow Edge: ", moves)
        return moves
        

    def no_of_correctly_oriented_corners(self):
        """
        Find the number of correctly oriented corners on the upper face (i.e. yellow centre facing the sky)

        Approach:
            - Check the lower right corner to see if it matches the front, right and upper layers colors
            - Change orientation to account for all 4 corners
        """
        self.unsolved_cube.save_state()
        front_face = self.unsolved_cube.get_cube()[2]
        while (front_face[0][1] != front_face[1][1]):
            self.unsolved_cube.algorithm_parser('U')

        counter = 0
        for face in 'r g o b'.split():
            self.unsolved_cube.change_orientation(face)
            yellow_face = self.unsolved_cube.get_cube()[1]
            front_face = self.unsolved_cube.get_cube()[2]                    
            right_face = self.unsolved_cube.get_cube()[4]
            colors = [yellow_face[1][1], front_face[1][1], right_face[1][1]]
            corner = [yellow_face[2][2], front_face[0][2], right_face[0][2]]
            colors.sort()
            corner.sort()
            if corner == colors:
                # print("FACE: ", face)
                # print("CORNERS: ", corner)
                # print("COLORS: ", colors)
                counter+= 1
        
        self.unsolved_cube.restore_state()
        return counter

        #print(counter)
        

        
    

    def orient_yellow_corners(self):
        moves = ""
        #moves += self.no_of_yellow_edges_permuted()[1]
        front_face = self.unsolved_cube.get_cube()[2]
        while (front_face[0][1] != front_face[1][1]):
            self.unsolved_cube.algorithm_parser('U')
            moves += ' U'
        alg = " U R U' L' U R' U' L"
        print("TEST:" , moves)
        counter = self.no_of_correctly_oriented_corners()
        # print("COUNTER: ", counter)
        # print(self.unsolved_cube.get_cube())
        
        match counter:
            case 4:
                return moves
            case 1:
                noted = []
                #self.unsolved_cube.save_state()
                for face in ['r', 'g', 'o', 'b']:
                    moves += self.unsolved_cube.change_orientation(face)
                    yellow_face = self.unsolved_cube.get_cube()[1]
                    front_face = self.unsolved_cube.get_cube()[2]                    
                    right_face = self.unsolved_cube.get_cube()[4]
                    colors = [yellow_face[1][1], front_face[1][1], right_face[1][1]]
                    if yellow_face[2][2] in colors and front_face[0][2] in colors and right_face[0][2] in colors:
                        #noted.append(front_face)
                        break

                #self.unsolved_cube.restore_state()
                #moves += self.unsolved_cube.change_orientation(noted[0])
                                
                self.unsolved_cube.algorithm_parser(alg)
                moves += alg
                # print("Orient yellow corners: ", moves)
                return moves
            case 0:
                self.unsolved_cube.algorithm_parser(alg)
                moves += alg
                #moves += self.orient_yellow_corners()
                # print("Orient yellow corners: ", moves)
                return moves
            




        #print("Orient yellow corners: ", moves)

    def o_y_c(self):
        moves = ""
        while self.no_of_correctly_oriented_corners() != 4:
            moves += self.orient_yellow_corners()
        
        # print("Orient Yellow Corners: ", moves)
        return moves
    
    def permute_yellow_corners(self):
        alg = " R' D' R D"
        moves = ""

        yellow_face = self.unsolved_cube.get_cube()[1]
        for i in range(4):
            while yellow_face[2][2] != 'y':
                moves += alg
                self.unsolved_cube.algorithm_parser(alg)
            moves += " U"
            self.unsolved_cube.algorithm_parser(" U")
        

        # print("Permute Yellow Corners (AND SOLVE THE CUBE): ", moves)
        return moves
    

    def solve(self):
        moves = ""
        moves += " " + self.cross()
        moves += " " + self.white()
        moves += " " + self.white()
        moves += " " + self.second_layer()
        # print(moves)
        # print("------------------------------------")
        # print(moves)
        # print("------------------------------------")

        moves += " " + self.orient_yellow_edges()
        # print(moves)

        moves += " " + self.p_y_e()
        # print(moves)

        moves += " " + self.o_y_c()
        moves += " " + self.permute_yellow_corners()
        #print("SOLUTION: ", moves)
        return moves
        # print("------------------------------------")
       # print(moves)
    
    def human_readable_solver(self):
        moves = {}
        cross = self.cross()
        moves['cross'] = cross
        
        white = self.white()
        moves['white'] = white

        moves['second_layer'] = self.second_layer()

        # print(moves)
        # print("------------------------------------")
        # print(moves)
        # print("------------------------------------")

        moves['orient_yellow_edge'] = self.orient_yellow_edges()
        # print(moves)

        moves['permute_yellow_edge'] = self.p_y_e()

        moves['orient_yellow_corners'] = self.o_y_c()
        moves['permute_yellow_corners'] = self.permute_yellow_corners()

        final_moves = """
        Cross: {} \n
        Solving the white face: {} \n
        Second Layer: {} \n
        Orient Yellow Edges: {} \n
        Permute Yellow Edges: {} \n
        Orient Yellow Corners: {} \n
        Permute Yellow Corners: {}

        """.format(cross, white, moves['second_layer'] ,moves['orient_yellow_edge'], moves['permute_yellow_edge'], moves['orient_yellow_corners'],moves['permute_yellow_corners'])
        #print("SOLUTION: ", moves)
        return final_moves










    
















                
        
            




    
 


            
            
        
        
        
    


"""
Solving the first layer (i.e. solve the white face)

Three cases:

1) White corner piece is oriented correctly
    -> If R/L' results in the same color as 7th piece on the 6th/8th piece, do one of the following:
        -> R' F R F' (8th)
        -> L F' L F  (6th)

2) White not oriented properly -- on third layer
    -> Put piece on top of white unsolved piece (keep track of unsolved pieces)
        -> R/L' U2 R'/L (make it case one and solve)

3) White not oriented properly 
    -> Li U L
    -> R U' R'
    (i.e. make it case one and solve)

"""

"""
Approach to white cross functions:
When a complex function returns True, do white_insert for all faces
"""


