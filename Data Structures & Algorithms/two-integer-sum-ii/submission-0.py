class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for num in numbers:
            need = target - num
            if need in seen :
                return [need,num]
            else:
                seen.add(num)
        