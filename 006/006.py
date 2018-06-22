import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def main():
    limit = 100
    sum = 0
    sum_of_squares = 0

    for i in range(1, limit + 1):
        sum += i
        sum_of_squares += i * i

    square_of_the_sum = sum * sum
    difference = square_of_the_sum - sum_of_squares
    
    print('result: {}'.format(difference))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))