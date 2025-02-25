def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    new_x = str(x)
    half = len(new_x) // 2
    for i in range(0, half):
        if new_x[i] != new_x[-i - 1]:
            return False
        if new_x[i] == new_x[-i]:
            continue
    return True    
    
# Test cases
x = 121
result_x = isPalindrome(x)
print(f"Is the number {x} a palindrome? {result_x}")

y = -121
result_y = isPalindrome(y)
print(f"Is the number {y} a palindrome? {result_y}")

z = 10
result_z = isPalindrome(z)
print(f"Is the number {z} a palindrome? {result_z}")
