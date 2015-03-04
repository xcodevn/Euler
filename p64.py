import math
n = 13


def fac(n):
    a = int(math.floor(math.sqrt(n)))
    b = 1
    c = a
    lst = []
    while True:
        lst.append( (a,b,c) )
        d0 = n - c*c
        d1 = d0 / b
        if d1 != d0*1.0 / b:
            print "error"
        a1 = int (math.floor((math.sqrt(n) + c)/d1))
        b1 = d1
        c1 = a1*d1 - c
        a, b, c = a1, b1, c1
        if (a,b,c) in lst:
            return len(lst) - lst.index( (a,b,c) )
print fac(2)
print fac(3)
print fac(5)
print fac(6)
print fac(7)
print fac(8)
print fac(10)
print fac(11)
print fac(12)
print fac(13)

count = 0
for i in range(2, 10000+1):
    if int(math.sqrt(i))**2 != i:
        if fac(i) % 2 == 1: count += 1
print count

