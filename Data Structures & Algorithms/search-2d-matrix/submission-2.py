class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r)//2
            row = m // (len(matrix[0]))
            col = m % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        return False