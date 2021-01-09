def partion(arr,first_index,last_index):
    lowest_value=first_index-1
    pivot=arr[last_index]
    for i in range(first_index,last_index):
        if arr[i]<= pivot:
            lowest_value += 1
            arr[i],arr[lowest_value]=arr[lowest_value],arr[i]
    arr[lowest_value+1],arr[last_index]=arr[last_index],arr[lowest_value+1]
    return lowest_value+1


def quick_sort(arr,low,high):
    if low<high:
        part=partion(arr,low,high)
        # print('PART',part)
    
        quick_sort(arr,part+1,high)
        quick_sort(arr,low,part-1)
    return arr

if __name__ == "__main__":
    # 10, 80, 30, 90, 40, 50, 70
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quick_sort(arr,0,n-1) 
    print () 
    strg=''
    for i in range(n): 
        strg+= str(arr[i]) +'  '
    print("QUICK SORT ",strg)

    print('************')
    a = [10, 80, 30, 90, 40, 50, 70] 
    n = len(a) 
    quick_sort(a,0,n-1) 
    print () 
    stg=''
    for i in range(n): 
        stg+= str(a[i]) +'  '
    print("QUICK SORT ",stg)