class Solution:
    def isValid(self, s: str) -> bool:

        otc = {"(":")", "[":"]", "{":"}"}

        stack = []

        for i in range(len(s)):
            if s[i] in  otc.keys(): # ( [ {
                stack.append(s[i])

            else:
                if stack == []:
                    return False
                top = stack.pop() # ( same opener
                if otc[top] != s[i]:
                    return False
        
        if stack == []:
            return True
        return False
    