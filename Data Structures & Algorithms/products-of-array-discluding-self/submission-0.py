class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        prefix = []
        suffix = []
        product = 1
        for i in range(len(nums)):
            prefix.append(product)
            product = product * nums[i]
        product = 1
        for i in range(-1, -len(nums) - 1, -1):
            suffix.append(product)
            product = product * nums[i]

        suffix_ord = suffix[::-1]
            
        for i in range(len(nums)):
            final.append(prefix[i]*suffix_ord[i])

        return final


        