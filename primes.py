#!/usr/bin/python3

# copyright 2020 Edmundo Carmona Antoranz
# released under the terms of GPLv2


# a script to list the primes up to 100

primes=[]

def isPrime(aNumber):
  prime=True
  for i in primes:
    prime=aNumber % i > 0
    if not prime:
      break
  # if we made it this far, it's a prime
  if prime:
    primes.append(aNumber)
  return prime

for i in range(2, 100):
  if isPrime(i):
    print(i)
