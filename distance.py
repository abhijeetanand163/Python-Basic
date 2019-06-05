
import numpy as np

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class distance():
    """
    
    This class contains three different function.
        1. Rooks Distance
        2. Pandemic Distance
        3. Levenshtein Distance
        
    """
    # 1. Rooks Distance , otherwise also called Manhattan Distance
    
    def ManhattanDistance(point1, point2):
        """
        The Manhattan distance, also known as rectilinear distance, city block distance, taxicab metric is defined as the sum of the lengths of the projections of
        the line segment between the points onto the coordinate axes. 

        In chess, the distance between squares on the chessboard for rooks is measured in Manhattan distance.

        It is given by |x1 - x2| + |y1 - y2|

        # for example I am putting it in the form of dictionary. 

        Note : Please input the data in the following dictionary format. 
            
            Check "Class point" for more detials.

        >>> point1 = point(2,3)
        >>> point2 = point(5,1)

        >>> ManhattanDistance(point1, point2)
            5

        """

        x1 = point1.x
        x2 = point2.x
        y1 = point1.y
        y2 = point2.y

        manhattandistance = np.abs(x1 - x2) + np.abs(y1 - y2)

        return manhattandistance
    
    # 2. Pandemic Distance 
    
    
    
    
    # 3. Levenshtein Distance 
    
    def LevenshteinDistance(a, b):
        """
        This function takes two string as input and return Levenshtein distance between them. 



        For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other, and there is no way to
        do it with fewer than three edits:

            kitten → sitten (substitution of "s" for "k")
            sitten → sittin (substitution of "i" for "e")
            sittin → sitting (insertion of "g" at the end).

        >>> LevenshteinDistance('cat','bat')
            1


        Since we only need to replace 'c' of cat to 'b' of bat

        Note: a and b are string so put it under a double bracket or single bracket. 
        """

        initial_cost = 0
        total_cost = 0
        if (len(a) != len(b)):
            initial_cost = np.abs(len(a) - len(b))
        else: 
            initial_cost = 0

        if (len(a) <= len(b)):
            for i in range(len(a)):
                if (a[i] != b[i]):
                    total_cost += 1
                else:
                    pass
        else:
            for i in range(len(b)):
                if (b[i] != a[i]):
                    total_cost += 1
                else:
                    pass

        return initial_cost + total_cost
    
    