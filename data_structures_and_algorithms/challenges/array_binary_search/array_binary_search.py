"""
function called BinarySearch which takes in 2 parameters: a sorted array and the search key.
that return the index of the array’s element that is equal to the search key,
 or -1 if the element does not exist

"""
def binary(arr, low, high, x): 
  
    if high >= low: 
  
        mid = (high + low) // 2
  
        if arr[mid] == x: 
            return mid 
   
        elif arr[mid] > x: 
            return binary(arr, low, mid - 1, x) 
  
        else: 
            return binary(arr, mid + 1, high, x) 
  
    else: 
        return -1



if __name__ == "__main__":
    arr = [ 5,15,25,35,45,55,65,75,85] 
    x = 45
    
    result = binary(arr, 0, len(arr)-1, x) 
    
    if result != -1: 
        print(str(result)) 
    else: 
        print("Element Not Found")