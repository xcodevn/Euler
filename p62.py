i = 1
dic = {}
def num2lst(num):
    s = 10*[0]
    for c in str(num): s[int(c)] += 1
    return "".join([str(d) for d in s])

while True:
    i = i + 1
    m = num2lst(i**3)
    if m in dic: dic[m].append(i)
    else: dic[m] = [i]
    if len(dic[m]) == 10:
        print dic[m][0]**3

