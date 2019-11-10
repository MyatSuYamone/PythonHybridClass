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

	
#Program 1 sample 1
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

#Program 1 sample 2
x = int(input("Please enter the age of the people: "))

if x >= 1 and x <= 18:	
	print('"To school"')
elif x >= 19 and x <= 50:
	print('To beach')
elif x >= 51 and x <= 75:
	print('To monastery')
else:
	print('To somewhere they prefer')

#Program 2

print('"I told that "I dont like it".')

#Measure some strings:
#Program 3

words = ['cat','window','defenestrate']
for w in words:
	print(w,len(w))

#Program 3 sample 1
fruits = ['apple', 'banana', 'pinapple' , 'cucumber', 'orange']
for f in fruits:
	print(f,len(f))

#Program 3 sample 2
fruits = ['apple', 'banana', 'pinapple' , 'cucumber', 'orange']
for x in fruits:
	print(x,len(x))

#Program 4

for i in range(5):
	print(i)

#Program 5

for x in range(0, 10):
	print(x)

#Program 5 sample
for i in range(-4,10):
	print(i)


#Program 6

a = ['1','2','3','4','5']
for c in range(len(a)):
	print(c,a[c])

#Program 6 sample
words = ['dog','cat','horse']
for y in range(len(words))
	print(y,words[y])

#Program 7

list(range(4))

#Program 8

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.count('pineapple')
fruits.count('banana')
fruits.count('apple')

#Program 8.1

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.index('pineapple')
fruits.index('pear')
fruits.index('banana')
fruits.index('banana',2)
fruits.index('apple',1)

#Program 8.2

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.reverse()
fruits

#Program 8.3

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.sort()
fruits

#Program 8.4

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.append('durian')
fruits

fruits.append('strawberry')
fruits.append('cherry')
fruits

#Program 8.5

fruits = ['apple', 'banana', 'pinapple' , 'pear', 'orange','apple','banana','apple']
fruits.pop()
fruits





