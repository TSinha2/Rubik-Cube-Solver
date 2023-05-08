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
    # print(np.equal(correct_array,fix_orientation(cube_array)))
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





if __name__ == "__main__":
    test_right()
    test_up()
    test_one()
    test_two()
    test_three()
    test_four()
    print("All tests passed")