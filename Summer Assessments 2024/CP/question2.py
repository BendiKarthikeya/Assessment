'''Given a number N, Print first N prime number starting from 2 and skipping every 
alternate prime number
Example Input:
5
Example Output:
2 5 11 17 23
Explanation :
▪ First few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 …
▪ First five alternate prime numbers will be 2, 5, 11, 17, and 23'''



def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_alternate_primes(N):
    count = 0
    num = 2
    while count < N:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1
        while True:
            if is_prime(num):
                break
            num += 1
    print()

N = int(input("Enter the value of N: "))
print("Output:")
print_alternate_primes(N)



'''def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return primes

def print_alternate_primes(N):
    sieve_size = 10000  # Choose a sufficiently large size for the sieve
    primes = sieve_of_eratosthenes(sieve_size)
    result = []
    i = 0
    count = 0
    while count < N:
        if i % 2 == 0:
            result.append(primes[i])
            count += 1
        i += 1
    print(*result)

# Example Input
N = 5
print_alternate_primes(N)'''
