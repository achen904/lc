class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we can improve the previous approach even more but using
        #a hashmap instead of a hashset. in the previous apporach
        #we would use a while loop to increment our left side, 
        #however, if we use a hash map we can instantly jump to the 
        #last location of our repeated string
        location = {}
        l, r = 0 , 0
        ans = 0
        for r in range(len(s)):
            if s[r] in location and location[s[r]] >= l:
                l = location[s[r]] + 1
            location[s[r]] = r
            ans = max(ans, r - l + 1)
        return ans