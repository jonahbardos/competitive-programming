"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not 
use the same element twice.

You can return the answer in any order.

Notes:
Since this is not asking for a subarray then we don't use sliding window
"""
def p3(arr: list, target: int)->list:
    seen = {}

    for i in range(len(arr)):
        if target - arr[i] in seen:
            return [seen[target-arr[i]], i]
        
        seen[arr[i]] = i
        
    return -1

x = p3([1,2,3], 6)
print(x)