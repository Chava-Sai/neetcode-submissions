class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            seen = dict()
            for i in range(len(s)):
                if s[i] in seen:
                    seen[s[i]] += 1
                else:
                    seen[s[i]] = 1
            for i in range(len(t)):
                if t[i] in seen:
                    seen[t[i]] -= 1
                else:
                    return False
            print(seen)
            if sum(val for val in seen.values() if val > -1 ) == 0:
                return True
            else:
                return False
        

        