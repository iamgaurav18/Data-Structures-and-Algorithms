# In this approach we go through each and every element one by one to find the the element
import array

def LinearSearch(arr, value):
    for i in range(len(arr)):
        if(arr[i]==value):
            return i
    return -1

s=int(input("Enter the size of the array : "))
l=[]
for j in range(s):
    l.append(int(input(f"Enter value {j}:")))
a=array.array("i",l)

m=int(input("Enter a value to be searched: "))

l=LinearSearch(a,m)
if(l!=-1):
    print(f"Searched avlue is at {l} position in the array")
else:
    print("Element not found")

# Best case time Complexity: O(1)
# Worst case time Complexity: O(N)
# Average case time Complexity: O(N)