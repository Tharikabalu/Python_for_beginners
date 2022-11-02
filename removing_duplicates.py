num_list=[5,7,3,8,5,90,4,8,43,98,54,95,8,79,578,0,4,789,45,46,89]
uniques=[]
for i in num_list:
    if i not in uniques:
        uniques.append(i)
print(uniques)
uniques.sort()
print(uniques)

