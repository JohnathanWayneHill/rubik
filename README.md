# 2-D representation of a Rubik's cube 

Used for demonstrating numpy to students. 
In progress. 

To use: 

1) `python -i cube.py` 

2) `cube.rotate('F')` to rotate face 'F' clockwise: 
- 'F' for front face
- 'B' for back face
- 'U' for "up" face
- 'D' for "down" face
- 'L' for left face
- 'R' for right face 

3) `cube.rotate('F*')` to rotate 'F' counterclockwise. 

4) `cube.solve()` to undo all rotations. 

5) `cube.scramble(5)` rotate 5 random faces in random directions. 
