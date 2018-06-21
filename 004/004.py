import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def reverse(number):
    reversed_number = 0
    while (number > 0):
        reversed_number = (reversed_number * 10) + (number % 10)
        number //= 10
    
    return reversed_number

def is_palindrome(number):
    reversed_number = reverse(number)
    return (reversed_number == number)

def main():
    biggest_palindrome = 0
    for factor1 in range(999, 99, -1):
        for factor2 in range(factor1, 99, -1):
            number = factor1 * factor2
            if number <= biggest_palindrome: break
            if is_palindrome(number):
                biggest_palindrome = number
                break
    
    print('result: {}'.format(biggest_palindrome))

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))
