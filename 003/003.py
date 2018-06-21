import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def is_even(number):
    return (number % 2) == 0

def is_factor(factor, number):
    return (number % factor) == 0

def is_prime(number):
    if (number <= 1): return False
    if (number <= 3): return True
    if ((number % 2) == 0) or ((number % 3) == 0): return False
    
    i = 5
    while ((i * i) <= number):
        if ((number % i) == 0) or ((number % (i + 2)) == 0):
            return False
        i += 6
    
    return True

def main():
    number = 600851475143
    largest_prime_factor = 1
    if is_even(number): largest_prime_factor = 2

    candidate_factor = 3
    while (candidate_factor <= number):
        if is_factor(candidate_factor, number) and is_prime(candidate_factor):
            largest_prime_factor = candidate_factor
            number = (number // candidate_factor)

        candidate_factor += 2

    print('result: {}'.format(largest_prime_factor))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))
