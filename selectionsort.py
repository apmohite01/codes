arr=[12,32,4,23,-4,30]
for i in range (len(arr)-1):
    min=i
    for j in range(i+1,len(arr)):
        if(arr[min]>arr[j]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print(arr)