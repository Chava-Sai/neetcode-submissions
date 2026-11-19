class Solution:
    def trap(self, height: List[int]) -> int:

        def prefix(index):

            prefix_arr = []

            for i in range(0,index):

                prefix_arr.append(height[i])

            return max(prefix_arr) or 0

        def suffix(index):

            suffix_arr = []

            for i in range(index,len(height)-1):

                suffix_arr.append(height[i])

            return max(suffix_arr) or 0

        total = 0

        for i in range(1,len(height)-1):

            x =  min(prefix(i),suffix(i)) - height[i]
            if x > 0 :
                total += x
            print(total)

        return total


        