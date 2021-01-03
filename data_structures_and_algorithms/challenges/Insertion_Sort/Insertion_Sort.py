arr=[8,4,23,42,16,15]
def InsertionSort(arr):
    tem=[]
    for i in range(len(arr)):
        # print(i)
        j=i-1
        temp=arr[i]
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            print( arr[j+1], ' ',arr[j])
            
            j-=1
        arr[j+1]=temp
        tem=arr
        
        
    return tem
        
print(InsertionSort(arr))