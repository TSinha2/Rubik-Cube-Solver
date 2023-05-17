from cube import Cube


edges = [(0, 1), (1, 0), (1, 2), (2, 1)]


class Solver:
    def __init__(self, unsolved_cube) -> None:
        self.unsolved_cube = unsolved_cube
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
    
    def one_move_white_onto_yellow(self, move):
        initial_white_edge_count = self.white_edge_count()
        self.unsolved_cube.save_state()
        u_turns = 0
        moves = []
        while True:
            for i in range(u_turns):
                self.unsolved_cube.algorithm_parser("U")
            self.unsolved_cube.algorithm_parser(move)
            if (self.white_edge_count() > initial_white_edge_count):
                for i in range(u_turns):
                    moves.append("U")
                moves.append(move)
                self.unsolved_cube.save_state()
                break
            else:
                u_turns += 1
                self.unsolved_cube.restore_state()
        
        return ' '.join(i for i in moves)

    def two_move_white_onto_yellow(self, move_one, move_two):
        initial_white_edge_count = self.white_edge_count()
        self.unsolved_cube.algorithm_parser(move_one)
        flag = False
        if (self.white_edge_count() < initial_white_edge_count):
            flag = True
        
        if flag == False:
            moves = []
            moves.append(move_one)
            moves.append(self.one_move_white_onto_yellow(move_two))
            return ' '.join(i for i in moves)
        else:
            moves = []
            moves.append(move_one)
            moves.append(self.one_move_white_onto_yellow(move_two))
            moves.append(self.one_move_white_onto_yellow(' '.join(move_one for i in range(3))))
            return ' '.join(i for i in moves)
            
    def all_white_onto_yellow(self):
        white_edges = self.find_white_edges()
        faces = self.unsolved_cube.get_cube()
        moves = []
        for face_index, row, row_index in white_edges:
            face = faces[face_index]

            #print(face[row][row_index])

            if face_index == 1:
                pass

            elif face_index == 0:
                if row == 1:
                    if row_index == 2:
                        moves.append(self.one_move_white_onto_yellow("R R"))
                    if row_index == 0:
                        moves.append(self.one_move_white_onto_yellow("L L"))
                if row == 0:
                    moves.append(self.one_move_white_onto_yellow("F F"))
                if row == 2:
                    moves.append(self.one_move_white_onto_yellow("B B"))

            elif face_index == 2:
                if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("R"))
                if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("Li"))
                if row == 0 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("F", "R"))
                if row == 2 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("F", "Li"))

            elif face_index == 3:
                if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("Ri"))
                if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("L"))
                if row == 0 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Bi", "Ri"))
                if row == 2 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Bi", "L"))
            
            elif face_index == 4:
                if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("B"))
                if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("Fi"))
                if row == 0 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Ri", "Fi"))
                if row == 2 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Ri", "B"))
                
            elif face_index == 5:
                if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("Bi"))
                if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                    moves.append(self.one_move_white_onto_yellow("F"))
                if row == 0 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Li", "Bi"))
                if row == 2 and face[row][row_index] == 'w':
                    moves.append(self.two_move_white_onto_yellow("Li", "F"))

        return moves

    def one_yellow_to_white(self, face_index, color, position):
        moves = []
        while True:
            self.unsolved_cube.algorithm_parser("U")
            moves.append("U")
            if ((self.unsolved_cube.get_cube()[face_index][0][1] == color) and self.unsolved_cube.get_cube()[1][position[0]][[position[1]]] == 'w'):
                break

        return moves
        
    def yellow_to_white(self):
        moves = []
        faces = self.unsolved_cube.get_cube()
        for face_index in range(2, 6):
            if face_index == 2:
                moves.append(self.one_yellow_to_white(face_index,'b', (2,1)))
                self.unsolved_cube.algorithm_parser("F F")
                moves.append("F F")
            if face_index == 3:
                moves.append(self.one_yellow_to_white(face_index,'g', (0, 1)))
                self.unsolved_cube.algorithm_parser("B B")
                moves.append("B B")
            if face_index == 4:
                moves.append(self.one_yellow_to_white(face_index,'r', (1,2)))
                self.unsolved_cube.algorithm_parser("R R")
                moves.append("R R")
            if face_index == 5:
                moves.append(self.one_yellow_to_white(face_index,'o', (1,0)))
                self.unsolved_cube.algorithm_parser("L L")
                moves.append("L L")
            
        return moves

    def cross(self):
        moves = []
        move_str = ' '
        while (self.white_edge_count() != 4):
            moves.append(self.all_white_onto_yellow())

        print(moves)
        for i in range(len(moves)):
            if i != []:
                move_str += ' '.join(j for j in moves[i])
                move_str += ' '
        a = self.yellow_to_white()
        for i in a:
            if type(i) == list:
                move_str += ' '.join('U' for i in range(len(i)))
                move_str += ' '
            else:
                move_str += i
                move_str += ' '
        print(move_str)
        
        return move_str
    
    def white_insert(self, face):
        try:
            self.unsolved_cube.change_orientation(face)
        except:
            self.unsolved_cube.default_orientation()
        face_to_check = self.unsolved_cube.get_cube()[2]
        for i in range(4):
            #print(face_to_check[0])
            if (face_to_check[0][0] == 'w'):
                print("T1")
                if (self.unsolved_cube.get_cube()[1][2][0] == face_to_check[1][1]):
                    self.unsolved_cube.algorithm_parser("U' L' U L")
                
            if (face_to_check[0][2] == 'w'):
                print("T2")
                # print(face_to_check[1][1])
                # print(self.unsolved_cube.get_cube()[1][2][2])
                if (self.unsolved_cube.get_cube()[1][2][2] == face_to_check[1][1]):
                    self.unsolved_cube.algorithm_parser("U R U' R'")

            self.unsolved_cube.algorithm_parser('U')   

    
    def white(self):
        self.white_insert('r')
        self.unsolved_cube.default_orientation()
        self.white_insert('g')
        self.unsolved_cube.default_orientation()
        self.white_insert('o')
        self.unsolved_cube.default_orientation()
        self.white_insert('b')



            
            
        
        
        
    


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



#self.unsolved_cube.algorithm_parser("Di R")
# print(white_edge_count())
#b = find_white_edges()
# self.unsolved_cube.algorithm_parser("F R F")
# print(b)
test_cube = Cube()
a = Solver(test_cube)
test_cube.algorithm_parser(" L U U F F R L Fi Ri U U Ri Fi U U L B B Di B B D F Di L B Ri Fi Ri Di R")

a.cross()
test_cube.algorithm_parser(" R U R'")
#print("INITIALLY")
#print(test_cube.get_cube()[0])
a.white()
print(test_cube.get_cube()[0])
