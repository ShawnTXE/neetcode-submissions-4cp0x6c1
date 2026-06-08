class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettersS = {}
        lettersT = {}
        for num in s:
            if num not in lettersS:
                lettersS[num] = 1
            else:
                lettersS[num] += 1
        
        for num in t:
            if num not in lettersT:
                lettersT[num] = 1
            else:
                lettersT[num] += 1
        
        if lettersT == lettersS:
            return True

        return False