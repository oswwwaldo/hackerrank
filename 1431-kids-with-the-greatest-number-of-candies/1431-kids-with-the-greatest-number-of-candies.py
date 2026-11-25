class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        truth_lst: list[bool] = []

        for index, candy in enumerate(candies): 
            if candy + extraCandies >= max(candies):
                truth_lst.append(True)
            else:
                truth_lst.append(False)
        
        return truth_lst


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna