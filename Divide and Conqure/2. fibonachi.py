num = 10


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


if __name__ == "__main__":
    print(fib(num))
