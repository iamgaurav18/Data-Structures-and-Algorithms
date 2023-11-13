#Bubble Sort
import array

def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

a=array.array("i",[12,23,1,3,35,9,34,6,56,8])
a=BubbleSort(a)
print(a)

# this approach is very straight forward, here we are comparing the very next element and if it is greater than the current element we are swapping it. so in every iteration of first loop the subsequent highest element will get sorted and swapped at the end.

# Time Complexity : O(N^2)
