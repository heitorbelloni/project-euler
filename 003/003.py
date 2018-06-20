import timeit

def timed_execution(function, *args):
    start = timeit.default_timer()
    function(*args)
    end = timeit.default_timer()
    return (end - start)

def main():
    print('result: {}')

elapsed = timed_execution(main)
print('elapsed: {}'.format(elapsed))
