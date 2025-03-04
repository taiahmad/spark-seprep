def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
     """
    y=str(x)
    z=""
    for i in range(len(y)):
        z=z+ y[-1]
        y=y[:-1]
       
    if z==str(x):
        return True
    else:
        return False
#Test 
test1=121
result=isPalindrome(test1)

test2=-121
result2=isPalindrome(test2)

test3=10
result3=isPalindrome(test3)

