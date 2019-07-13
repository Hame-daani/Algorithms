def count_calls(counter):
    """
    A decorator to count number of\n
    'function calls' with each algorithm.
    """
    def decorator(func):
        def wrapper(x):
            counter[x] = 1 if x not in counter else counter[x]+1
            return func(x)
        return wrapper
    return decorator


def gen_result(num, func, counts):
    """
    Generate a result string for output purpose.\n
    including 'result', number of 'total calls' and
    number of 'calls for each value'.
    """
    def sum_calls(counts):
        """
        return sum of all values in counter dict.
        """
        total = 0
        for x in counts.values():
            total += x
        return total
    # main function
    result = f"""   fib memo {num} is {func(num)}.
    total calls: {sum_calls(counts)}.
    number of each call:
    {counts}"""
    return result
