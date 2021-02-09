''' 
abcd
*d%#

abacabadaba
*d*%*d*#*d*

'''

# data
s1 = input() #alf
s2 = input() #res_alf

#lenth
lenth = len(s1) 

# dict to assignment lists
encode = input() # abdabdba
decode = input() # *dd*%#%*

# code = {s1:s2}
code = {}
#descrypt = {s2:s1}
descrypt = {}

for i in range(lenth):
	# assignment
    code.update({s1[i]: s2[i]})
    descrypt.update({s2[i]: s1[i]})

#main replacement
spis_for_encode = []
for i in encode: # abcabcab
	spis_for_encode.append(code[i])

spis_for_decode = [descrypt[i] for i in decode]

# result
print("".join(spis_for_encode))
print("".join(spis_for_decode))












