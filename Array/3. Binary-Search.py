# this approach will only work if the array is sorted. here we select a mid element (mid=low+(high-low)/2) and compare our key in the left or side side of this mid index. this process is done recursively until we find our desired element

import array

def BinarySearch(arr,l,r,k):
    print(arr[l:r+1])
    mid=l+((r-l)//2)
    print(f"Mid : {mid}")
    if(l<=r):
        if(arr[mid]==k):
            return mid
        elif(arr[mid]<k):
            return BinarySearch(arr,mid+1,r,k)
        elif(arr[mid]>k):
            return BinarySearch(arr,l,mid-1,k)
    else:
        return -1

a=array.array("i",[0,1,2,3,4,5,6,7,8,9])
res=BinarySearch(a,0,9,10)
if(res>=0):
    print(f"Element is found at : {res}")
else:
    print("Element not found")

# Best case time Complexity: O(1)
# Worst case time Complexity: O(logN)
# Average case time Complexity: O(logN)