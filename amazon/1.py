def myAtoi(s):
    num_str = ""
    s = s.strip()

    break_counter = False
    for idx in range(len(s)):
        char = s[idx]
        if char.isnumeric():
            if idx > 0:
                if s[idx - 1] == "-":
                    num_str += "-"
                    num_str += char
                else:
                    break_counter = True
                    num_str += char
            else:
                break_counter = True
                num_str += char
        
        if not char.isnumeric() and break_counter == True:
            break_counter = False
            break
        
    # # Convert to integer
    try:
        num_str = int(num_str)
    except:
        return 0
        
    if num_str == 0:
        return num_str
    if num_str < -2 ** 31:
        return -2 ** 31
    elif num_str > 2 ** 31 - 1:
        return 2 ** 31 - 1
    
    return num_str
        
        




out = myAtoi("-4193 with words")
print(out)

out = myAtoi("4193 with words")
print(out)

out = myAtoi("+4193 with words")
print(out)

out = myAtoi("----------4193 with words")
print(out)

out = myAtoi("0")
print(out)

out = myAtoi("0032")
print(out)

out = myAtoi("words and 987")
print(out)