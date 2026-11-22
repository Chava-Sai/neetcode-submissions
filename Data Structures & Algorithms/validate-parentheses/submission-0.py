class Solution:
    def isValid(self, s: str) -> bool:
        final = []
        for item in s:
            if item == "(" or item == "[" or item == "{":
                final.append(item)
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
        return True
            

        