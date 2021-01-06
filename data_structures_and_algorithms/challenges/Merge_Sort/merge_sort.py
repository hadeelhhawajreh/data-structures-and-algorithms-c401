# ```
# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length
           
#     if n > 1
#       DECLARE mid <-- n/2
#       DECLARE left <-- arr[0...mid]
#       DECLARE right <-- arr[mid...n]
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
#     DECLARE j <-- 0
#     DECLARE k <-- 0

#     while i < left.length && j < right.length
#         if left[i] <= right[j]
#             arr[k] <-- left[i]
#             i <-- i + 1
#         else
#             arr[k] <-- right[j]
#             j <-- j + 1
            
#         k <-- k + 1

#     if i = left.length
#        set remaining entries in arr to remaining values in right
#     else
#        set remaining entries in arr to remaining values in left

# ```
# i                j
# Left array        Right arry 
#  new array merge sort index=k
def mergeSort(arr):
    new=[]
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        new =arr
    return new
 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(mergeSort(arr))
