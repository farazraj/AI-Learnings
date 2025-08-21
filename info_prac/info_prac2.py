
#to create a decorater which logs execution times
import time
def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(f"\n{func.__name__} took {end - start:.5f} sec to execute.")
		return result
	return wrapper



#reverse a string with slicing
@timer
def reverse_str():	
	string = input("Enter string -")
	rev_str = string[::-1]
	print("reverse_str : ",rev_str)




#reverse a string with slicing
@timer
def reverse_str_ws():	
	string = input("Enter string - ")
	
	result = ''
	for i in string:
		result = i + result
	
	print("reverse_str : ",result)



#reverse a string with reversed and join
@timer
def reverse_str_rj():	
	string = input("Enter string -")
	rev_str = ''.join(reversed(string))
	print("reverse_str : ",rev_str)



#reverse a string with reversed recursive
def recursive_rr(s):

	if len(s) == 0:
		return s
	else:
		return recursive_rr(s[1:]) + s[0]

@timer
def reverse_str_rr():
	string = input("Enter string - ")
	reverse = recursive_rr(string)

	print(reverse)



#reverse a string with while loop
@timer
def reverse_str_wh():
	string = input("Enter String - ")
	reverse_string = ""
	index = len(string) - 1
	while index >= 0:
		print("looped")
		reverse_string += string[index]
		index -= 1
	print(reverse_string)




#to find duplicates in a list of numbers
@timer
def find_dupli(nums):

	seen = set()
	dupli = set()

	for n in nums:
		if n in seen:
			dupli.add(n)
		else:
			seen.add(n)

	print("Duplicates - ",dupli)




#to take list inputs from user and find duplicates in a list of numbers
@timer
def find_dupli2():

	#to enter the list elements
	nums = []

	j = int(input("Enter Number Of Elements In The List - "))

	for i in range(j):
		e = input(f"Enter Element {i+1} - ")
		nums.append(e)

	#to find the duplicate
	seen = set()
	dupli = set()

	for n in nums:
		if n in seen:
			dupli.add(n)
		else:
			seen.add(n)

	print("Duplicates - ",dupli)



#example of generator
@timer
def count_upto(n):
	i = 0
	while i <= n:
		yield i # this will memorise the result and will only give that result when called with next()

		i += 1

def print_gen_once():
	c = count_upto(5)

	print(c) #this only gave count_upto took 0.00000 sec to execute. <generator object count_upto at 0x000001609B336420>

	print("\n\n") # to print 2 blank lines

	#to print the generator object you need next() to print the next result, which will only give one object

	print(next(c)) #this gave 0 as an output when run at first.
	print(next(c)) #this run will give 1 the next output.


def print_gen_for():

	#to show the result with single print and then with for loop

	c = count_upto(10)

	print(next(c), " - single output") #this gave 0 as an output when run at first.
	print(next(c), " - single output") #this run will give 1 the next output.

	print("\nnow for loop - \n")

	for num in c:
		print (num) #this will give all the next result


#fibbonaci series using generator
@timer
def fibonacci(n):
    a = 0 
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# print(list(fibonacci(7))) #to call the fibonacci and display as a list



#generater expression -  a generator can be created with parenthesis witout yield but work as a yield
def gen_exp():
	n = int(input("Enter the range - "))
	ge = (x * x for x in range(1, n+1)) #this is a generator expression where it is expressed in()

	lc =  [x * x for x in range(1, n+1)] #if same is done in square brackets it is list list comprehension

	print(ge, " - Generator expression\n") #output - <generator object gen_exp.<locals>.<genexpr> at 0x00000273419D6490>  - Generator expression

	print(lc, " - List Comprehension ") #output - [1, 4, 9, 16, 25]  - List Comprehension


#OOPS concept banking system using a class

class Bank:
	def __init__(self, owner, balance = 0):
		self.owner = owner
		self.balance = balance

		print("Owner - ", self.owner)
		print("Balance - ",self.balance)


	def deposit(self, amount):
		self.balance += amount
		print("Amount Deposited - ", amount)
		print("Available Balance - ",self.balance)

		return self.balance


	def withdraw(self, amount):
		if amount > self.balance:
			print(f"Insufficient balance to withdraw {amount}")
			print("Available Balance - ",self.balance)
			return "Insufficient balance"
		self.balance -= amount

		print("Amount Withdrawn - ",amount)
		print("Remaining Balance - ", self.balance)

		return self.balance


def banking():
	 acc = Bank("Faraz", 15000)

	 acc.deposit(5000)

	 acc.withdraw(30000)

	 acc.withdraw(15000)
	 


	 







