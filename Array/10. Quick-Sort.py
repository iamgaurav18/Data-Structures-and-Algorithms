#Quick Sort 
def partition(array, low, high):    
    pivot = array[high]                                 # Choose the rightmost element as pivot    
    i = low - 1                                         # Pointer for greater element 
    
    for j in range(low, high):                          # Traverse through all elements
        if array[j] <= pivot:                           # compare each element with pivot                         
            i = i + 1                                   # If element smaller than pivot is found             
            (array[i], array[j]) = (array[j], array[i]) # swap it with the greater element pointed by i
                                                        # Swapping element at i with element at j
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
 
# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

a=[6,8,4,6,9,4,2,6,9,5,4,0]
quicksort(a,0,len(a)-1)
print(a)
