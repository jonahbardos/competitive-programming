"""
    Given an array of positive integers, find the subarray that add up to a
    given number.

    Requirements:
    All numbers that are input must be > 0. Otherwise Kadens algorithm must be
    used.

"""
# [1,7,4,3,1,2,1,5,1], target = 7
def p1(arr : list, target : int) -> list:
    total = 0
    window = []
    allsubs = []
    for num in arr:
        total = sum(window)
        
        while total > target: # we shrink
            window.pop(0)
            total = sum(window)

        if total == target:
            allsubs.append(list(window))
            # return window
        
        window.append(num)
    
    print(allsubs)

p1([1,7,4,3,1,2,1,5,1], 8)