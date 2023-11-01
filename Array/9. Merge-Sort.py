import array

def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2              # Finding the mid of the array
        L = arr[:mid]                  # Dividing the array elements         
        R = arr[mid:]                  # Into 2 halves
         
        MergeSort(L)                   # Sorting the first half
        MergeSort(R)                   # Sorting the second half
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

a=array.array("i",[1,7,2,9,5,2,8,4,6])
MergeSort(a)
print(a)