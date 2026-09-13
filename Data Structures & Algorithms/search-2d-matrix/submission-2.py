class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #since they're all contiguous we can consider the indices to be 1-m*n
        # to index we just divide by len(matrix[0] and mod by len(matrix[i])
        #
        m = len(matrix)
        n = len(matrix[0])
        l,r = 0, m*n -1

        while l <= r:
            mid = l + (r-l)//2
            rem = mid%n
            div = mid//n
            if matrix[div][rem] == target:
                return True
            elif matrix[div][rem] < target:
                l = mid + 1
            elif matrix[div][rem] > target:
                r = mid - 1
        return False