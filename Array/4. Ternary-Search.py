# This approach is similar to Binary search except here instead of one mid we have two mids. here we are dividing the array in three parts instead of two
import array

def TernarySearch(arr,l,r,k):
    print(arr[l:r+1])
    mid1=l+(r-l)//3
    mid2=r-(r-l)//3
    print(f"Mid1 : {mid1} Mid2 : {mid2}")
    if(l<=r):
        if(arr[mid1]==k):
            return mid1
        elif(arr[mid2]==k):
            return mid2
        elif(arr[mid1]>k):
            return TernarySearch(arr,l,mid1-1,k)    # check in first part of array
        elif(arr[mid2]<k):
            return TernarySearch(arr,mid2+1,r,k)    # check in third part of array
        else:
            return TernarySearch(arr,mid1+1,mid2-1,k) # check between mid1 and mid2
    else:
        return -1
    
a=array.array("i",[0,1,2,3,4,5,6,7,8,9])
res=TernarySearch(a,0,9,5)
if(res>=0):
    print(f"Element is found at : {res}")
else:
    print("Element not found")

# Best case time Complexity: O(1)
# Worst case time Complexity: O(logN base3)
# Average case time Complexity: O(logN base3)