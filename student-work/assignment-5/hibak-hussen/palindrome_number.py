class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10

# Test case 1: Palindrome number
solution = Solution()
print(solution.isPalindrome(121))  # Output: True

# Test case 2: Negative number
print(solution.isPalindrome(-121))  # Output: False

# Test case 3: Non-palindrome number
print(solution.isPalindrome(10))  # Output: Fals
