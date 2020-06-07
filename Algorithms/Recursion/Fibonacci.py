def fibonacci(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci(n - 2) + fibonacci(n - 1)
    print(result)
    return result


print(fibonacci(50))
