def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: if n is greater than 1, call the function with n-1 and multiply by n
    else:
        return n * factorial(n - 1)


# Call the factorial function and print the result
result = factorial(5)
print(result)  # Output: 120