class Solution(object):
    def removeElement(self, nums, val):
        k = 0
    
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
    
        return k

# Test case
solution = Solution()  # Create an instance of the Solution class
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)  # Call the method on the solution instance

print("Removing the integer", val, "results in the array:", nums[:k])
