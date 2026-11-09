class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        available = [True] * len(strs)
        for i in range(len(strs)):
            if not available[i]:
                continue
            middle = []
            seen = {}
            middle.append(strs[i])
            for k in range(len(strs[i])):
                char = strs[i][k]
                if char in seen:
                    seen[char] += 1
                else:
                    seen[char] = 1
            for j in range(i+1,len(strs)):
                seen2 = seen.copy()
                if len(strs[i]) != len(strs[j]):
                        continue
                else:
                    for p in range(len(strs[j])):
                        second_char = strs[j][p]
                        if second_char in seen:
                            seen2[second_char] -= 1
                        else:
                            seen2[second_char] = 1
                            break
                if all(value == 0 for value in seen2.values()):
                    middle.append(strs[j])
                    available[j] = False
            final.append(middle)
        return final
        


        