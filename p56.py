maxs = -1

for i in range(2, 100):
    for j in range(2, 100):
        s = sum([int(l) for l in str(i**j)])
        if s > maxs:
            maxs = s
print(maxs)
