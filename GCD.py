"""
Greatest Common Divisor: it is the largest positive integer that divides each of the integers.
"""

def gcd(n1, n2):
  while n2:
    n1, n2 = n2, n1 % n2
  return n1
