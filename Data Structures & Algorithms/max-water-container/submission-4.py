class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        vol = 0

        max_vol = (j - i) * min(heights[i],heights[j])

        while i < j:

            if heights[i] >= heights[i-1]:
                max_vol = max((j - i) * min(heights[i],heights[j]),max_vol)
                i += 1
            else:
                i+=1
            if heights[j-1] < heights[j]:
                max_vol = max((j - i) * min(heights[i],heights[j]),max_vol)
                j -= 1
            else:
                j -= 1

        return max_vol

        