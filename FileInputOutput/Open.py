# # 19.1.2020

# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

# open & Read File
# ------------------------------------------
# f = open('test.txt', 'r') # r - Read
# print(f.name)
# f.close()
# -------------------------------------------
# filenames = ['test.txt', 'test1.txt']
# with open('filenames', 'r') as f:
# 	for f in filenames:
# 		print(f.name)
# 		f.close()
# ---------------------------------------------
# with open('test1.txt','a') as g:

# 	g.write('This is line number '+"\n")

# 	print(g, end='')

#-----------------------------------------------

with open('test.txt','r') as f:

# 	f_text = f.readline()
# 	print(f_text, end='')

# 	f_text = f.readline()
# 	print(f_text, end='')

# 	f_text = f.readline()
# 	print(f_text, end='')

# ---------------------------------------------

	# for f_text in f:
	# 	print(f_text, end='')

#----------------------------------------------

	# f_text = f.read(60)
	# print(f_text,end='')

#----------------------------------------------

	size_to_read = 100
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text,end='')