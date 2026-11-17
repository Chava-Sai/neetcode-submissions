class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        max_vol = (j - i) * min(heights[i],heights[j])

        while i < j:

            if heights[i+1] >= heights[i]:
                i += 1
                vol = (j - i) * min(heights[i],heights[j])
            elif heights[j-1] >= heights[j]:
                j -= 1
                vol = (j - i) * min(heights[i],heights[j])
            else:
                i += 1
                j -= 1

            if vol > max_vol:
                max_vol = vol

        return max_vol

        