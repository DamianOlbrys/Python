def factorial(n):
    if n == 1:
        result = 1
    else:
        result = n*factorial(n - 1)
        print(result)
    return result


print(factorial(900))
