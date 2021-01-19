"""
Least Common Multiplier: It is the smallest positive integer evenly divisible by all set numbers.
"""
class lcm:
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
        return multiplier
