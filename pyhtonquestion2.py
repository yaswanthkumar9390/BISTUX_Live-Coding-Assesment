string=input().split()
sorted_string=sorted(string)
multiple_string=[]
for i in sorted_string:
    evry_list=[]
    for j in string:
        if i[0]==j[0]:
            evry_list.append(j)
    multiple_string.append(evry_list)
lists=[]
for j in multiple_string:
    if j not in lists:
        lists.append(j)
for i in lists:
    print(i)
