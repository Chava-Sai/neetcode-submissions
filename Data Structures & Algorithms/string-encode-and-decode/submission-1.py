class Solution:

    def encode(self, strs: List[str]) -> str:
        num = len(strs)
        final = f"{num}"
        for item in strs:
            final += "-"+item
        return final

    def decode(self, s: str) -> List[str]:
        words = []
        new = ""
        for i in range(2,len(s)):
            if s[i] == "-":
                if len(new)!=0:
                    words.append(new)
                new = ""
                continue
            else:
                new += s[i]
        words.append(new)
        return words

        

                

            
