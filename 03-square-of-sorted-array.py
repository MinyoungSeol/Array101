# %%
class Solution:
    def sortedSquares(self, nums):
        """
        Return squares of sorted array in non-decreasing order.
        Uses two-pointers approach for O(n) time complexity.
        """

        n = len(nums)
        result = [0] * n  # Create list of n zeros

        # Two pointers approach
        left = 0
        right = n - 1

        # Fill result array from right to left (largest to smallest)
        for i in range( n-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result
    
# %%
def run_text_case():
    """Run predefined test cases."""

    solution = Solution()
    
    test_cases = [
        [1, 2, 3],
        [-1, 2, 3, -4, -5],
        [-7, -3, 2, 3, 11],
    ]

    print("Running the test cases:")
    print("=" * 30)

    for i, nums in enumerate(test_cases):
        result = solution.sortedSquares(nums)
        print(f"Test case {i + 1}: {nums}\nResult: {result}\n")


# %%
if __name__ == "__main__":
    run_text_case()
# %%
