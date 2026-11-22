class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest: str = max(word1, word2, key=len)
        output: str = ""

        for index, letter in enumerate(longest):

            try: 
                output = output + word1[index] + word2[index]
            except IndexError:
                output = output + longest[index]
        
        return output

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna