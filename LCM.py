"""
Least Common Multiplier: It is the smallest positive integer evenly divisible by all set numbers.
"""

def lcm(n1, n2):
    multiplier = 0
    if n1 > n2:
        multiplier = n1
    else:
        multiplier = n2
        
    while(True):
        if multiplier % n1 == 0 and multiplier % n2 == 0:
            break
        else:
            multiplier += 1
    return multiplie
    
    
    
def gcd(n1, n2):
    # The Euclid's Algorithm.
    while n2:      
        n1, n2 = n2, n1 % n2
    return n1
    
    

    
    
    
    
   
