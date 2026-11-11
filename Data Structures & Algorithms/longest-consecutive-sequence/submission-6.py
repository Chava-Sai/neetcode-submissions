class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for item in nums_set:

            if item - 1 not in nums_set:

                current_item = item
                current_length = 1

                while current_item + 1 in nums_set:

                    current_item += 1
                    current_length += 1

                longest = max(current_length,longest)
        return longest
            




        