class Solution:
    def reverseWords(self, s: str) -> str:
        sentence: str = s.split()   
        reversed_sentence: list[str] = list(reversed(sentence))

        reversed_str: str = ""
        for word in reversed_sentence:
            reversed_str += word + " "
        return reversed_str.strip()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna