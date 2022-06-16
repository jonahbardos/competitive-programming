"""
    You are given a list of integers nums. You can reduce the length of nums by 
    taking any two integers, removing them, and appending their sum to the end. 
    The cost of doing this is the sum of the two integers you removed.

    Return the minimum total cost of reducing nums to one integer.
"""


nums = [-1,-1, 2]

def p3(nums):
    summ = 0
    
    # sort first
    nums.sort()
    while len(nums) > 1:
        min_num = nums[0]
        min_num2 = nums[1]
        total = min_num + min_num2
        nums.append(total)
        nums.pop(0)
        nums.pop(0)

        if total <= 0:
            nums.sort()

        summ += total
    
    print(summ)
        
        
        
p3(nums)