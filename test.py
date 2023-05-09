from cgi import test
from solver import Cube
import numpy as np


def fix_orientation(cube_array):
    cube_array[3] = np.fliplr(cube_array[3])
    cube_array[4] = np.fliplr(cube_array[4])
    return cube_array


def test_right():
    test_cube = Cube()
    test_cube.turn_vertical(2)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'g'],
    ['w', 'w' ,'g'],
    ['w', 'w' ,'g']],

    [['y', 'y' ,'b'],
    ['y', 'y', 'b'],
    ['y', 'y' ,'b']],

    [['b', 'b' ,'w'],
    ['b', 'b' ,'w'],
    ['b', 'b', 'w']],

    [['y' ,'g' ,'g'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['o','o' ,'o'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    assert (correct_array == fix_orientation(cube_array)).all()
    # print(np.equal(a,b))

def test_up():
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['w', 'w' ,'w']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['y', 'y' ,'y']],

    [['r', 'r' ,'r'],
    ['b', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['o' ,'o' ,'o'],
    ['g', 'g' ,'g'],
    ['g' ,'g' ,'g']],

    [['g', 'g' ,'g'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['b','b' ,'b'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    assert (correct_array == fix_orientation(cube_array)).all()


def test_one():
    """
    Tests the algorithm 'R U'
    """
    test_cube = Cube()
    test_cube.turn_vertical(2)
    test_cube.turn_horizontal(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'g'],
    ['w', 'w' ,'g'],
    ['w', 'w' ,'g']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['b', 'b' ,'b']],

    [['r', 'r' ,'r'],
    ['b', 'b' ,'w'],
    ['b', 'b', 'w']],

    [['o' ,'o' ,'o'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['y', 'g' ,'g'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['b','b' ,'w'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()


def test_two():
    """
    Tests the algorithm 'U R'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'g'],
    ['w', 'w' ,'g'],
    ['w', 'w' ,'o']],

    [['y', 'y' ,'r'],
    ['y', 'y', 'b'],
    ['y', 'y' ,'b']],

    [['r', 'r' ,'w'],
    ['b', 'b' ,'w'],
    ['b', 'b', 'w']],

    [['y' ,'o' ,'o'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['r', 'r' ,'g'],
    ['r', 'r' ,'g'],
    ['r', 'r' ,'g']],

    [['b','b' ,'b'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    # print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_three():
    """
    Tests the algorithm 'R U R'
    """
    test_cube = Cube()
    test_cube.turn_vertical(2)
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'y'],
    ['w', 'w' ,'y'],
    ['w', 'w' ,'o']],

    [['y', 'y' ,'r'],
    ['y', 'y', 'w'],
    ['b', 'b' ,'w']],

    [['r', 'r' ,'g'],
    ['b', 'b' ,'g'],
    ['b', 'b', 'g']],

    [['b' ,'o' ,'o'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['r', 'r' ,'y'],
    ['r', 'r' ,'g'],
    ['r', 'r' ,'g']],

    [['b','b' ,'w'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    # print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_four():
    """
    Tests the algorithm 'U R U'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    test_cube.turn_horizontal(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'g'],
    ['w', 'w' ,'g'],
    ['w', 'w' ,'o']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['b', 'b' ,'r']],

    [['r', 'r' ,'g'],
    ['b', 'b' ,'w'],
    ['b', 'b', 'w']],

    [['b' ,'b' ,'b'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['y', 'o' ,'o'],
    ['r', 'r' ,'g'],
    ['r', 'r' ,'g']],

    [['r','r' ,'w'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_five():
    """
    Tests the algorithm 'Ui'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['w', 'w' ,'w']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['y', 'y' ,'y']],

    [['o', 'o' ,'o'],
    ['b', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['r' ,'r' ,'r'],
    ['g', 'g' ,'g'],
    ['g' ,'g' ,'g']],

    [['b', 'b' ,'b'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['g','g' ,'g'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_six():
    """
    Tests the algorithm 'Ui Ri'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'o'],
    ['w', 'w' ,'b'],
    ['w', 'w' ,'b']],

    [['y', 'y' ,'g'],
    ['y', 'y', 'g'],
    ['y', 'y' ,'r']],

    [['o', 'o' ,'y'],
    ['b', 'b' ,'y'],
    ['b', 'b', 'y']],

    [['w' ,'r' ,'r'],
    ['w', 'g' ,'g'],
    ['w' ,'g' ,'g']],

    [['b', 'r' ,'r'],
    ['b', 'r' ,'r'],
    ['b', 'r' ,'r']],

    [['g','g' ,'g'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_seven():
    """
    Tests the algorithm 'Ui Ri U U U'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'o'],
    ['w', 'w' ,'b'],
    ['w', 'w' ,'b']],

    [['g', 'g' ,'r'],
    ['y', 'y', 'y'],
    ['y', 'y' ,'y']],

    [['g', 'g' ,'g'],
    ['b', 'b' ,'y'],
    ['b', 'b', 'y']],

    [['b' ,'r' ,'r'],
    ['w', 'g' ,'g'],
    ['w' ,'g' ,'g']],

    [['o', 'o' ,'y'],
    ['b', 'r' ,'r'],
    ['b', 'r' ,'r']],

    [['w','r' ,'r'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()



def test_eight():
    """
    Tests the algorithm 'Li'
    """
    test_cube = Cube()
    test_cube.turn_vertical(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['g' ,'w', 'w'],
    ['g', 'w' ,'w'],
    ['g', 'w' ,'w']],

    [['b', 'y' ,'y'],
    ['b', 'y', 'y'],
    ['b', 'y' ,'y']],

    [['w', 'b' ,'b'],
    ['w', 'b' ,'b'],
    ['w', 'b', 'b']],

    [['g' ,'g' ,'y'],
    ['g', 'g' ,'y'],
    ['g' ,'g' ,'y']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['o','o' ,'o'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()

def test_nine():
    """
    Tests the algorithm 'Li Di'
    """
    test_cube = Cube()
    test_cube.turn_vertical(0)
    test_cube.turn_horizontal(2)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['g', 'g' ,'g']],

    [['b', 'y' ,'y'],
    ['b', 'y', 'y'],
    ['b', 'y' ,'y']],

    [['w', 'b' ,'b'],
    ['w', 'b' ,'b'],
    ['r', 'r', 'r']],

    [['g' ,'g' ,'y'],
    ['g', 'g' ,'y'],
    ['o' ,'o' ,'o']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['g', 'g' ,'y']],

    [['o','o' ,'o'],
    ['o', 'o' ,'o'],
    ['w' ,'b' ,'b']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    assert (correct_array == fix_orientation(cube_array)).all()


def test_ten():
    """
    Tests the algorithm 'Li Di Li'
    """
    test_cube = Cube()
    test_cube.turn_vertical(0)
    test_cube.turn_horizontal(2)
    test_cube.turn_vertical(0)
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['o' ,'w', 'w'],
    ['y', 'w' ,'w'],
    ['y', 'g' ,'g']],

    [['w', 'y' ,'y'],
    ['w', 'y', 'y'],
    ['r', 'y' ,'y']],

    [['w', 'b' ,'b'],
    ['w', 'b' ,'b'],
    ['g', 'r', 'r']],

    [['g' ,'g' ,'b'],
    ['g', 'g' ,'b'],
    ['o' ,'o' ,'b']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['g', 'g' ,'y']],

    [['o','o' ,'b'],
    ['o', 'o' ,'b'],
    ['o' ,'o' ,'w']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()

def test_eleven():
    """
    Tests the algorithm 'D L Di Li'
    """
    test_cube = Cube()
    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)

    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)

    test_cube.turn_horizontal(2)

    test_cube.turn_vertical(0)

    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['o' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['w', 'b' ,'o']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['b', 'y' ,'y']],

    [['w', 'b' ,'b'],
    ['w', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['g' ,'g' ,'g'],
    ['g', 'g' ,'g'],
    ['g' ,'o' ,'r']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'w']],

    [['o','o' ,'o'],
    ['o', 'o' ,'o'],
    ['g' ,'g' ,'y']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()

def test_twelve():
    """
    Tests the algorithm 'R U L D Ri Ui Li Di'
    """
    test_cube = Cube()

    test_cube.turn_vertical(2)

    test_cube.turn_horizontal(0)

    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)

    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)

    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)

    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)

    test_cube.turn_vertical(0)

    test_cube.turn_horizontal(2)


 
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['r' ,'w', 'w'],
    ['b', 'w' ,'g'],
    ['r', 'w' ,'w']],

    [['o', 'y' ,'o'],
    ['y', 'y', 'b'],
    ['o', 'g' ,'o']],

    [['b', 'o' ,'b'],
    ['w', 'b' ,'y'],
    ['y', 'r', 'b']],

    [['g' ,'r' ,'g'],
    ['w', 'g' ,'y'],
    ['g' ,'o' ,'y']],

    [['y', 'r' ,'y'],
    ['g', 'r' ,'b'],
    ['r', 'r' ,'r']],

    [['w','b' ,'w'],
    ['o', 'o' ,'g'],
    ['g' ,'o' ,'b']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()



def test_thirteen():
    """
    Tests the algorithm 'F'
    """
    test_cube = Cube()

    test_cube.turn_sideways(2)
 
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['r' ,'r', 'r'],
    ['w', 'w' ,'w'],
    ['w', 'w' ,'w']],

    [['y', 'y' ,'y'],
    ['y', 'y', 'y'],
    ['o', 'o' ,'o']],

    [['b', 'b' ,'b'],
    ['b', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['g' ,'g' ,'g'],
    ['g', 'g' ,'g'],
    ['g' ,'g' ,'g']],

    [['y', 'r' ,'r'],
    ['y', 'r' ,'r'],
    ['y', 'r' ,'r']],

    [['o','o','w'],
    ['o', 'o' ,'w'],
    ['o' ,'o' ,'w']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()


def test_fourteen():
    """
    Tests the algorithm 'F R F'
    """
    test_cube = Cube()

    test_cube.turn_sideways(2)
    test_cube.turn_vertical(2)
    test_cube.turn_sideways(2)

 
    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['r' ,'r', 'y'],
    ['w', 'w' ,'g'],
    ['w', 'w' ,'g']],

    [['y', 'y' ,'b'],
    ['y', 'y', 'b'],
    ['w', 'w' ,'w']],

    [['b', 'b' ,'b'],
    ['b', 'b' ,'b'],
    ['w', 'w', 'r']],

    [['o' ,'g' ,'g'],
    ['y', 'g' ,'g'],
    ['y' ,'g' ,'g']],

    [['o', 'y' ,'y'],
    ['o', 'r' ,'r'],
    ['b', 'r' ,'r']],

    [['o','o','r'],
    ['o', 'o' ,'r'],
    ['o' ,'o' ,'g']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()


def test_fifteen():
    """
    Tests the algorithm ' F R U Ri Ui Fi '
    """
    test_cube = Cube()

    test_cube.turn_sideways(2)

    test_cube.turn_vertical(2)

    test_cube.turn_horizontal(0)

    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)

    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)

    test_cube.turn_sideways(2)
    test_cube.turn_sideways(2)
    test_cube.turn_sideways(2)

    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['w', 'w' , 'w']],

    [['y', 'y' ,'o'],
    ['y', 'y', 'b'],
    ['y', 'g' ,'o']],

    [['r', 'y' ,'b'],
    ['b', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['g' ,'r' ,'r'],
    ['g', 'g' ,'g'],
    ['g' ,'g' ,'g']],

    [['y', 'y' ,'y'],
    ['r', 'r' ,'r'],
    ['r', 'r' ,'r']],

    [['g','o','b'],
    ['o', 'o' ,'o'],
    ['o' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()



def test_sixteen():
    """
    Tests the algorithm ' Bi '
    """
    test_cube = Cube()

    test_cube.turn_sideways(0)


    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'w'],
    ['w', 'w' ,'w'],
    ['r', 'r' , 'r']],

    [['o', 'o' ,'o'],
    ['y', 'y', 'y'],
    ['y', 'y' ,'y']],

    [['b', 'b' ,'b'],
    ['b', 'b' ,'b'],
    ['b', 'b', 'b']],

    [['g' ,'g' ,'g'],
    ['g', 'g' ,'g'],
    ['g' ,'g' ,'g']],

    [['r', 'r' ,'y'],
    ['r', 'r' ,'y'],
    ['r', 'r' ,'y']],

    [['w','o','o'],
    ['w', 'o' ,'o'],
    ['w' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()


def test_seventeen():
    """
    Tests the algorithm ' Bi R Bi'
    """
    test_cube = Cube()

    test_cube.turn_sideways(0)
    test_cube.turn_vertical(2)
    test_cube.turn_sideways(0)


    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'g'],
    ['w', 'w' ,'g'],
    ['y', 'r' , 'r']],

    [['w', 'w' ,'w'],
    ['y', 'y', 'b'],
    ['y', 'y' ,'b']],

    [['b', 'b' ,'w'],
    ['b', 'b' ,'w'],
    ['b', 'b', 'r']],

    [['g' ,'g' ,'g'],
    ['g', 'g' ,'g'],
    ['y' ,'y' ,'o']],

    [['r', 'r' ,'o'],
    ['r', 'r' ,'o'],
    ['y', 'y' ,'b']],

    [['r','o','o'],
    ['r', 'o' ,'o'],
    ['g' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()



def test_eighteen():
    """
    Tests the algorithm ' R U L D F B Ri Ui Li Di Fi Bi'
    """
    test_cube = Cube()

    #R
    test_cube.turn_vertical(2)
    
    #U
    test_cube.turn_horizontal(0)

    #L (Li * 3)
    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)
    test_cube.turn_vertical(0)

    #D (Di *3)
    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)
    test_cube.turn_horizontal(2)


    #F 
    test_cube.turn_sideways(2)

    #B (Bi * 3)
    test_cube.turn_sideways(0)
    test_cube.turn_sideways(0)
    test_cube.turn_sideways(0)

    #Ri (R * 3)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)
    test_cube.turn_vertical(2)

    #Ui (U * 3)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)
    test_cube.turn_horizontal(0)

    #Li
    test_cube.turn_vertical(0)

    #Di
    test_cube.turn_horizontal(2)

    #Fi
    test_cube.turn_sideways(2)
    test_cube.turn_sideways(2)
    test_cube.turn_sideways(2)

    #Bi
    test_cube.turn_sideways(0)



    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['r' ,'g', 'b'],
    ['r', 'w' ,'o'],
    ['r', 'b' , 'w']],

    [['o', 'y' ,'o'],
    ['o', 'y', 'b'],
    ['o', 'g' ,'y']],

    [['b', 'y' ,'b'],
    ['o', 'b' ,'b'],
    ['b', 'w', 'o']],

    [['g' ,'r' ,'g'],
    ['g', 'g' ,'y'],
    ['g' ,'w' ,'y']],

    [['r', 'y' ,'y'],
    ['r', 'r' ,'r'],
    ['y', 'w' ,'r']],

    [['w','b','w'],
    ['o', 'o' ,'g'],
    ['g' ,'w' ,'w']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()


def test_nineteen():
    """
    Tests the algorithm ' R Bi R'
    """
    test_cube = Cube()


    test_cube.turn_vertical(2)
    test_cube.turn_sideways(0)
    test_cube.turn_vertical(2)


    cube_array = test_cube.get_cube()
    correct_array = np.array(
    [[['w' ,'w', 'y'],
    ['w', 'w' ,'g'],
    ['r', 'r' , 'g']],

    [['o', 'o' ,'w'],
    ['y', 'y', 'w'],
    ['y', 'y' ,'w']],

    [['b', 'b' ,'g'],
    ['b', 'b' ,'g'],
    ['b', 'b', 'r']],

    [['b' ,'g' ,'g'],
    ['b', 'g' ,'g'],
    ['o' ,'y' ,'y']],

    [['r', 'r' ,'r'],
    ['r', 'r' ,'r'],
    ['b', 'y' ,'y']],

    [['w','o','o'],
    ['w', 'o' ,'o'],
    ['g' ,'o' ,'o']]]
    )
    #print(np.equal(correct_array,fix_orientation(cube_array)))
    #test_cube.display_cube()
    assert (correct_array == fix_orientation(cube_array)).all()





if __name__ == "__main__":
    test_right()
    test_up()
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()
    test_six()    
    test_seven()    
    test_eight()
    test_nine()
    test_ten() 
    test_eleven()  
    test_twelve()
    test_thirteen() 
    test_fourteen()   
    test_fifteen()   
    test_sixteen()    
    test_seventeen()  
    test_eighteen() 
    test_nineteen()     
    print("All tests passed")