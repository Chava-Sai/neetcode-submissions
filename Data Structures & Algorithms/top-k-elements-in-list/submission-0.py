class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        final = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        for i in range(k):
            final_key = max(seen,key = seen.get)
            final.append(final_key)
            seen.pop(final_key)
        return final