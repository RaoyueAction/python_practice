class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        left = 0
        right = 0
        char_set = set()
        max_length = 0
        while right < n:
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                char_set.remove(s[left])
                left += 1
        return max_length
#example
s = "abcabcbb"
solution = Solution() 
print(solution.lengthOfLongestSubstring(s))  # Output: 3