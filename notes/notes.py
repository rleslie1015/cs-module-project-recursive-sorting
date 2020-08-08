def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
    countdown(n-1)

# countdown(3)

# fib(n) = fib(n-1) + fib(n-2)
# 1, 1, 2, 3, 5, 8, 13
def fib(n):
# base case
    # if n == 0 return 0
    # if n == 1 return 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    n_minus_1 = fib(n-1)
    n_minus_2 = fib(n-2)
    # print(n_minus_1 + n_minus_2)
    return n_minus_1 + n_minus_2

fib(7)