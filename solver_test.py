from pyTwistyScrambler import scrambler333
import numpy as np
from solver import Solver
from cube import Cube



correct_array = np.array(
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

rip = []



counter = 0 
for i in range(1000):
    scramble = scrambler333.get_WCA_scramble()
    #scramble = i
    print("SCRAMBLE: ", scramble)
    test_cube = Cube()
    test_cube.algorithm_parser(scramble)
    a = Solver(test_cube)
    move = ''
    try:
        move += a.solve()
    except:
        rip.append(scramble)

    test_cube.change_orientation('b')
    test_cube2 = Cube()
    test_cube2.algorithm_parser(scramble)
    test_cube2.algorithm_parser(move)
    test_cube2.change_orientation('b')
    while (test_cube2.get_cube()[2][0][1] != test_cube2.get_cube()[2][1][1]):
        test_cube2.algorithm_parser('U')

    # print(test_cube2.get_cube())
    print("-------------------------------------------------------------------------------------------")
    if (correct_array == test_cube2.get_cube()).all():
        counter += 1
    else:
        rip.append(scramble)


print("WE SOLVED: ", counter)
print(rip)


