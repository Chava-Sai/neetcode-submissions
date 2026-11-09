class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:

            count = [0] * 26

            for char in word:

                count[ord(char) - ord('a')] += 1

            signature = tuple(count)

            if signature in anagrams:

                anagrams[signature].append(word)

            else:

                anagrams[signature] = [word]

        return list(anagrams.values())
        


        