# %%
class Solution:
    def noOfEvenNumDigits(self, nums):
        evenCount = 0

        for num in nums:
            digitCount =0

            if num == 0:
                digitCount = 0
            else:
                while num > 0:
                    num = num // 10
                    digitCount += 1

            if digitCount % 2 == 0:
                evenCount += 1
        
        return evenCount
    
# %%
### Test
if __name__ == "__main__":

    solution = Solution()

    # Test cases
    test_cases = [
        [11, 345, 2, 6, 6883],
        [555, 901, 482, 1771],
        [1, 333, 55555],
        [0, 10, 100, 1000],
    ]

    print("Let's test the function with some cases:")

    for i, nums in enumerate(test_cases):
        result = solution.noOfEvenNumDigits(nums)
        print(f"Test case: {i + 1}: {nums}, Result: {result}")
# %%
