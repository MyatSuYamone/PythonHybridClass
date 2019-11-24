#Program 1

def fib(n):
	"""Print a Fibonacci series up to n."""

	a, b = 0, 1 
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

fib(500)


#Program 2
def fib2(n):

	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

fib2(500)


