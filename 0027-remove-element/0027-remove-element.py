class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        while val in nums:
            nums.remove(val)

        return len(nums)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna