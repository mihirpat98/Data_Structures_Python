# Arrays, also called Stacks
# Array/Stack
# FIFO
# That is, an item can be inserted and removed from a stack, but an item can only be removed from the stack after all the items added after it are removed first.
# Used in recursion

# Initializes the stack
stack = []
# Pushing 5 into the stack
stack.append(5)
# Look at the top item of the stack and print it
print(stack[-1])
# Removing the top item from the stack
stack.pop()

strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push  
strings.append('e')      # O(1)

#pop  
strings.pop() 
strings.pop()            # O(1)

#addfirstelement 
strings.insert(0,'x')    #O(n)

#splice
strings.insert(2,'alien')   #O(n)

print(strings)

arr = [0,1,2,3,4,5]

print(arr[3]) # prints 4th(3 position) of the array

print(arr[-1]) # prints last element of array


arr.pop(0) # removes the first element

first = arr.pop(0)# removes first element as well as assigns the popped element to first variable

#remove
arr.remove(4) # removes first occurence of 4 #O(n)

del arr[2:4] # removes the elements from index 2 to 3(3 included) #O(n)




# Array manipulation
arr = [0,1,2,3,4,5]
arr[::1] # returns same array
# [0,1,2,3,4,5]


arr[::2] #returns alternate elements
# [0, 2, 4]

arr[::3] # every third element
# [0, 3]

arr[1::2] # every alternate element from position 1 element
# [1, 3, 5]

arr[:4:2] # every alternate element till  position 4(excluded) element
# [0, 2]

arr[:0:2] 
#[]

arr[::-1] # reverses the array
# [5, 4, 3, 2, 1, 0]

arr[::-2] # reverses the array and selects from the second last element
# [5, 3, 1]


arr.clear() # clears all elements. arr = []



arr2 = arr.copy() # makes a duplicate list


arr.count(4) # counts how many 4s are present in the array


arr.insert(4,1) # adds 4 to 1st position.
#Array native python methods :-
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#array.sorted() Returns sorted list

#List objects are implemented as arrays. 
#They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) 
#operations which change both the size and position of the underlying data representation.

#For in depth information on arrays 
#https://docs.python.org/3/tutorial/datastructures.html

#to implement arrays as a stack 
#https://docs.python.org/3/library/collections.html#collections.deque\


# Implementation of arrays:

class Array:
  def __init__(self):
    self.length=0
    self.data={}

  def __str__(self):
    return str(self.__dict__)

  def get(self,index):
    return self.data[index]
  
  def push(self,item):
    self.data[self.length]=item
    self.length+=1

  def pop(self):
    lastitem = self.data[self.length-1]
    del self.data[self.length-1]
    self.length-=1
    return lastitem

  def delete(self,index):
    deleteditem = self.data[index]
    for i in range(index,self.length-1):
      self.data[i] = self.data[i+1]

    del self.data[self.length-1]
    self.length-=1
    return deleteditem

arr=Array()
arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')
arr.delete(3)
print(arr)

