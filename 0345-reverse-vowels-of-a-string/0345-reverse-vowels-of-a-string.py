class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels: str = 'aeiouAEIOU'
        word: str = s
        reversed_text: str = ""

        vowels_found: list[str] = "".join(filter(lambda char: char in vowels, word))
        reversed_vowels: list[str] = vowels_found[::-1]
        vowel_index: int = 0

        for letter in word:
            if letter in vowels:
                reversed_text += reversed_vowels[vowel_index]
                vowel_index += 1
            else: 
                reversed_text += letter
        return reversed_text

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna