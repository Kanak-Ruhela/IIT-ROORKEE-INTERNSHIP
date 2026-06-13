list = [1,4,3,5,6,4,5,3,9,6,7,7,8,9]
new_list = []
for x in list:
    if x not in new_list:
        new_list.append(x)
print(new_list)

