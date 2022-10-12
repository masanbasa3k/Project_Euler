import sympy
prime_count = 0

for i in range(-1000, 1000):
    for j in sympy.primerange(1, 1000):
        aux_prime_count = 0
        n = 0
        while sympy.isprime(n ** 2 + i * n + j):
            aux_prime_count += 1
            n += 1
        if aux_prime_count > prime_count:
            prime_count = aux_prime_count
            imax = i
            jmax = j
print(imax * jmax)