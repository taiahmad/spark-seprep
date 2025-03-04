def plusOne(self, digits: List[int]) -> List[int]:

	for i in range(len(digits) - 1, -1, -1):

        	if digits[i] + 1 != 10:
       			digits[i] += 1
        		return digits
            
		digits[i] = 0

            	if i == 0:
                	return [1] + digits

# Test case
Input = [1,2,3]
Output =  [1,2,4]
print(f"Plus 1 will show change from {Input} to {Output}")
