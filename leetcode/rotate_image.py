from typing import List


# https://leetcode.com/problems/rotate-image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        while i < len(matrix) / 2:
            j = len(matrix) - 1 - i
            k = 0
            while k < j - i:
                tl = [i, i + k]
                tr = [i + k, j]
                bl = [j - k, i]
                br = [j, j - k]

                tmp = self.get(matrix, tl)
                self.move(matrix, bl, tl)
                self.move(matrix, br, bl)
                self.move(matrix, tr, br)
                self.set(matrix, tr, tmp)

                k += 1

            i += 1

    def move(self, mx: List[List[int]], f: List[int], t: List[int]):
        self.set(mx, t, self.get(mx, f))

    def set(self, mx: List[List[int]], c: List[int], v: int):
        mx[c[0]][c[1]] = v

    def get(self, mx: List[List[int]], c: List[int]):
        return mx[c[0]][c[1]]
