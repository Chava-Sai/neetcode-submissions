class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        final = []
        for item in s:
            if item == "(" or item == "[" or item == "{":
                final.append(item)
            elif len(final) != 0 :
                if item == ")":
                    if final.pop() == "(":
                        continue
                    else:
                        return False
                if item == "}":
                    if final.pop() == "{":
                        continue
                    else:
                        return False
                if item == "]":
                    if final.pop() == "[":
                        continue
                    else:
                        return False
            else:
                return False
        return True
            

        