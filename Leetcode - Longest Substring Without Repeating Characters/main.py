class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1:
            return len(s)
        longeststr=0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if len(set(s[i:j])) != len(s[i:j]):
                    continue
                if len(s[i:j]) > longeststr:
                    longeststr = len(s[i:j])
        return longeststr
