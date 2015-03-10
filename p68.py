import itertools
from sets import Set

ll = []
for inner in itertools.permutations(range(1,11), 5):
    com = [i for i in range(1,11) if i not in inner]
    s = 2*sum(inner) + sum(com)
    if s % 5 == 0:
        outer = []
        for i in range(5):
            num = s/5 - inner[i] - inner[(i+1)%5]
            if num in range(1,11): outer.append(num)
        if len(Set(outer)) == 5:
            idx = outer.index(min(outer))
            lst =[]
            for i in range(5):
                lst = lst + [outer[(idx+i)%5], inner[(idx+i)%5], inner[(idx+i+1)%5]]
            sti = "".join([str(di) for di in lst])
            if len(sti) == 16:
                ll.append(int(sti))
                print inner,outer,sti
print sorted(ll)
print max(ll)
