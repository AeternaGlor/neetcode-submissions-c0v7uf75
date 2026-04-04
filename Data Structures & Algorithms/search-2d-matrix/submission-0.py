class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = None
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                # row_idx = m # тут не выпллнится при len(matrix) = 1
                break
        
        row_idx = m

        l, r = 0, len(matrix[row_idx]) - 1
        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if target < matrix[row_idx][m]:
                r = m - 1
            elif target > matrix[row_idx][m]:
                l = m + 1
            else:
                return True
        return False
