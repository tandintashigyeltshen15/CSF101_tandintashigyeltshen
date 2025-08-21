def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
print("recursive:", fib_recursive(2))

def fib_iterative(n):
    a, b = 0, 1
    count = 0

    while count < n:
        a, b = b, a + b
        count += 1
    return a 

print("iterative:", fib_iterative(2))
        