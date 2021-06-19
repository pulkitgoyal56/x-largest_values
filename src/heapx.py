#!/usr/bin/env python3
# %%

import sys
import heapq

# > LEGEND
# <TC> - Time Complexity
# <SC> - Space Complexity


class HeapX():
    def __init__(self, X):
        self._X = int(X)
        self._heap = []  # <SC> O(X)

    def insert(self, element):
        """
        Inserts a new element in the heap
        - If the heap is already full, pops the HEAD (the smallest value)
        """
        if len(self._heap) == self._X:  # <TC> O(1), N times | O(N)
            # `heapq.heappushpop()` - Push item on the heap, then pop and return the smallest item from the heap
            heapq.heappushpop(self._heap, element)
            # <TC> O(log(X)), N-X times | O((N-X).log(X))
        else:
            # # > [METHOD 1] Maintaining a heap from the beginning -- slightly better for smaller values of X
            # heapq.heappush(self._heap, element)
            # # <TC> O(log(k)), X times = Θ(Σlog(k)), k ∈ [0, X) === Θ(log(X!)) | O(X.log(X))
            # # <TC> TOTAL = Θ(X.log(X) + (N-X).log(X) + 3.N)
            #              ~ O(N.log(X))
            # # <SC> TOTAL = O(X)

            # > [METHOD 2] Converting to heap only after the first X elements are parsed -- when X is large
            self._heap.append(element)  # <TC> O(1), X times | O(X)
            # Heapify the list once it reaches max size, X
            if len(self._heap) == self._X:  # <TC> O(1), X times | O(X)
                heapq.heapify(self._heap)  # <TC> O(X), once | O(X)
            # <TC> TOTAL = Θ(3.X + (N-X).log(X) + 3.N)
            #            ~ O((N-X).log(X)) --------------- FINAL ANSWER
            # <SC> TOTAL = O(X) -------------------------- FINAL ANSWER

    @property
    def heap(self):
        """
        Returns an iterable of the corresponding UUIDs of the elements in the heap
        """
        return map(str, self._heap)

    @staticmethod
    def parse(X, data, Type):  # N - Data size
        """
        Parses the data stream and returns a heap

        ARGUMENTS
        1. X - Number of elements to be found
        2. data - Input data
        3. Type - Input data entry type
        """
        heapX = HeapX(X)  # Initialize priority queue of size X using min heap

        for entry in data:  # <TC> O(1), N times | O(N)
            if not entry.isspace():  # Check if the entry is a whitespace | <TC> O(1), N times | O(N)
                heapX.insert(Type(entry))

        return heapX


class Element:
    """
    A data capsule for the entries

    PROPERTIES
    1. uri - <unique record identifier>
    2. value - <numeric value>

    MAGIC METHODS
    1. `__lt__`  - The `heapq` module uses the less than ('<') method for sorting and comparisons
    2. `__str__` - Returns the UUID of the element, for printing
    """

    def __init__(self, entry):
        self.uri, value = entry.split()
        self.value = int(value)

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return self.uri


if __name__ == '__main__':
    if (len(sys.argv) < 2):  # If no argument is passed
        raise Exception("Error: 'X' not provided")
    elif (len(sys.argv) == 2):  # If only one argument is passed
        # Read input from 'stdin'
        pqX = HeapX.parse(sys.argv[1], sys.stdin, Element)
    elif (len(sys.argv) == 3):  # If two arguments are passed
        # Read file from name provided in the arguments
        with open(sys.argv[2]) as file:
            pqX = HeapX.parse(sys.argv[1], file, Element)
    else:  # If three or more arguments are passed
        raise Exception("Error: Too many arguments provided")

    # Print the priority queue
    print(*pqX.heap, sep='\n')
