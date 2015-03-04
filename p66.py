import  math

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def expand(e):
    l = len(e) - 1
    a = 1
    b = e[l]
    for i in range(1, l):
        k = l - i
        (a, b) = (b, b*e[k] + a)
        (a, b) = (a/gcd(a, b), b/gcd(a, b))
    return (b, a)

def testD(n):
    a = int(math.floor(math.sqrt(n)))
    b = 1
    c = a
    lst = []
    li = [0]
    while True:
        li.append(a)
        (x, y) =  expand(li)
        if x**2 - n* y**2 == 1:
            return x
        lst.append( (a,b,c) )
        d0 = n - c*c
        d1 = d0 / b
        if d1 != d0*1.0 / b:
            print "error"
        a1 = int (math.floor((math.sqrt(n) + c)/d1))
        b1 = d1
        c1 = a1*d1 - c
        a, b, c = a1, b1, c1
        #if (a,b,c) in lst:
        #    return len(lst) - lst.index( (a,b,c) )

print testD(2)
print testD(3)
print testD(5)
print testD(6)
print testD(7)
ll = []
for i in range(2, 1000 + 1):
    if int(math.sqrt(i))**2 != i:
        ll.append((testD(i), i))
print max(ll)
