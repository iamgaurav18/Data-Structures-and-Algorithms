import array

def MergeSort(arr):
    if(len(arr)>1):
        mid=len(arr)//2      # to find the middle index of the array
        L=arr[:mid]
        R=arr[mid:]
        MergeSort(L)    # to sort the left half array
        MergeSort(R)    # to sort the right half array

        i=j=k=0
        while(i<len(L) and j<len(R)):     # to merge the arrays upto the length of smaller array 
            if(L[i]<=R[j]):
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=R[j]
                j=j+1
            k+=1
            
        while(i<len(L)):       # to merge any remaining elements in left array
            arr[k]=L[i]
            i+=1
            k=k+1
        while(j<len(R)):      # to merge any remaining elements in right array
            arr[k]=R[j]
            j+=1
            k+=1

a=array.array("i",[1,7,2,9,5,2,8,4,6])
MergeSort(a)
print(a)