#Ar 5.1.3

#Prob 1

squares = []
for x in range(10):
		squares.append(x**2)
squares	

#Prob 1.1

squares = list(map(lambda x: x**2,range(10)))
squares

#Prob 1.2

squares = [x**2 for x in range(10)]
squares

#Prob 2
[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

[(x,y) for x in [2,5,6,3] for y in [4,3,6,5] if x != y]

[(x,y) for x in [2,5,6,3] for y in [4,3,6,5] if x == y]

#Prob 2.1

combs = []
for x in [1,2,3]
	for y in [3,1,4]
		if x != y:
			combs.append((x,y))
combs

#Prob 3

 vec = [-4,-2,0,2,4]
 [x*2 for x in vec]

#Prob 3.1

vec = [-4,-2,0,2,4]
[x for x in vec if x >= 0]

#Prob 3.2

vec = [-4,-2,0,2,4]
[abs(x) for x in vec]

#Prob 4

freshfruit = [' banana', ' loganberry ', 'passion fruit ']
[x.strip() for x in freshfruit]

#Prob 2.2

[(x, x**2) for x in range(6)]

#Prob 5 flatten an array in array

vec = [[1,2,3], [4,5,6], [7,8,9]]
[y for x in vec for y in x]

#Prob 5.1
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

#Prob 5.2
num = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 1, 9], [4, 9, 3, 6, 8, 3]]
num
num[0][3]
num[2][2]
num[1][4]
num[2][4]
num[0][0]

#Prob 6

from math import pi 
[str(round(pi,i)) for i in range(1,6)]

#Prob 7

matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]

[[row[i] for row in matrix] for i in range(4)]

#Prob 7.1
matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]
transposed = []
for i in range(4):
	transposed.append([row[i] for row in matrix])

transposed

#Prob 7.2

transposed = []
for i in range(4):
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)
	
transposed





