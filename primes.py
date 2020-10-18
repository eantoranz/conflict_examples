#!/usr/bin/python3

# copyright 2020 Edmundo Carmona Antoranz
# released under the terms of GPLv2


# a script to list the primes up to 100


def isPrime(aNumber):
  prime=True
  for i in range(2, aNumber):
    prime=aNumber % i > 0
    if not prime:
      break
  # if we made it this far, it's a prime
  return prime

for i in range(2, 10000):
  if isPrime(i):
    print(i)
