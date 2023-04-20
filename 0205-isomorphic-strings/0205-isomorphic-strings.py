class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        
        for c1, c2 in zip(s,t):
            if (c1 not in countS) and (c2 not in countT):
                countS[c1] = c2
                countT[c2] = c1
            
            elif countS.get(c1) != c2 or countT.get(c2) != c1:
                return False
                
        return True