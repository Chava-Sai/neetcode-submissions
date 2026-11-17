class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        vol = 0

        max_vol = (j - i) * min(heights[i],heights[j])

        while i < j:

            if heights[i+1] >= heights[i]:
                i += 1
                max_vol = max((j - i) * min(heights[i],heights[j]),max_vol)
            elif heights[j-1] >= heights[j]:
                j -= 1
                max_vol = max((j - i) * min(heights[i],heights[j]),max_vol)
            else:
                i += 1
                j -= 1

        return max_vol

        