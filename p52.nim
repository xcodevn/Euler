import strutils

proc toString(num: int): array[10,int] =
    var n = num
    var rl: array[10, int]
    while n != 0:
        rl[n mod 10] += 1
        n = n div 10
    return rl
        
var num = 1
while true:
    num += 1
    let ori = toString(num)
    if ori != toString(2*num): continue
    if ori != toString(3*num): continue
    if ori != toString(4*num): continue
    if ori != toString(5*num): continue
    if ori != toString(6*num): continue
    if ori != toString(7*num): continue
    echo(num, " ", 2*num, " ", 3*num, " ", 4*num, " ", 5*num, " ", 6*num)
