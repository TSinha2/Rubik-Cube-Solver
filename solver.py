from cube import Cube

unsolved_cube = Cube()

edges = [(0, 1), (1, 0), (1, 2), (2, 1)]


def find_white_edges():
    """
    Return array of white edges in following format: 
    [  (face_index, row, row_index)   ]
    """
    faces = unsolved_cube.get_cube()
    white_edges = []
    for face_index in range(6):
        face = faces[face_index]
        for row, edge in edges:
            if face[row][edge] == 'w':
                white_edges.append((face_index, row, edge))
    
    return white_edges

def white_edge_count():
    """
    Returns the number of white edges on yellow faces
    """
    count = 0
    faces = unsolved_cube.get_cube()
    yellow_face = faces[1]
    for row, edge in edges:
        if yellow_face[row][edge] == 'w':
            count += 1
    
    return count
    
def one_move_white_onto_yellow(move):
    initial_white_edge_count = white_edge_count()
    unsolved_cube.save_state()
    u_turns = 0
    moves = []
    while True:
        for i in range(u_turns):
            unsolved_cube.algorithm_parser("U")
        unsolved_cube.algorithm_parser(move)
        if (white_edge_count() > initial_white_edge_count):
            for i in range(u_turns):
                moves.append("U")
            moves.append(move)
            unsolved_cube.save_state()
            break
        else:
            u_turns += 1
            unsolved_cube.restore_state()
    
    return ' '.join(i for i in moves)

def two_move_white_onto_yellow(move_one, move_two):
    initial_white_edge_count = white_edge_count()
    unsolved_cube.algorithm_parser(move_one)
    flag = False
    if (white_edge_count() < initial_white_edge_count):
        flag = True
    
    if flag == False:
        moves = []
        moves.append(move_one)
        moves.append(one_move_white_onto_yellow(move_two))
        return ' '.join(i for i in moves)
    else:
        moves = []
        moves.append(move_one)
        moves.append(one_move_white_onto_yellow(move_two))
        moves.append(one_move_white_onto_yellow(' '.join(move_one for i in range(3))))
        return ' '.join(i for i in moves)
        




def all_white_onto_yellow():
    white_edges = find_white_edges()
    faces = unsolved_cube.get_cube()
    moves = []
    for face_index, row, row_index in white_edges:
        face = faces[face_index]

        #print(face[row][row_index])

        if face_index == 1:
            pass

        elif face_index == 0:
            if row == 1:
                if row_index == 2:
                    moves.append(one_move_white_onto_yellow("R R"))
                if row_index == 0:
                    moves.append(one_move_white_onto_yellow("L L"))
            if row == 0:
                moves.append(one_move_white_onto_yellow("F F"))
            if row == 2:
                moves.append(one_move_white_onto_yellow("B B"))

        elif face_index == 2:
            if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("R"))
            if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("Li"))
            if row == 0 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("F", "R"))
            if row == 2 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("F", "Li"))

        elif face_index == 3:
            if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("Ri"))
            if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("L"))
            if row == 0 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Bi", "Ri"))
            if row == 2 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Bi", "L"))
        
        elif face_index == 4:
            if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("B"))
            if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("Fi"))
            if row == 0 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Ri", "Fi"))
            if row == 2 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Ri", "B"))
            
        elif face_index == 5:
            if row == 1 and row_index == 0 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("Bi"))
            if row == 1 and row_index == 2 and face[row][row_index] == 'w':
                moves.append(one_move_white_onto_yellow("F"))
            if row == 0 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Li", "Bi"))
            if row == 2 and face[row][row_index] == 'w':
                moves.append(two_move_white_onto_yellow("Li", "F"))



    return moves

def one_yellow_to_white(face_index, color, position):
    moves = []
    while True:
        unsolved_cube.algorithm_parser("U")
        moves.append("U")
        if ((unsolved_cube.get_cube()[face_index][0][1] == color) and unsolved_cube.get_cube()[1][position[0]][[position[1]]] == 'w'):
            break

    return moves
    
        



def yellow_to_white():
    moves = []
    faces = unsolved_cube.get_cube()
    for face_index in range(2, 6):
        if face_index == 2:
            moves.append(one_yellow_to_white(face_index,'b', (2,1)))
            unsolved_cube.algorithm_parser("F F")
            moves.append("F F")
        if face_index == 3:
            moves.append(one_yellow_to_white(face_index,'g', (0, 1)))
            unsolved_cube.algorithm_parser("B B")
            moves.append("B B")
        if face_index == 4:
            moves.append(one_yellow_to_white(face_index,'r', (1,2)))
            unsolved_cube.algorithm_parser("R R")
            moves.append("R R")
        if face_index == 5:
            moves.append(one_yellow_to_white(face_index,'o', (1,0)))
            unsolved_cube.algorithm_parser("L L")
            moves.append("L L")
        
    return moves




def cross():
    moves = []
    move_str = ' '
    while (white_edge_count() != 4):
        moves.append(all_white_onto_yellow())

    print(moves)
    for i in range(len(moves)):
        if i != []:
            move_str += ' '.join(j for j in moves[i])
            move_str += ' '
    a = yellow_to_white()
    for i in a:
        if type(i) == list:
            move_str += ' '.join('U' for i in range(len(i)))
            move_str += ' '
        else:
            move_str += i
            move_str += ' '
    print(move_str)
    
    return move_str
    
    
    
    






#unsolved_cube.algorithm_parser("Di R")
# print(white_edge_count())
#b = find_white_edges()
# unsolved_cube.algorithm_parser("F R F")
# print(b)

