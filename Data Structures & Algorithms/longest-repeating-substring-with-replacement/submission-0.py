class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxf = max(maxf, count[s[r]]) # count the maximum frequency 

            while (r-l+1)-maxf >k: # within the given window, if we subtract the max freq and still have more than K elements left
                count[s[l]] -=1 #remove the charater from count to match k
                l +=1 # reduce the size of the window by 1 
            res = max(res, r-l+1) # finds the maximum and return 
        return res
        