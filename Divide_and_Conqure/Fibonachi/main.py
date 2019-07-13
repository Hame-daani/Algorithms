from .funcs import count_calls, gen_result

# counters dict to count function calls
# for each value
recur_count = {}
memo_count = {}

# cache to use in memo algorithm
cache = {}


@count_calls(recur_count)
def fib_recur(x):
    """
    Recursive algorithm with no optimization.\n
    T(n) = O(n^2)
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fib_recur(x-1) + fib_recur(x-2)


@count_calls(memo_count)
def fib_memo(x):
    """
    Recursive algorithm using a cache dictionary\n
    to memoising the results and speed up.\n
    T(n) = O(n)
    """
    if x in cache:
        return cache[x]
    else:
        if x == 0 or x == 1:
            cache[x] = 1
            return cache[x]
        else:
            cache[x] = fib_memo(x-1) + fib_memo(x-2)
            return cache[x]


if __name__ == "__main__":
    num = int(input("Enter number: "))

    print("-"*100)

    memo_result = gen_result(num, func=fib_memo, counts=memo_count)
    print(memo_result)

    print("-"*100)

    recur_result = gen_result(num, func=fib_recur, counts=recur_count)
    print(recur_result)

    print("-"*100)
