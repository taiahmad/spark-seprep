def sortedSquares(nums):
    square_nums = []
    for num in nums:
        square_nums.append(num**2)
    square_nums.sort()
    return square_nums
print(sortedSquares([-4,-1,0,5,9]))