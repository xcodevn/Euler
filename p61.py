from sets import Set
import itertools

def setfunc(fun):
    lst = []
    for i in range(1000):
        if fun(i) >= 1000 and fun(i) <= 9999:
            lst.append(fun(i))
    return lst

lst = [ setfunc(lambda n: n*(n+1)/2),
        setfunc(lambda n: n*n),
        setfunc(lambda n: n*(3*n-1)/2),
        setfunc(lambda n: n*(2*n-1)),
        setfunc(lambda n: n*(5*n-3)/2),
        setfunc(lambda n: n*(3*n-2)) ]

cc = 6*[0]

def thu(loc, case, num):
    global cc
    l = []
    if loc == 6:
        if cc[0] / 100 == cc[5] % 100:
            print cc
            print sum(cc)
        cc = 6*[0]
        return
    if loc == 0:
        l = lst[case[loc]]
    else:
        for nn in lst[case[loc]]:
            if nn / 100 == num: l.append(nn)
    for nn in l:
        head = nn / 100
        tail = nn % 100
        if len(str(head)) == 2 and len(str(tail)) == 2:
            cc[loc] = nn
            thu(loc+1, case, tail)

for case in itertools.permutations(range(6)):
    thu(0, case, 00)
