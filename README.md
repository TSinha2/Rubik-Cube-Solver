# Rubik-Cube-Solver

A simple Rubik's Cube Solver made using Python [Work in Progress] . 

This repository consists of the following files: 
- "cube.py" -- a class to represent a 3x3 Rubik's Cube; 
- "solver.py" -- outputs the beginner method solution, using the previously mentioned Cube class, described on the <a href='https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/'>Ruwix</a> website. 
- "face_id.py" -- uses the opencv library to get the state of the Rubik Cube (to be used by solver)
- "new_disp.py" -- use Custom TKinter to make a Rubik's Cube Solver. 

# Headless implementation
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
# GUI
Run ```python3 new_disp.py```. The default state of the given Rubik's Cube is solved. 

You can manually update the state by clicking the colored button on the bottom left, and then clicking the Rubik Cube. Alternatively, you can use the "Get Cube State" button to use your webcam to get the Rubik Cube state. If you manually scrambled the cube and know the moves you made, then you can input a scramble using the standard Rubik Cube notation described [here]([url](https://ruwix.com/the-rubiks-cube/notation/)). 

Press the solve button to get an algorithm that solves the cube using the method described in the <a href='https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/'>Ruwix</a> website. 

NOTE: Your operating system may indicate that your webcam is being used as soon as you start the program. Rest assured the webcam is not storing any information, and you can even cover your webcam without affecting functionality (obviously excluding the ability to use the webcam to get the cube state)

Refer to below screenshot for a visual reference of the buttons mentioned above:
<img width="1438" alt="image" src="https://github.com/TSinha2/Rubik-Cube-Solver/assets/90647555/4cd487e2-3fba-4a27-8045-4e45d0659208">


TODO: 
- Make sure that new_disp.py doesn't automatically turn on webcam when started.
- Add requirements.txt
- Add a Kociemba solver to make an optimal solver (using minimal words)
- Make sure that redundant moves (e.g. U U') are removed from the human solution. 


