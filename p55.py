def isLychrel(n):
    for i in range(50):
        newn = n + int(str(n)[::-1])
        if str(newn) == str(newn)[::-1]:
            return True
        n = newn
    return False

count = 0
for i in range(0, 10000+1):
    if not isLychrel(i): count += 1

print(count)
