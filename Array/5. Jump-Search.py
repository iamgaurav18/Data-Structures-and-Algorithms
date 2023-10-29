#THis approach also requires the array to be sorted. in this approach we will skip a fixed number of elemnts and compare the upccoming value with the key element, untill we find the element or and element greater than this element. if the element we jumped to is greater than then we will perform linear short from last jumped element to current element.

import array
import math

def JumpSearch(arr,k):
    l=len(arr)
    j=int(math.sqrt(l))
    i,r,c,m=0,0,0,0
    while(i<l):
        if(arr[i]==k):
            return i
        elif(i+j<l):
            if(arr[i+j]<k):
                m=i
                i=i+j
            else:
                for a in range(i+1,i+j):
                    if(arr[a]==k):
                        c=1
                        return a
                if(c!=1):
                    return -1  
        else:
            for a in range(i+1,i+j):
                    if(arr[a]==k):
                        c=1
                        return a
            if(c!=1):
                return -1       

print(JumpSearch([0,1,2,3,4,5,6,7,8,9,10,11],12))       