import sympy

def all_numbers(x):
    numbers = []
    number = str(x) * 2
    for i in range(len(str(x))):
        numbers.append(int(number[i: i+ len(str(x))]))
    return numbers

primes = sympy.sieve.primerange(2,1_000_000)
circular_primes = []

for prime in primes:
    if prime in circular_primes:
        continue
    circular = True

    for number in all_numbers(prime):
        if sympy.isprime(number) == False:
            circular = False
            break

    if circular:
        for num in all_numbers(prime):
            if num in circular_primes:
                continue
            else:
                circular_primes.append(num)

print(len(circular_primes))