class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix: str = ""
        first_word: str = strs[0]
        words: List[str] = strs

        for index, char in enumerate(first_word):
            if all(word.startswith(common_prefix + char) for word in words):
                common_prefix = common_prefix + char
            else:
                return common_prefix
        return common_prefix

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna