class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # We will be using a O(n^2) time and O(1) space complexity
        
        left, right = 0, len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                #Move the topleft in temporary var
                topLeft = matrix[top][left + i]
                #move bottom left to topleft
                matrix[top][left + i] = matrix[bottom - i][left]
                #Move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                #Move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                #Move topLeft to top right
                matrix[top + i][right] = topLeft
            right -= 1
            left += 1
        
                