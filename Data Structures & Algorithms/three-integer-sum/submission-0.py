class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)-1
        seen = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    seen.add((nums[i],nums[j],nums[k]))
        sorted_final = {tuple(sorted(t)) for t in seen if sum(t)==0}
        final_list = []
        for item in sorted_final:
            final_list.append(list(item))
        return final_list


        