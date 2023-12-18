def solver(factors, start, end):
    sum = 0
    for i in range(start, end):
        for num in factors:
            if i % num == 0:
                sum += i
                break
    return sum


print(solver([4, 7, 11], 8912, 40512))
