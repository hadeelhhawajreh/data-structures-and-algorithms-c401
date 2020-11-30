def add_middle(arr,x):
    size=len(arr)
    mid=size//2
    # print(size,mid)
    arr2=[]
    a=0
    for i in range(size+1):
        if i!=mid:
            arr2.append(arr[a])
            a+=1
        else:
            arr2.append(x)
    return arr2
a=[1,2,3,4,5,6,7]
b=10
print(add_middle(a,b))