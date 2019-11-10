#Program 1

x = int(input("Please enter an integer: "))
	#This is user input.

if x < 0:
	x = 0
	print('Neagative chhanged to zero')
elif x == 0:
	print('Zero')	
elif x == 1:
	print('Single')	
else:
	print('More')	

	
#Program 2

x = int(input("Please enter an integer: "))

if x < 5:
		x = 0
		print('x is smaller than 5')
elif x > 10:
		print('x is greater than 10')
elif x == 7:
		print('x is equal to 7')
elif x > 5 and x < 10:
		print ('x is between 5 & 10')
else:
		print('x is undefined')

#Program 3

x = int(input("Please enter the age of the people: "))

if x >= 1 and x <= 18:	
	print('"To school"')
elif x >= 19 and x <= 50:
	print('To beach')
elif x >= 51 and x <= 75:
	print('To monastery')
else:
	print('To somewhere they prefer')

#Program 4	

print('"I told that "I dont like it".')

#Measure some strings:

#Program 5

words = ['cat','window','defenestrate']
for w in words:
	print(w,len(w))

fruits = ['apple', 'banana', 'pinapple' , 'cucumber', 'orange']
for f in fruits:
	print(f,len(f))

#Program 6

for i in range (5):
	print(i)

#Program 7

for x in range (0, 10):
	print(x)

for i in range(-4,10):
	print(i)


#Program 8

a = ['1','2','3','4','5']
for c in range(len(a)):
	print(c,a[c])

#Program 9

list(range(4))

#Program 10

fruits = ['apple', 'banana', 'pinapple' , 'cucumber', 'orange']
fruits.append('grape')


#Program 11

fruits = ['apple', 'banana', 'pinapple' , 'cucumber', 'orange','banana']
fruit
