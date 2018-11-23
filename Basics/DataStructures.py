user_list = ['muhammad', 'aathif']
for user in user_list:
    print(user)
user_list.append('muhammad')
# extending with a tuple
user_list.extend(('aa', 'bb'))
print(user_list)

print('Initializing a Fibonacci Array is so easy!')
fibonacci = [0, 1]
fibonacci.extend(sum(fibonacci[i-2:i]) for i in range(2, 10))
print(fibonacci)

for i in range(0, 20):
    print(i%2, end=',')

print('Prime Sieve')
prime_sieve = [i for i in range(0, 20) if i % 2 == 0]
print(prime_sieve.__len__())
