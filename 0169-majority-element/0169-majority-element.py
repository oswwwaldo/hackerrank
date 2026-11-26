

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        results: dict[int, int] = {}
        unique_nums: set[int] = set(nums)
        for n in unique_nums:
            results[n] = nums.count(n)
        majority: int = max(results, key=results.get)
        return majority        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna