e = [2, 2]
for k in range(1, 40):
    e.append(1)
    e.append(2*k)
    e.append(1)
a = 1
b = e[100]
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

for i in range(1, 100):
    k = 100 - i
    (a, b) = (b, b*e[k] + a)
    (a, b) = (a/gcd(a, b), b/gcd(a, b))

print a, b
print sum ([int(c) for c in str(b) ])

