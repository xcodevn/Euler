import strutils
import algorithm

let f = open("p054_poker.txt")

proc samesuit(h: seq[string]): bool =
    for i in h:
        if i[1] != h[0][1]: return false
    return true

proc samevalue(h: seq[string]): bool =
    for i in h:
        if i[0] != h[0][0]: return false
    return true

proc consecutive(h: seq[string]): bool =
    let order = "23456789TJQKA"
    var idx = strutils.find(order, h[0][0])
    for i in h:
        if i[0] != order[idx]: return false
        idx += 1
    return true

proc rank(h: seq[string]): tuple[rank: int, value: char] =
    if consecutive(h) and samesuit(h) and 
                h[0][0] == 'T': return (-1, 'T')
    elif consecutive(h) and samesuit(h): return (-2, h[0][0])
    elif samevalue(h[0..3]): return (-3, h[0][0])
    elif samevalue(h[1..4]): return (-3, h[1][0])
    elif samevalue(h[0..1]) and samevalue(h[2..4]): return (-4, h[4][0])
    elif samevalue(h[0..2]) and samevalue(h[3..4]): return (-4, h[2][0])
    elif samesuit(h): return (-5, h[4][0])
    elif consecutive(h): return (-6, h[4][0])
    elif samevalue(h[2..4]): return(-7, h[4][0])
    elif samevalue(h[1..3]): return(-7, h[3][0])
    elif samevalue(h[0..2]): return(-7, h[2][0])
    elif samevalue(h[1..2]) and samevalue(h[3..4]) : return(-8, h[4][0])
    elif samevalue(h[0..1]) and samevalue(h[3..4]) : return(-8, h[4][0])
    elif samevalue(h[0..1]) and samevalue(h[2..3]) : return(-8, h[3][0])
    elif samevalue(h[3..4]): return(-9, h[4][0])
    elif samevalue(h[2..3]): return(-9, h[3][0])
    elif samevalue(h[1..2]): return(-9, h[2][0])
    elif samevalue(h[0..1]): return(-9, h[1][0])
    else: return (-10, h[4][0])

proc gcmp[T](a: T, b:T): int =
    let order = "23456789TJQKA"
    return system.cmp(strutils.find(order, a[0]),
                      strutils.find(order, b[0]))

proc seqcmp(a:seq[string], b:seq[string]): bool=
    for i in countdown(high(a), low(a)):
        if gcmp(a[i], b[i]) == 1: return true
        elif gcmp(a[i], b[i]) == -1: return false
    return true

var count = 0
for l in f.lines:
    let lst = strutils.split(l, ' ')
    var (A, B) = (lst[0..4], lst[5..9])
    algorithm.sort[string](A, gcmp[string])
    algorithm.sort[string](B, gcmp[string])
    let (ra, rb) = (rank(A), rank(B))
    if ra.rank > rb.rank: count += 1
    elif ra.rank == rb.rank:
        let rl = gcmp(@[ra.value], @[rb.value])
        if rl == 1: count += 1
        elif rl == 0 and seqcmp(A, B): count += 1

echo(count)
