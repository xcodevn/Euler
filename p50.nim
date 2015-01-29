import math

const MAX = 1_000_000

proc Eratosthenes_sieve(bound: int):tuple[sieve:seq[bool], primes: seq[int]] =
    var primes: seq[int] = @[]
    var list : seq[bool] = newSeq[bool](bound+1)

    var i = 2
    while i <= high(list):
        if list[i] == false:
            primes.add(i)
            var j = i*i
            while j <= high(list):
                list[j] = true
                j += i
        i += 1
    return (list, primes)

let (sieve, primes) = Eratosthenes_sieve(MAX)
var 
    maxlen = 1
    sum = 2

for i in 0..primes.len-1:
    var s = 0
    for j in i..high(primes):
        s = s + primes[j]
        if s > MAX: break

        if sieve[s] == false and j - i + 1 > maxlen:
            maxlen = j -i + 1
            sum = s
echo(sum)
