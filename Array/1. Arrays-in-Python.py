import array          # importing the array module

arr=array.array('i',[1,2,3,4,5,6])      # this will create and array object of signed integer ('i') and assign values to it
print(arr)                              # array('i', [1, 2, 3, 4, 5, 6])

# this array will only have signed integer values in it
# we can parse the array similar to list
for i in arr:
    print(i)

for i in range(len(arr)):
    print(arr[i])

arr.append(7)       # this will insert the value at the end of the array
print(arr)

arr.insert(3,10)    # this will insert the 10 in index 3 in the array
print(arr)

arr.pop()           # this will remove one element from the last of the array, and return that popped value
print(arr)          # if you specify the position the index it will remove lement from that index  arr.pop(3)

arr.remove(10)      # this will remove the first occurance of the element
print(arr)

print(arr.index(3)) # this will return the index of first occurance of the value

arr.reverse()
print(arr) # this will return the reverse of array