 ```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

 ```

1. the array is  [12, 11, 13, 5, 6, 7]
and it will divied into 
mid =n//2
mid=6//2=3

    left        right 
[12, 11, 13]     [5, 6, 7]


and diveded the left  sub array
  left        right 
[12]            [11, 13]     

and diveded the right of the left  sub array
  left        right 
[11]            [ 13] 

and diveded the right  sub array
  left        right 
[5]            [6, 7]   

and diveded the rigth  of the right  sub array
  left        right 
[6]            [ 6]



1.        [12, 11, 13, 5, 6, 7  ]
        /                         \
2.   [12, 11, 13]                  [5, 6, 7]

        /      \                    /       \
    
3.   [12]        [ 11, 13]]        [5]       [6,7]   

and will each level  the array of the ,and will return sorted array
4. in the level 3 the left side compare  [11,12,13]
5. and the right side  [5,6,7]
6. and compare the left and right [11,12,13]  [5,6,7] and the final output [5,6,7,11,12,13]

