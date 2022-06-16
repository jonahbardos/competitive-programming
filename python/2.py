# Return kth largest element in array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
nums = [3,2,1,5,6,4]
k = 2

def p2(nums, k):
    nums.sort()
    return nums[len(nums) - k]