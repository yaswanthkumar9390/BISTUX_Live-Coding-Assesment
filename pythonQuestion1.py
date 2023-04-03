sentence=input().split()
output_string=""
for i in sentence:
    if i[0]=="a":
        output_string+='*'*(len(i)-1)+" "
    else:
        output_string+=i+" "
print(output_string)
