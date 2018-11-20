import string


def is_vowel(char):
    return char in 'aeiou'


def is_hexa(l_string):
    return l_string in string.hexdigits


def is_consonant(char):
    return char in string.ascii_letters and not is_vowel('b')


def print_string(l_string):
    for i in l_string:
        print i


print is_vowel('a')
print is_hexa('1a')
print print_string('1a')
print 'a' in string.ascii_letters
print isinstance('a', str)
print is_consonant('b')

for i in "This is a sentence".split(" "):
    print i

print 2 * 'Test'
