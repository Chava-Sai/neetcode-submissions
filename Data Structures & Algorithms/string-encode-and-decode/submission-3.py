class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for item in strs:
            final += f"{len(item)}#{item}"
        return final

    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i])

            start_word = j+1
            end_word = start_word + length

            words.append(s[start_word:end_word])

            i = end_word
        return words





        

                

            
