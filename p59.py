import string
lst = eval ("[ %s ]" % ( open("p059_cipher.txt").readline() ))

key = []

for i in [0, 1, 2]:
    save, maxcount = ' ', -1
    for c in string.ascii_lowercase:
        count = 0
        for j in range(0, len(lst)/3):
            if chr(lst[3*j + i] ^ ord(c) ) in string.ascii_letters: count += 1
        if count > maxcount: maxcount, save = count, c
    key.append(ord(save))
    print save,

s = 0
for i in range(len(lst)):
    s  += lst[i] ^ key[i % 3]

print "\n", s

