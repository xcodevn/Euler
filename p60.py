
prime = 1000001 * [0]
p = []

for i in range(2, 1000000+1):
    if prime[i] == 0:
        p.append(i)
        for j in range(2, 1000000/i + 1):
            prime[i*j] = 1

def isPrime(n):
    if n < 1000000:
        return prime[n] == 0

    for pp in p:
        if pp*pp > n: return True
        if n % pp == 0: return False
    return True

def thu(i, arr, ti):
    if ti == 4:
        print arr
        print sum(arr)
    count = i+1
    while True:
        num = p[count]
        if num > 10000: break
        flag = True
        for pp in arr:
            if not isPrime(int(str(pp) + str(num)))  or not isPrime(int(str(num) + str(pp))):
                flag = False
                break
        if flag == True: thu(count, arr + [num], ti+1)
        count += 1
        if count >= len(p): break

thu(0, [], 0)


