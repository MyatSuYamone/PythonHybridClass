#Chapter 5 
#Ar 5.1

#1
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('pineapple') # inserting an item at the end of the list(fruits)
fruits.append('mango')
fruits

#2
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'mango']
add = ['cherry','berry']
fruits.extend(add) #appending all item from add to the list
fruits

#3
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'mango', 'cherry', 'berry']
fruits.insert(1,'durian') #inserting an item at a defined postion
fruits

#4
fruits = ['orange', 'durian', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'mango', 'cherry', 'berry']
fruits.remove('durian')

#5
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'mango', 'cherry', 'berry']
fruits.pop(2) #removing an item of defined index(2)
fruits

#6
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple', 'banana', 'pineapple', 'mango', 'cherry', 'berry']
fruits.pop() #removing am item at the end of the list
fruits

#7
fruits.clear() #removing all item from the list

#8
fruits =  ['orange', 'apple', 'banana', 'apple']
fruits.index('apple') #finding the positin of an item in the list
fruits.index('apple', 2) # **finding another index of apple starting from position 2 **

#9
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') #finding how many times an item include in the list

#10
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort() #sorting the same items
fruits

#11
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']
fruits.reverse()
fruits

## example

stack = [-1, 0, 1, 2, 3]
stack.append(4)

add = [5,6]
stack.extend(add)
stack.insert(2, 7) #insert 7 in index 2

stack = [-1, 0, 7, 1, 2, 3, 4, 5, 6]

stack.remove(6)
stack.pop(2) #removing 7 from index 2
stack.pop()

stack = [-1, 0, 1, 2, 3, 4]
stack.reverse()
stack.clear()

stack = [1, 2, 3, 0, 1, 3, 4, 4, 3]
stack.count(3)

stack.index(3)
stack.index(3, 6)


