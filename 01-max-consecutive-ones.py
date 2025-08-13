# %%
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        This function finds max number of consecutive 1's in a binary list.

        args:
            nums: List[int]

        returns:
            int: Max num of consecutive 1's
        """

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
def run_test_case():
    """Run predefined test cases."""
    
    solution = Solution()

    test_cases = [
        [0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]

    print("Let's test with given list first:")

    for i, nums in enumerate(test_cases):
        result = solution.findMaxConsecutiveOnes(nums)
        print(f"Test case: {i + 1}: {nums}, Result: {result}")


# %%
def run_interactive_test():
    """Run interactive test cases with user input."""

    solution = Solution()

    print("\nNow let's test with Your numbers.")
    print("Enter any count of only binary numbers (0s and 1s)")
    print("Enter 'quit' or 'exit' to stop testing.")
    print("=" * 50)

    while True:
            user_input = input("Enter a list of binary numbers: ").strip()
            # .strip() removes whitespace characters (spaces, tabs, newlines) from the beginning and end of a string.
            # It helps to process the input accurately.
            
            if user_input.lower() in ['quit', 'exit']:
                print("Thx for testing! Goodbye!")
                break
            
            """ Handling user input: """
            try:
                if ' ' in user_input:
                    user_nums = list(map(int, user_input.split()))
                    # .split() splits the string into a list of substrings based on whitespace.
                    # map(int, ...) converts each substring to an integer.
                else:
                    # if user input is not separated by spaces
                    user_nums = [int(char) for char in user_input]
                        # This converts each character in the string to an integer.
                
                # Binary validation
                if all(num in [0, 1] for num in user_nums):
                    user_result = solution.findMaxConsecutiveOnes(user_nums)
                    print(f"Your input: {user_nums}, \nMax count of consecutive 1s: {user_result}")
                else:
                    print("Please enter only 0s and 1s.")

            # Error handling
            except ValueError:
                print("Please enter a list of binary numbers (0s and 1s) separated by spaces, \nor 'quit'/'exit' to exit.")

            except Exception as e:
                print(f"Unexpected Error: {e}")

# %%
def program():
    """Main function to run the program."""
    print("Hi! This program finds max count of consecutive 1s in a binary list.")
    
    while True:
        choice = input("Choose an option:\n1. Run predefined test cases\n2. Run interactive test case\n3. Exit\nType option number: ").strip()
        if choice == '1':
            run_test_case()
        elif choice == '2':
            run_interactive_test()
        elif choice == '3':
            print("Thank you for using the program! Goodbye!")
            break
        else:
            print("Oops! Please choose a valid option (Enter 1, 2, or 3).")

# %%
if __name__ == "__main__":

    program()
