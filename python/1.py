# First unique char in string

input_s = "aabb"

def p1(strr):
    seen = {}

    for idx in range(len(strr)):
        # print(strr[idx])
        if strr[idx] not in seen:
            seen[strr[idx]] = [1, idx]
        else:
            seen[strr[idx]][0] += 1

    # Check dictionary that has a value of 1 and since it is ordered get the
    # first one
    for s in seen:
        if seen[s][0] == 1:
            return seen[s][1]
    return -1


out = p1(input_s)
print(out)