```python
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
```
first the array value [8,4,23,42,16,15]
tem is empty array
looping from 0 to 6
j=-1
1. iteration 1
temp=arr[0] ---> temp=8
i	0
j	-1
temp	8
8	4	23	42	16	15
2. iteration 2 
i	1
j	0
temp	4
8	8	23	42	16	15
3. iteration 3
i	2
j	-1
temp	4
4	8	23	42	16	15

4. iteration 4
i	3
j	2
temp	42
4	8	23	42	16	15






5. iteration 5
i	4
j	3
temp	16
4	8	23	42	42	15

------
i	4
j	1
temp	16


-----
i	5
j	4
temp	15


0	1	2	3	4	5
4	8	16	16	23	42

******
i	5
j	1
temp	15
4	8	15	16	23	42

