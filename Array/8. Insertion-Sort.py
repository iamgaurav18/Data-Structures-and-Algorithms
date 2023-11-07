#Insertion Sort
import array

def InsertionSort(arr):
    l=len(arr)                      # to get the length of the array
    for i in range(1,l):
        count=0                     # a count variable to reduce the value of i variable in second loop to keep trailing j
        for j in range(i-1,-1,-1):
            if(arr[j]>arr[i-count]):
                arr[j],arr[i-count]=arr[i-count],arr[j]    # here insertion is performed of smaller value to its right position
            count=count+1
    return arr

a=array.array("i",[5,2,6,1,7,3])
res=InsertionSort(a)
print(res)
