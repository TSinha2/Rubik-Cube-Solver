# Rubik-Cube-Solver

A simple Rubik's Cube Solver made using Python [Work in Progress] . 

This repository consists of "cube.py" -- a class to represent a 3x3 Rubik's Cube; "solver.py" -- outputs the beginner method solution, using the previously mentioned Cube class, described on the <a href='https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/'>Ruwix</a> website.

Note that the solver is fully functional, and its usage is described below:

```
from cube import Cube
from solver import Solver
"""
Each face is represented in the following format:
  1 2 3
  4 5 6
  7 8 9

To describe a face as a string, just write dowm the colors as characters in the order mentioned above
For example:, "w" - white",  b" - blue and so forth.
"""
  
# State of a scrambled cube. Note that you need to mention all six sides in the following order: 
# (1) Side with White Centre, (2) Side with Yellow Centre, (3) Side with Blue Centre, (4) Side with Green Centre, (5) Side with Red Centre, (6) Side with Orange Centre
sample_cube = Cube("bybwwoogwbwooybrrrybwgbwroogbwygoorbgyygrrybgrggwoywry")
sample_solver = Solver(sample_cube)
sample_solver.solve() # Returns string with moves to solve Cube 

# Alternatively, you can use Rubik's Cube Move Notation to input a scramble as shown below: 
sample_cube_2 = Cube()
sample_cube_2.algorithm_parser("B2 L' D' B2 R F U2 F' R2 D F2 R F2 B2 R D2 R' U2")
sample_solver_2 = Solver(sample_cube)
sample_solver_2.solve() # Returns string with moves to solve Cube 
```

To use the webcam to get the scramble: 
``` python face_id.py```
First, 'teach' the program how the colors look. Do this by FIRSTLY putting the white color from the cube in the centre of the square on the webcam, and pressing ```c```. Repeat this process for yellow, blue, green, red and orange. 

After teaching the cube, how the colors look, put in the faces in the following order: white, yellow, blue, green, red and orange.  To put in a face, match it to the grid on the webcam as best as you possibly can, and then pressing ```space```. After the 6th (orange) face, you will have a string representing the cube state that can bes solved using the method described above. 

Note using the webcam to get the scramble is not perfectly accurate, and often mistakes white for yellow, orange for red and vice versa (in both cases). 

Optional:
To visualize how the cube looked (in a 2D "net"), there is also a file called display.py, that uses the pygame library. It was primarily used for debugging --- however if you want to use it, just modify "test_cube" in that file with your own scramble and run it: ```python3 display.py```

