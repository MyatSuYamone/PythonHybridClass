# Ar 5.2

#Prob 1

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0] # delete number at index 0 in a
a

del a[2:4] # delete number from index 2 to 3 in a
a 

del a[:] # delete all numbers in a
a

# Prob 2 HW Ar. 5.3

t = 12345, 54321, 'hello!'
t
t[0]

u = t, (1, 2, 3, 4, 5)
u

t = 1, (2, 3, 4, 5, 6, 7, 8, 9, 10)
u = t, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

u
u[0]

v = ([1, 2, 3], [3, 2, 1])
x = ([5, 6, 7], [8, 5, 9])
z = v + x
z

z[0]

# Prob 3

empty = ()
singleton = 'hello', # beaware of comma
len(empty)
len(singleton)

# Prob 4 Ar. 5.4

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'} # This is Sets
print(basket)

'orange' in basket # fast membership testing
'grass' in basket


a = set('mamawawahtahtaka')
a
 
b = set('kokoaungaungkyikyikyukyu')
b

a - b # letters in a but not b
a | b # letters in a or b or both
a & b # letters in both a and b
a ^ b # (caret) letters in a or b but not both

b - a
b | a
b & a
b ^ a

c = set('1234567')
c - b - a

# Prob 5

a = {x for x in 'mgmgmamamyamyaayeaye' if x not in 'agye'}
a

a = {x for x in 'mgmgmamamyamyaayeaye' if x not in 'agyem'}
a

a = {x for x in ' mgmgmamamyamyaayeaye' if x not in 'agyem'}
a

