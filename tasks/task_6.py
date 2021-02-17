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
def char_frequency(inp):   # inp:str --> input('hello')
    dict = {}              # create new empty dict
    for el in arr:
        keys = dict.keys()
        if el in keys:
            dict[el] += 1  # dict[el] = for example it is 'h' if 'h' in key of our dict --> {'h': +=1}
        else:
            dict[el] = 1   # if dict[el] not in dict yet, for example 'e' --> {'e': 1} 
    return dict

# arr = hello
inp = input()
print(char_frequency(inp))






