from typing import List
from unittest import TestCase

from leetcode.rotate_image import Solution


class TestSolution(TestCase):

    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.rotate(matrix)

        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_example2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

        self.rotate(matrix)

        self.assertEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    def test_one(self):
        matrix = [[1]]

        self.rotate(matrix)

        self.assertEqual(matrix, [[1]])

    def rotate(self, matrix: List[List[int]]) -> None:
        sol = Solution()
        sol.rotate(matrix)
