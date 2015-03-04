lines = open("p067_triangle.txt").readlines()
mat = [ [int(w) for w in l.split(" ")] for l in lines]
print mat
l = len(mat)
opt = [mat[0][0], 0]
for i in range(1, len(mat)):
    lst = [opt[0] + mat[i][0]]
    for j in range(1, i+1):
        lst.append(max([opt[j-1], opt[j]]) + mat[i][j])
    lst.append(0)
    opt = lst
print max(opt)




