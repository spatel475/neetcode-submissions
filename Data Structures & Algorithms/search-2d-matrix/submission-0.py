class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search the row that should contain the target, then do search columns of that row
        """

        maxRow, maxCol = len(matrix) - 1, len(matrix[0]) - 1

        leftCol, rightCol = 0, maxCol
        topRow, bottomRow = 0, maxRow

        while leftCol <= rightCol and topRow <= bottomRow:
            midRow = (bottomRow + topRow) // 2
            midCol = (rightCol + leftCol) // 2
            matrixMid = matrix[midRow][midCol]

            if matrixMid == target:
                return True

            if matrix[midRow][0] <= target <= matrix[midRow][maxCol]:
                # target in this row, update columns only
                if target <= matrixMid:
                    rightCol = midCol - 1
                else:
                    leftCol = midCol + 1
            elif target <= matrix[midRow][0]:
                # target in above row
                bottomRow = midRow - 1
            elif target > matrix[midRow][maxCol]:
                # target in below row
                topRow = midRow + 1
            else:
                return False

        return False
