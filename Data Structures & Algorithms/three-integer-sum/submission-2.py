class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # k = len(nums)-1
        # seen = set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             seen.add((nums[i],nums[j],nums[k]))
        # sorted_final = {tuple(sorted(t)) for t in seen if sum(t)==0}
        # final_list = []
        # for item in sorted_final:
        #     final_list.append(list(item))
        # return final_list

        sort = sorted(nums)
        res = []
        n = len(nums)

        for i in range(n-2):

            if sort[i] > 0 :

                break

            if i > 0 and sort[i] == sort[i-1]:

                continue

            j = i + 1
            k = n - 1

            while j < k :

                total = sort[i] + sort[j] + sort[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([sort[i],sort[j],sort[k]])
                    j += 1
                    k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        return res

        