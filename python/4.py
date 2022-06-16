def p4(a, b ,c):
    points = 0

    while True:
        # Check which has stones
        counter = 0
        if a > 0 and counter < 2:
            a -= 1
            counter += 1
        if b > 0 and counter < 2:
            b -= 1
            counter += 1
        if c > 0 and counter < 2:
            c -= 1
            counter += 1
        
        if counter == 2:
            points += 1
        else:
            # Game ends
            print("game done", (a,b,c), points)
            return


p4(2,4,6)