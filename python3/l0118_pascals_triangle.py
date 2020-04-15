from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if i == 0 or j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1]+triangle[i-1][j])
            triangle.append(row)
        return triangle