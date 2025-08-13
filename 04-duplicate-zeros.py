# %%
class Solution:
    def duplicateZeros(self, arr):
        """
        Duplicate each occurrence of zero in the array.
        The length of the array remains unchanged.
        """
        n = len(arr)
        
        #Count zeros in the list
        zeros = 0
        
        for num in arr:
            if num == 0:
                zeros += 1
                
                
        #Backwards to avoid overwritting
        
        # i : reading pointer(original list)
        # j : writing pointer(final list)
        
        i = n - 1 #last element of original list
        j = n + zeros - 1 #last position with infinite space
        
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
                
            #If Zero found, duplicate it
            if arr[i] == 0:
                j -= 1
                if j < n: #Making sure to stay in bounds
                    arr[j] = 0
                    
            i -= 1
            j -= 1

# %%
def run_test_case():
    """Run predefined test cases."""

    solution = Solution()
    test_cases = [
        [1, 0, 2, 3, 0, 4, 5],
        [1, 2, 3],
        [0, 0, 0],
    ]
    print("Running the test cases:")
    print("=" * 30)
    for i, arr in enumerate(test_cases):
        print(f"Test case {i + 1}: {arr}")
        solution.duplicateZeros(arr)
        print(f"Result: {arr}\n")

# %%
if __name__ == "__main__":
    run_test_case()
# %%
