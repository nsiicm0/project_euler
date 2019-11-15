'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
def fib_generator():
    n_minus2 = 1
    yield(n_minus2)
    n_minus1 = 1
    yield(n_minus1)
    while True:
        n = n_minus2 + n_minus1
        yield n
        n_minus2 = n_minus1
        n_minus1 = n

def fib_sequence(n):
    fib = fib_generator()
    i = 0
    while i < n:
        yield next(fib)
        i += 1


if __name__ == "__main__":
    for i, el in enumerate(fib_generator(), 1):
        if len(repr(el)) >= 1000:
            print(i, el)
            break