class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        mid = 0

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] > target:
                r = mid - 1

            elif matrix[mid][0] < target:
                l = mid + 1

            else:
                break


        if l <= r and l != mid:
            r = mid

        
        elif l <= r:
            r = l
            
        start = 0
        end = len(matrix[r]) - 1

        print(matrix[r])

        while start <= end:
            mid = (start + end) // 2
            if matrix[r][mid] > target:
                end = mid - 1
            
            elif matrix[r][mid] < target:
                start= mid + 1
            
            else:
                return True
        
        return False