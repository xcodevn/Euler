from sets import Set
lst = []
for i in range(10):
    for j in range(1, 25):
        nn = str(i**j)
        if len(nn) == j:
            lst.append(i**j)
print Set(lst)
print len(Set(lst))
