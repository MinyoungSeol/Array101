# %%
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0

            if current_count > max_count:
                max_count = current_count

        return max_count
    
# %%
### Test
if __name__ == "__main__":

    solution = Solution()

    # Test cases

    test_cases = [
        [0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]

    print("Let's test the function with some cases:")

    for i, nums in enumerate(test_cases):
        result = solution.findMaxConsecutiveOnes(nums)
        print(f"Test case: {i + 1}: {nums}, Result: {result}")


# %%
### Trying to add a test case with user input
    print("\nNow let's test with Your numbers.")
    print("Enter 'quit' or 'exit' to stop testing.")

    while True:
        user_input = input("Enter a list of binary numbers separated by spaces: ").strip()
        # .strip() removes whitespace characters (spaces, tabs, newlines) from the beginning and end of a string.
        # It helps to process the input accurately.
        
        if user_input.lower() in ['quit', 'exit']:
            print("Exiting the test.")
            break

        try:
            user_nums = list(map(int, user_input.split()))
            # .split() splits the string into a list of substrings based on whitespace.
            # map(int, ...) converts each substring to an integer.
            
            # Binary validation
            if all(num in [0, 1] for num in user_nums):
                user_result = solution.findMaxConsecutiveOnes(user_nums)
                print(f"Your input: {user_nums}, Result: {user_result}")
            else:
                print("Please enter only 0s and 1s.")

        # Error handling
        except ValueError:
            print("Please enter a list of binary numbers (0s and 1s) separated by spaces, \nor 'quit'/'exit' to exit.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

# %%
