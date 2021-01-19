"""
Calculating the Least Common Multiplier with the Greatest Common Denominator
"""
import GCD

def gcd(n1, n2):
    # The Euclid's Algorithm.
    while n2:      
        n1, n2 = n2, n1 % n2
    return n1

def lcm_gcd(n1, n2):
    return n1 * n2 // gcd(n1, n2)
       
# OR

def lcm_gcd(n1, n2):
    return n1 * n2 // GCD.gcd(n1, n2)
