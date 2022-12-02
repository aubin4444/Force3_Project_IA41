# Correspondence between the identifier of the tiles and their coordinates x and y
correlation = {"1": [0, 0], "2": [1, 0],
               "3": [2, 0], "4": [0, 1],
               "5": [1, 1], "6": [2, 1],
               "7": [0, 2], "8": [1, 2],
               "9": [2, 2]}

# Line of the playing area allowing to deduce the segond square token when 2 square token moves
ga_line = [[1, 4, 7],
           [1, 2, 3],
           [3, 6, 9],
           [9, 8, 7],
           [4, 5, 6],
           [2, 5, 8]]
