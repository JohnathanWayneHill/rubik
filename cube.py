"""
~ TODO: Refactor and clean-up!!!!! 
~ TODO: Need to sanity check edge. 
~ TODO: Write TEST cases. 
~ TODO: Write SCRAMBLE method. 
~ TODO: Raise erro in rotate_face if unacceptable "target" given
"""

<<<<<<< HEAD


import numpy as np

=======
>>>>>>> parent of 8b6d9dd (added documentation to cube class)
class Cube: 
    def __init__(self): 
        
        self.row = 0
        self.col = 1
        
        # todo: list of tuples? 
        self.edge = { "R": 
                            {"B": (self.col, 0), "D": (self.col, 2), 
                             "F": (self.col, 2), "U": (self.col, 2),
                             "order": ['B', 'D', 'F', 'U']},    
                     "L": 
                            {"F": (self.col, 0), "D": (self.col, 0), 
                             "B": (self.col, 2), "U": (self.col, 0),
                             "order": ['F', 'D', 'B', 'U']},    
                     "U": 
                            {"R": (self.row, 0), "F": (self.row, 0), 
                             "L": (self.row, 0), "B": (self.row, 0),
                             "order": ['R', 'F', 'L', 'B']},   
                     "D": 
                            {"R": (self.row, 2), "B": (self.row, 2), 
                             "L": (self.row, 2), "F": (self.row, 2),
                             "order": ['R', 'B', 'L', 'F']},  
                     "F":
                            {"R": (self.col, 0), "D": (self.row, 0),
                              "L": (self.col, 2), "U": (self.row, 2),
                             "order": ['R', 'D', 'L', 'U']},     
                     "B": 
                            {"L": (self.col, 0), "D": (self.row, 2), 
                              "R": (self.col, 2), "U": (self.row, 0),
                             "order": ['L', 'D', 'R', 'U']}
                      }
        
        # list of all faces 
        self.faces = list(self.edge.keys()) # does this need to be self? 
        
        # array representation of Rubic's Cube
        self.cube = {face:np.full((3,3),index) for index, face in enumerate(self.faces)}

                
    def extract_edge(self, target, touching_edges, assignrow, assigncol):
        
        for index, face in enumerate(self.edge[target]["order"]):
            axis = self.edge[target][face][0]
            touching = self.edge[target].keys()
            
            if face in touching and axis == self.row:
                    row_num = self.edge[target][face][1]
                    exec(assignrow)
                    
            elif face in touching: 
                    col_num = self.edge[target][face][1]
                    exec(assigncol)
                    
        return touching_edges
    
    def rotate_face(self, target):
        # placeholder for values in edges touching target face
        touching_edges_placeholder = np.full((4,3),0)
        # updating array for values in edges touching target face
        touching_edges = self.extract_edge(target, touching_edges_placeholder,
                    "touching_edges[index] = self.cube[face][row_num]", 
                    "touching_edges[index] = self.cube[face][:,col_num]")
        
        # roll (rotate) edges in temporary array
        touching_edges_rotated = np.roll(touching_edges, 3)
        # update temporary (rotated) array for edges touching target face
        self.extract_edge(target, touching_edges_rotated,
                    "self.cube[face][row_num] = touching_edges[index]", 
                    "self.cube[face][:,col_num] = touching_edges[index]")
        
        # rotate target face, clockwise (-1 for clockwise, counterclock is default)
        np.rot90(self.cube.cube[target],-1)
        
        
        

if __name__ == "__main__": 
    cube = Cube()



