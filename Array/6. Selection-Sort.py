import array

def SelectionSort(arr):
    for i in range(0,len(arr)-1):        #the first loop is to traverse and find first smallest number
        min=i
        for j in range(i+1,len(arr)):    # this loop is for finding the index of smallest number
            if(arr[min]>arr[j]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]  # this is how swapping can be done without using third variable
    return arr

a=array.array("i",[12,23,1,6,34,7,1,9])
a=SelectionSort(a)
print(a)

# In selection sort in every iteration we try to find the next smallest or largest number and place it next to sorted array(alreay found numbers)

# Time complexity : O(N^2)