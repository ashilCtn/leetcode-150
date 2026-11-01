class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        for row in matrix:
            if target <= row[-1]:
                l = 0
                h = len(row) - 1
                while l <= h:
                    m = ( l + h ) // 2
                    if target < row[m]:
                        h = m - 1
                    elif target > row[m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False
        