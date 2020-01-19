# 12.1.2020
# 8.3 Handling exceptions

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(x)
#         break

#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# 19.1.2020
import sys
import time # For delay, sleep

f = None 
try:
	f = open("poem.txt")

	#Our usual file reading idiom

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line,end='') # spacebar
		sys.stdout.flush()
		print("Press Ctrl+C now")

		# To make sure it runs for a while

		time.sleep(10) #stop for a while
except IOError:
		print("Could not find file poem.txt")

except KeyboardInterrupt:
		print("!! You cancelled the reading from thr file.")

finally:
	if f:
		f.close() # Close the file
	print("(Cleaning up : Closed the file)")

