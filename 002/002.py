import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def is_even(number):
    return (number % 2) == 0

def main():
    one_million = pow(10, 6)
    four_million = 4 * one_million
    term_1 = 1
    term_2 = 2

    sum = 0
    if is_even(term_1): sum += term_1
    if is_even(term_2): sum += term_2

    next_term = term_1 + term_2
    while (next_term < four_million):
        if is_even(next_term): sum += next_term
        term_1 = term_2
        term_2 = next_term
        next_term = term_1 + term_2

    print('result: {}'.format(sum))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))
