class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l =0
        count = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            count = max(count, r-l+1)
        return count

        