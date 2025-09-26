class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            # Sort the string to find its anagram group
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())
# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))