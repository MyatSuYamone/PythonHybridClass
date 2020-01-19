# 5.1.2020

# 9.2.1
--------------------------------------------------
def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:",spam)
	do_nonlocal()
	print("After nonlocal assignment:",spam)
	do_global()
	print("After global assignment:",spam)

scope_test()
print("In global scope:", spam)
-----------------------------------------------------

#Functions
def say_hello():
	print('Hello World')

say_hello()

-------------------------------------------------------
#Function parameters
a = input('Please enter value of a: ')
b = input('Please enter value of b: ')
def print_max(a,b):
	if a > b:
		print(a, "is maximum")
	elif a == b:
		print(a, "is equal to".b)
	else:
		print(b, "is maximum.")

print_max(a, b)
--------------------------------------------------------

print_max(3, 4)
print_max(2, 5)
print_max(0.9, 10)
---------------------------------------------------------
x = 8
y = 10
print_max(x, y)
---------------------------------------------------------
print(20 > 10)
ptint(20 == 10)
print (20 < 10)
print(bool("Hello World"))
print(bool(20))

--------------------------------------------------------
Python Conditions

Equals                     -> x == y
NOt Equals                 -> x != y
Less than                  -> x < y
Less than or Equal to      -> x <= y
Greater than               -> x > y
Greatre than or equal to   -> x >= y
-----------------------------------------------------------
# local variables

def func(x):
	print('x is', x)
print('x is still', x)


x = 10
func(x)
print('x is still', x)

# ---------------------------------------
def func(y):
	print('y is', y)
	y = 50
	print('Changed local y to', y)

def funx(y):
	print('y is', y)
	y = x + y
	print('y is changed to x + y', y)

x = 40
y = 20
func(y)
funx(y)
print('y is still', y)
# -----------------------------------------

# Global statement

def func():  no parameter needed to enter
	global x

	print('x is', x)
	x = 2
	print('Changed global x to', x)

x = 50
func()
print('Value of x is:', x)

# -------------------------------------------

# eg

def func():
	global y
	print('y is', y)

	y = 100
	print('Value of y is', y)

y = 15
func()
print('Value of y:', y)

# -------------------------------------------------------
def do_global():
		global spam
		spam = "global spam"

spam = "test spam"
do_global()
	print("After global assignment:",spam)

--------------------------------------------------------

# eg
def func():
	nonlocal x
	print('x is', x)

	x = 5
	print('Value of x is:', x)

x = 10
func()
print('Real value of x is:', x)

---------------------------------------------------------

def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	spam = "test spam"
	do_local()
	print("After local assignment:",spam)

	do_nonlocal()
	print("After nonlocal assignment:",spam)
	
scope_test()
--------------------------------------------------------------