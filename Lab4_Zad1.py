# Stanisław Kusiak

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_gen(m):
    n = 1
    while n <= m:
        if is_prime(n):
            yield n
        n += 1

for num in prime_gen(1000):
    print(num)