import math
import strutils

const MAX = 1_000_000_00

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

var (sieve, primes) = Eratosthenes_sieve(MAX)

var maxc = 0

for p in primes:
    var sp = strutils.intToStr(p)
    for i in countdown(high(sp), 1):
        sp = strutils.intToStr(p)
        if sp[i] < '3':
            var count = 0
            while sp[i] <= '9':
                if sieve[strutils.parseInt(sp)] == false:
                    count += 1
                inc(sp[i])
            if count > maxc:
                maxc = count
                echo(p)
                echo(count)
            if count == 8:
                echo(p)

    sp = strutils.intToStr(p)
    for ch in "0123456789":
        if strutils.count(sp, ch) >= 2:
            var count = 0
            for ch1 in "0123456789":
                let n = strutils.parseInt(strutils.replace(sp, ch, ch1))
                if sieve[n] == false and strutils.intToStr(n).len == sp.len:
                    count += 1
            if count > maxc:
                maxc = count
                echo(sp)
                echo(maxc)
