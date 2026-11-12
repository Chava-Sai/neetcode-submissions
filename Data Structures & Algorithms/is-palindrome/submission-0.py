class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower().split()
        combined = "".join(new_s)
        i = 0
        j = len(combined)-1
        Answer = True

        while i < j:
            if combined[i].isalnum() and combined[j].isalnum():
                if combined[i] == combined[j]:
                    print(combined[i])
                    print(combined[j])
                    i +=1
                    j -= 1
                    continue
                else :
                    return False
            elif combined[i].isalnum() == False:
                print(combined[i])
                print(combined[j])
                i += 1
            else:
                print(combined[i])
                print(combined[j])
                j -= 1
               
        return Answer

        
        