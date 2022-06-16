def test(s):
    s = s.strip()
    # 2. if the string is blank then return 0
    if len(s) == 0:
        return 0
    # 3. initialize temp as 0 string, and result as 0 int
    temp = "0"
    result = 0
    # 4. initialize pointer i
    i = 0
    # 5. check if the first character in the string is  + or -
    # - if it is + or -, set temp equal to str[0], then increment i=1 
    if s[0] in "+-":
        temp = s[0]
        i = 1
    # 6. setting the minimum and the maximum
    min_int = -2147483648
    max_int = 2147483647
    # 7. Iterate through the string, if the current element is a digit 
    # then add it to temp, if not a digit then break
    for i in range(i, len(s)):
        if s[i].isdigit():
            temp += s[i]
        else:
            break
    # 8. if the length of temp variable is more than one (which means
    # str has characters more than +,-, then convert temp into int and store it into 
    if len(temp)>1:
        result  = int(temp)

    # 9. check if result has value more than max and min ranges
    if result>max_int:
        return max_int
    elif result<min_int:
        return min_int
    else:
        return result

test("words with 987")