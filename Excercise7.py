"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Below is the code block to find n pythagorean triples(unique not multiples). (taken from w3schools)

"""

def pythagoreanTriplets(limits):
    c, m = 0, 2
 
    # Limiting c would limit
    # all a, b and c
    alist = []
    blist = []
    clist = []
    while c < limits :
      
         
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > limits :
                break
            print(a,b,c)
        m = m + 1
