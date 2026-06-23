class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose then reverse the rows
        #[1,2,3] [1,4,7]
        #[4,5,6] [2,5,8] 
        #[7,8,9] [3,6,9]
        #transpose first
        for row in range(len(matrix)):
            for column in range(row, len(matrix)):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
        #reverse row
        for row in range(len(matrix)):
            matrix[row] = reversed(matrix[row])
        
