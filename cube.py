import numpy as np

import random
import time


"""
2-D representation of a rubik's cube using numpy 
"""


class Cube:
    """
    A class used to represent an Rubik's Cube 
       TODO: more here 

    ...

    Attributes
    ----------
    row : int
        TODO: more here


    Methods
    -------
    extract_edge: 
        TODO: more here
    """

    def __init__(self):
        # codings for rows and columns
        self.row = 0  # THIS COULD BE A PRIVATE CLASS ATTRIBUTE
        self.col = 1  # THIS COULD BE A PRIVATE CLASS ATTRIBUTE

        # todo: list of tuples?
        # TODO: double-check that order is correct as well as (axis,index) pairs
        # THIS COULD BE A PRIVATE CLASS ATTRIBUTE
        self.edge = {"R":  # target face
                     {"B": (self.col, 0), "D": (self.col, 2),  # touching edges
                      "F": (self.col, 2), "U": (self.col, 2),  # touching edges
                      "order": ['B', 'D', 'F', 'U']},         # order of operations to perform
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

        # list of all faces - PUBLIC ?
        self.faces = list(self.edge.keys())  # does this need to be self?

        # array representation of Rubik's Cube # MAKE PRIVATE!!!!!!
        self.cube = {face: np.full((3, 3), index)
                     for index, face in enumerate(self.faces)}

        # ANSI escape sequences for color-coding
        self.color_dict = {'0': '\033[31m{}\033[0m', '1': '\033[95m{}\033[0m',  # target: color_scheme {symbol} reset_color_scheme
                           '2': '\033[34m{}\033[0m', '3': '\033[32m{}\033[0m',
                           '4': '\033[93m{}\033[0m', '5': '\033[96m{}\033[0m'}

        self.moves = []  # moves that have been performed
        print(self)

    # TODO: THINK ABOUT THOS ASSIGNROWs AND ASSIGNCOLs for exec()
    """ 
    MAKE THIS A PRIVATE METHOD 
    """

    def extract_edge(self, target: str, touching_edges: "np.array((4,3))",
                     assignrow: str, assigncol: str) -> "np.array((4,3))":
        """ Extracts rows and/or columns touching edge of target face 

        Parameters
        ----------
        target : str
            The target face we are intending to rotate.
        touching_edges : np.array((4,3),...)
            Numpy array that we are either updating or using to update. 
        assignrow: str
            String that will be evaluated as code using exec to assign from
                one array to another.
        assigncol: str
            String that will be evaluated as code using exec to assign from
                one array to another.

        Returns
        -------
        numpy
            a list of strings used that are the header columns
        """

        # iterate through order of rows
        for index, face in enumerate(self.edge[target]["order"]):
            axis = self.edge[target][face][0]  # 0 for row, 1 for col
            touching = self.edge[target].keys()  # list of touching edges

            # if current face touching target face and row touching
            if face in touching and axis == self.row:
                # row number of target edge to extract
                row_num = self.edge[target][face][1]
                exec(assignrow)  # assigned row

            # if current face touching target and col touching
            elif face in touching:
                # col number of target edge to extract
                col_num = self.edge[target][face][1]
                exec(assigncol)  # assigned column

        return touching_edges

    """
    TODO:
    ENABLE MULTIPLE TARGET ROTATIONS TO BE PERFORMED
    """

    def rotate(self, target: str) -> None:
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        target : str
            The target face we are intending to rotate.

        """
        all_faces = self.faces.copy()  # repeated in shuffle
        all_faces += [i + "*" for i in all_faces]  # repeated in shuffle
        if target in all_faces:
            # os.system('clear')
            time.sleep(0.25)
            print(target)
            self.moves.append(target)
            counter_clock = False
            if "*" in target:
                counter_clock = True
                target = target[0]
            # placeholder for values in edges touching target face
            touching_edges_placeholder = np.full((4, 3), 0)

            # updating array for values in edges touching target face
            touching_edges = self.extract_edge(target,  # target face
                                               touching_edges_placeholder,  # array of edges to re-assign
                                               # assignment operations
                                               # NOT DOCUMENTED WELL-ENOUGH
                                               "touching_edges[index] = self.cube[face][row_num]",
                                               "touching_edges[index] = self.cube[face][:,col_num]")  # NOT DOCUMENTED WELL-ENOUGH

            # roll (rotate) edges in temporary array
            if counter_clock == False:
                touching_edges_rotated = np.roll(touching_edges, 3)
                touching_edges_rotated[1] = touching_edges_rotated[1][::-1]
                touching_edges_rotated[3] = touching_edges_rotated[3][::-1]
            else:
                touching_edges_rotated = np.roll(touching_edges, -3)
                touching_edges_rotated[0] = touching_edges_rotated[0][::-1]
                touching_edges_rotated[2] = touching_edges_rotated[2][::-1]

            # update temporary (rotated) array for edges touching target face
            self.extract_edge(target,  # target face
                              touching_edges_rotated,  # array of edges to re-assign
                              # assignment operations
                              # NOT DOCUMENTED WELL-ENOUGH
                              "self.cube[face][row_num] = touching_edges[index]",
                              "self.cube[face][:,col_num] = touching_edges[index]")  # NOT DOCUMENTED WELL-ENOUGH

            # rotate target face, clockwise (-1 for clockwise, counterclock is default)
            if counter_clock == False:
                self.cube[target] = np.rot90(self.cube[target], -1)
            else:
                self.cube[target] = np.rot90(self.cube[target])
            print(self)
        else:
            # better way to handle this problem? ->>>>> used for when UNRECOGNIZABLE ERROR GIVEN
            raise Exception("BAD!")

    def __str__(self) -> None:
        """ 
        TODO:  refactor for human-readability 
        """
        # format first 3 rows
        U = "".join(str(self.cube['U'][i]).rjust(
            15) + '\n' for i in range(3)) + '\n'

        # format second 3 rows
        M = "".join((lambda row: "".join(str(self.cube[face][row]) + " " for face in
                    ['L', 'F', 'R', 'B']))(i) + '\n' for i in range(3)) + '\n'

        # format third 3 rows
        D = "".join(str(self.cube['D'][i]).rjust(15) + '\n' for i in range(3))

        # combine into one string
        num_string = U + M + D

        # TODO: refactor & clean up
        """
        TODO: CLEAN UP
        """
        string = ""
        for i, char in enumerate(num_string):
            if char in self.color_dict and i == 27:
                string += self.color_dict[char].format('U')
            elif char in self.color_dict and i == 85:
                string += self.color_dict[char].format('L')
            elif char in self.color_dict and i == 93:
                string += self.color_dict[char].format('F')
            elif char in self.color_dict and i == 101:
                string += self.color_dict[char].format('R')
            elif char in self.color_dict and i == 109:
                string += self.color_dict[char].format('B')
            elif char in self.color_dict and i == 176:
                string += self.color_dict[char].format('D')
            elif char in self.color_dict:
                string += self.color_dict[char].format("■")
            elif char == "[" or char == "]":
                string += " "
            else:
                string += char

        return "\n" + string

    # PROBABLY THE BEST WAY TO DO THIS --> OPTIMIZE FOR SPEED
    def scramble(self, scrambles: "int number of scrambles to perform ") -> None:
        shuf = self.faces.copy()  # repeated
        # repeated; create new list including counter-clockwise operations
        shuf += [i + "*" for i in shuf]
        for i in range(scrambles):
            face = random.sample(shuf, 1)[0]  # randomly select one face
            self.rotate(face)  # rotate face

    def solve(self) -> None:  # TODO: CREATE OTHER SOLVE METHODS
        for i in range(len(self.moves) - 1, -1, -1):
            if "*" in self.moves[i]:
                move_back = self.moves[i][0]
            else:
                move_back = self.moves[i] + "*"
            self.rotate(move_back)
        self.moves = []


if __name__ == "__main__":
    cube = Cube()
