import numpy as np

row = 0
col = 1
touching = {"R": {"B": (col, 0), "D": (col, 2), "F": (col, 2), "U": (col, 2)},
            "L": {"F": (col, 0), "D": (col, 0), "B": (col, 2), "U": (col, 0)},
            "U": {"R": (row, 0), "F": (row, 0), "L": (row, 0), "B": (row, 0)},
            "D": {"R": (row, 2), "B": (row, 2), "L": (row, 2), "F": (row, 2)},
            "F": {"R": (col, 0), "D": (row, 0), "L": (col, 2), "U": (row, 2)},
            "B": {"L": (col, 0), "D": (row, 2), "R": (col, 2), "U": (row, 0)}
            }

faces = ["U", "D", "F", "B", "L", "R"]

cube = {face:np.full((3,3),index) for index, face in enumerate(faces)}


def extract_array(target):
    array_to_rotate = np.full((4,3),0)
    ind = 0
    ls = []
    for face, squares in cube.items(): 
        if face in touching[target].keys(): 
            if touching[target][face][0] == 0:
                array_to_rotate[ind] = cube[face][[touching[target][face][1]][0]]
                ls.append(face)
                ind +=1
            else: 
                array_to_rotate[ind] = cube[face][:,[touching[target][face][1]][0]]
                ls.append(face)
                ind +=1
    return array_to_rotate, ls

arr = extract_array("B")


def rotate(target):
    array_to_rotate = extract_array(target)[0]
    ls = extract_array(target)[1]
    tmp = np.roll(array_to_rotate, 3)
    
    for ind, face in enumerate(ls): 
        if face in touching[target].keys(): 
            if touching[target][face][0] == 0:
                cube[face][[touching[target][face][1]][0]] = tmp[ind] 
                ind +=1
            else: 
                cube[face][:,[touching[target][face][1]][0]] = tmp[ind] 
                ind +=1

rotate("B")
