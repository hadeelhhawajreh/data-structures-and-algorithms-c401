def reverse_array(arr):
    size=len(arr)
    index=size-1
    for i in range(0,(size//2)):
        temp=arr[index]
        arr[index]=arr[i]
        arr[i]=temp
        (index)-=1
    return arr

list=[1,2,3,4,5,6,8]
print(reverse_array(list))