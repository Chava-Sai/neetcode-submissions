class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        new_list = sorted(nums)
        seen = {}
        for num in new_list :
            if len(seen) == 0:
                x = num
                y = num
                seen[num] = []
            if any(num in v for v in seen.values()):
                continue
            elif num == y + 1:
                seen[x].append(num)
                y = num
            else:
                seen[num] = []
                x = num
                y = num

        max_length = max((len(v) for v in seen.values()),default = 0)

        print(seen)
        
        return max_length + 1
            




        