# %%
class Solution:
    def noOfEvenNumDigits(self, nums):
        """
        This function counts how many numbers in the list have an even number of digits.

        args:
            nums: List[int]
            
        returns:
            int: Count of numbers with even number of digits
        """

        evenCount = 0

        for num in nums:
            digitCount =0

            if num == 0:
                digitCount = 1
                
            else:
                num = abs(num)  # Handle negative numbers
                while num > 0:
                    num = num // 10
                    digitCount += 1

            if digitCount % 2 == 0:
                evenCount += 1
        
        return evenCount
    
# %%
def run_text_case():
    """Run predefined test cases."""

    solution = Solution()

    test_cases = [
        [11, 345, 2, 6, 6883],
        [1, 333, 55555],
        [0, 10, 100, 1000],
        [-1, -22, -3333, -44444],
        [123456, 7890, 12, -34567, -890123],
    ]

    print("Let's test the function with some cases:")

    for i, nums in enumerate(test_cases):
        result = solution.noOfEvenNumDigits(nums)
        print(f"Test case: {i + 1}: {nums}, Result: {result}")

# %% 
def run_interactive_case():
    """Run interactive test cases with user input."""

    solution = Solution()

    print("\nNow let's test with Your numbers.")
    print("Enter any count of integers separated by space.")
    print("Enter 'quit', 'exit', 'q', or 'e' to stop testing.")
    print("=" * 50)

    while True:
        user_input = input("Enter a list of integers: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q', 'e']:
            print("Going back to main menu...")
            break
        
        try:
            user_nums = list(map(int, user_input.split()))

            result = solution.noOfEvenNumDigits(user_nums)
            print(f"Input: {user_nums}, \nResult: {result}")

        except ValueError:
            print("Invalid input. Please enter a list of integers separated by spaces.")
        
        except Exception as e:
                print(f"Unexpected Error: {e}")


# %%
def program():
    print("Welcome to the 'Count Numbers with Even Number of Digits' program!")
    print("You can test the function with predefined cases or your own input.")
    print("Choose an option:")
    print("1. Run predefined test cases")
    print("2. Enter your own numbers")
    print("3. Exit")

    while True:
        choice = input("Type option number (1, 2, or 3): ").strip()
        if choice == '1':
            run_text_case()
        elif choice == '2':
            run_interactive_case()
        elif choice == '3' or choice.lower() in ['quit', 'exit', 'q', 'e']:
            print("Thank you for using the program. Goodbye!")
            break
            
    
# %%
if __name__ == "__main__":

    program()

