"""
    Tactic:
    Sliding glass window
"""
def p1(s):
    window = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        res = max(res, r-l+1)
        window.add(s[r])