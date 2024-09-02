def reverse(st):
    l=len(st)
    list1=[]
    value_set=l
    for i in range(1,l):
        if st[l-i]==" ":
            list1.append(st[l-i+1:value_set])
            value_set=l-i
    list1.append(st[0:value_set])    
    return list1
list1=reverse("Sweta is a girl.")
str1=''
for i in list1:
    str1=str1+i+" "
print(str1)