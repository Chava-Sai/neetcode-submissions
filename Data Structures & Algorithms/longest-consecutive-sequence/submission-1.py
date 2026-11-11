class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_list = sorted(nums)
        new_set = set(sorted(nums))
        seen = {}
        for num in new_set :
            if len(seen) == 0:
                x = num
                y = num
                seen[num] = []
            if num == y + 1:
                seen[x].append(num)
                y = num
            else:
                seen[num] = []

        max_length = max((len(v) for v in seen.values()), default=0)
        
        return max_length+1
            




        