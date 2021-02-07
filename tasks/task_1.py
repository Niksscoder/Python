'''
Sample input :
	a aa abC aa ac abc bcd a

Sample Output :
	ac 1
	a 2
	abc 2
	bcd 1
	aa 2

'''

n = str(input())
m = []
m.append([str(s.lower()) for s in n.split()])

d = {}

li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j]
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
    for key, value in d.items():
        print(key, value)