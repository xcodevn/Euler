var i = 2
var s = 1

proc isPrime(n: int ): int =
    var i = 2
    while i*i <= n:
        if n mod i == 0: return 0
        i += 1
    return 1
var c = 0
while true:
    s += 4
    var d1 = i*i + 1
    var d0 = d1 - i
    var d2 = d1 + i
    var d3 = d2 + i
    c += isPrime(d0)
    c += isPrime(d1)
    c += isPrime(d2)
    c += isPrime(d3)
    if  float(c)*100.0 /float(s) < 10.0:
        echo i+1
        break
    i += 2

