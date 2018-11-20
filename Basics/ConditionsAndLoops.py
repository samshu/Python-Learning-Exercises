def print_squares_of_numbers_to(n):
    for i in range(1, n+1, 1):
        print (i*i)


def print_even_numbers_to(n):
    for i in range(0, n+1, 2):
            print i


def print_reverse_numbers(n):
    for i in range(n, -1, -1):
        print i


print "Squares of numbers"
print_squares_of_numbers_to(10)
print "Printing Even Numbers"
print_even_numbers_to(10)
print "Print Numbers in Reverse"
print_reverse_numbers(10)

print "Multiplication Table"


def multiplication_table(n):
    for num in range(1, n+1):
        for i in range(1, 10):
            print num * i
        print "----------------"


multiplication_table(2)


def division_is_different(dividend, divisor, cast_type):
    print 'Quotient Is '
    remainder = cast_type(dividend)/divisor
    print remainder
    print type(remainder)


division_is_different(10, 5, float)
division_is_different(10, 3, int)


def is_prime(num):
    if num < 2 or (not num % 2):
        return 'CONSONANT'
    for i in range(3, num, 2):
        if not num % i:
            return 'CONSONANT. Divisible by {}'.format(i)
    return "PRIME"


# def is_prime_sieve(num):
#    for i in range(2, num):
#        if i == False and i%

print is_prime(1223171)
