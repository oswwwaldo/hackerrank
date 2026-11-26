class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        can_plant: int = 0
        if can_plant == n: return True
        for i in range(len(flowerbed)):
            prev_item = flowerbed[i - 1] if i > 0 else None
            current_item = flowerbed[i]
            next_item = flowerbed[i + 1] if i + 1 < len(flowerbed) else None

            con_1: bool = (current_item == 0)
            con_2: bool = (prev_item == 0 or prev_item is None)
            con_3: bool = (next_item == 0 or next_item is None)
            required_conditions: bool = (con_1 and con_2 and con_3)

            if (required_conditions):
                flowerbed[i] = 1
                can_plant += 1
                if can_plant == n: return True
        return can_plant == n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna