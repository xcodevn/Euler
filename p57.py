def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num=0
den=1
count = 0
for i in range(1000):
    newnum = den
    newden = 2*den + num
    g = gcd(newnum, newden)
    num, den = newnum/g, newden/g
    if len(str(num + den)) > len(str(den)): count += 1

print count
