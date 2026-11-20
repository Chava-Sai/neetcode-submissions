class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        prefix_arr = [0] * n

        suffix_arr = [0] * n

        if n < 3 :

            return 0

        prefix_arr[0] = height[0]
        for i in range(1,n):
            prefix_arr[i] = max(height[i],prefix_arr[i-1])

        suffix_arr[-1] = height[-1]
        for i in range(n-2,-1,-1):
            suffix_arr[i] = max(height[i],suffix_arr[i+1])

        total = 0

        for i in range(1,n-1):

            total += min(prefix_arr[i],suffix_arr[i]) - height[i]
        
        return total



        