def solver(start, end, even=False, odd=False):
    if start > end:
        return None
    
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] <= end:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    result = 0
    for term in fibonacci_sequence:
        if start <= term <= end:
            if (even and term % 2 == 0) or (odd and term % 2 != 0):
                result += term
        
    return result
print(solver(start=15812, end=91581312, even=False, odd=True))
