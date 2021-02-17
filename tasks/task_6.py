''' 
Sample input : hello
sample output: {h: 1, e: 1, l: 2, 0: 1}

'''

# first solve
inp = input()
spis = {}
new_spis = []
for i in range(len(inp)):
	count=1
	if inp[i] not in new_spis:
		new_spis.append(inp[i])
		spis.update({inp[i]: count})
		count = 1
	else:
		count += 1
		spis.update({inp[i]: count})

print(spis)


# second solve
def char_frequency(arr):
    dict = {}
    for n in arr:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

# arr = hello
stri = input()
print(char_frequency(stri))






