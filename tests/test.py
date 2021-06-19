import unittest
import itertools
from heapx import HeapX, Element


class TestHeapX(unittest.TestCase):
    def test_list_int(self):
        """
        Test the algorithm on all the permutations of the provided sample data.
        """
        with open("data/sample") as sample, open("data/sample_solution_3") as solution:
            solution = list(map(lambda entry: entry.strip(), solution))
            for permutation in itertools.permutations(sample):
                result = HeapX.parse(3, permutation, Element).heap
                self.assertEqual(set(result), set(solution))


if __name__ == '__main__':
    unittest.main()
