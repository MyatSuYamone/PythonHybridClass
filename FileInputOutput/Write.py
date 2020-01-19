#19.1.2020

with open('test.txt', 'r') as rf:
	with open('testCOPY.txt', 'w') as wf:

		for line in rf:
			wf.write(line)

# with open('cat.jpg', 'rb') as rf: # rf = readfile
# 	with open('cat_copy.jpg', 'wb') as wf: # wf = writefile

# 		for line in rf:
# 			wf.write(line)