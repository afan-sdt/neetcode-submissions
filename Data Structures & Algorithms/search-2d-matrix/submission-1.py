class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n)-1
        while l <= r:
            middle = (l+r)//2
            print(middle, l, r)
            print(middle//n)
            print(middle%n)
            print(matrix[middle//n][middle%n])
            if matrix[middle//n][middle%n] < target:
                l=middle+1
            elif matrix[middle//n][middle%n] > target:
                r = middle-1
            else:
                return True
        return False


