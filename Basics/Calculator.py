number1 = input("Enter number1")
number2 = input("Enter number2")
operation = raw_input("Enter Operation +;-;*;/;oe")


def print_output(output):
    print "{} {} {} = {}".format(number1, operation, number2, output)


if operation == '+':
    print_output(int(number1)+int(number2))
elif operation == '-':
    print_output(int(number1)-int(number2))
elif operation == 'oe':
    print "ODD" if number1 % 2 else "EVEN"
