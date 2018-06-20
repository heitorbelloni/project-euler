import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def is_multiple_of(number, divisor):
    return (number % divisor) == 0

def is_multiple_of_3(number):
    return is_multiple_of(number, 3)

def is_multiple_of_5(number):
    return is_multiple_of(number, 5)

def main():
    limit = 1000
    sum = 0
    for natural_number in range(1, limit):
        if is_multiple_of_3(natural_number) or is_multiple_of_5(natural_number):
            sum += natural_number
    print('result: {}'.format(sum))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))