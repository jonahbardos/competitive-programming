"""
    Given a string 's', find the length of the longest substring without
    repeating characters.
"""


def p2(s : str):
    window = []
    l = 0
    out = 0

    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        
        window.append(s[r])
        out = max(out, r - l + 1)