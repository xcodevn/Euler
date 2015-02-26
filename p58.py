i = 2
s = 1
def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0: return 0
        i += 1
    return 1
c = 0
while True:
    s += 4
    d1 = i*i + 1
    d0 = d1 - i
    d2 = d1 + i
    d3 = d2 + i
    c += isPrime(d0)
    c += isPrime(d1)
    c += isPrime(d2)
    c += isPrime(d3)
    if  c*100.0 /s < 10.0:
        print i+1
        break
    i += 2

