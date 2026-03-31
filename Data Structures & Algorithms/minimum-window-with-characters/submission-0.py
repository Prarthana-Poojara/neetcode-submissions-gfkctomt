class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""

        countT, window = {},{}
        for c in t:
            countT[c] = 1+ countT.get(c,0)

        have, need = 0, len(countT)
        res, resLen = [-1,-1], float('infinity')
        l =0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -=1 #shrink the window from the left
                if s[l] in countT and window[s[l]]< countT[s[l]]: # if by shrinking we have removed an important character
                    have -=1 #decrement the count by 1
                l+=1 # shift the left pointer 
        l,r = res
        return s[l:r+1] if resLen !=float('infinity') else ""
        

        

        