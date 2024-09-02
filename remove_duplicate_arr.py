arr=[1,2,1,1,3,2]
new_arr=[" "]
i=0
for item in arr:
    if item not in new_arr:
        new_arr[i]=item
        i+=1
        # new_arr.append(item)
print(new_arr)