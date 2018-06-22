import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

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

def find_missing_prime(number, target):
    prime = 2
    while(prime < number):
        if is_prime(prime) and is_factor(prime, number) and is_factor(number, prime * target):
            return prime
        prime += (prime % 2) + 1
    
    return number

def main():
    ceiling = 20
    result = 1
    for factor in range(1, ceiling + 1):
        if not is_factor(factor, result):
            missing_prime = find_missing_prime(factor, result)
            result *= missing_prime
    
    print('result: {}'.format(result))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))