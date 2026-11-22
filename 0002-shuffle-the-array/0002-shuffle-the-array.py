class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n] 
        second_half = nums[n:]
        output: list[int] = []

        for i in range(len(first_half)):
            output.append(first_half[i])
            output.append(second_half[i])

        return output


# n = 
# determines how much the list is split into two
# and then we cycle through both sub lists and pair each number of the respective index in pairs


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna