
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


#Decorators with arguments

#creating decoreator
def repeat(n):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for _ in range(n):
				func(*args, **kwargs)
		return wrapper
	return decorator

#function to use that decorator
@repeat(5)
def say_hello(name):
	print(f'Hello {name}')


say_hello()





#reverse a string with slicing
@timer
def reverse_str():	
	string = input("Enter string to reverse with slicing  - ")
	rev_str = string[::-1]
	print("reverse_str : ",rev_str)




#reverse a string without slicing
@timer
def reverse_str_ws():	
	string = input("Enter string to reverse using for loop - ")
	
	result = ''
	for i in string:
		result = i + result
	
	print("reverse_str : ",result)



#reverse a string with reversed and join
@timer
def reverse_str_rj():	
	string = input("Enter string to reverse using .join and reversed - ")
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
	string = input("Enter string to reverse using recurssion - ")
	reverse = recursive_rr(string)

	print(reverse)



#reverse a string with while loop
@timer
def reverse_str_wh():
	string = input("Enter String to reverse using while loop - ")
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

	j = int(input("Enter Number Of Elements In The List to find duplicate - "))

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
	print("Displays the example of generator")
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
	n = int(input("Enter the range to find the squares using general expression (generator) - "))
	ge = (x * x for x in range(1, n+1)) #this is a generator expression where it is expressed in()

	print(ge, " - Generator expression\n") #output - <generator object gen_exp.<locals>.<genexpr> at 0x00000273419D6490>  - Generator expression

	#to print the generated values
	print(next(ge), " - Generator expression") #output - 1  - Generator expression
	print(next(ge), " - Generator expression \n") #output - 4  - Generator expression

	print("Generator expression remaining")
	for x in ge:
		print(x) #this will print the remaining values in the generator expression

	lc =  [x * x for x in range(1, n+1)] #if same is done in square brackets it is list list comprehension

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
	print("Banking operations using class - \n")
	acc = Bank("Faraz", 15000)
	acc.deposit(5000)
	acc.withdraw(30000)
	acc.withdraw(15000)


#difference between classmethod and staticmethod
class MyClass:
	@classmethod
	def class_method(cls):
		print("This is a class method.")
		print(f"Class name: {cls.__name__}")

	@staticmethod
	def static_method():
		print("This is a static method.")
		print("Static methods do not have access to the class or instance.")
		print(f"Class name: {cls.__name__}" if 'cls' in locals() else "No class context available")

def class_static_methods():
	MyClass.class_method()  # Calling class method
	MyClass.static_method()  # Calling static method
	print("\n")


#difference between shallow and deep copy
import copy

@timer
def shallow_copy_slice():
	print("Shallow copy using slicing and list()")
	a = [1, 2, 3]
	b = a[:]    # new list with same elements
	c = list(a) # also creates a new list

	a[0] = 99
	print(a, " original")  # [99, 2, 3]
	print(b, " new list with same elements using slicing")  # [1, 2, 3]
	print(c, " new list with same elements using list")  # [1, 2, 3]

	
# The shallow copy will copy the outer list, but the inner list will still refer to the same object.

@timer
def shallow_deep_copy():
	a = [[1, 2], [3, 4]]
	b = copy.copy(a)       # shallow copy
	c = copy.deepcopy(a)   # deep copy

	a[0][0] = 99

	print(a, " originial")  # [[99, 2], [3, 4]]
	print(b, " (changed! still linked inside)")  # [[99, 2], [3, 4]]  (changed! still linked inside)
	print(c, " (independent)")  # [[1, 2], [3, 4]]   (independent)
	
#DSA With Python 

#Stack implementation


class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)
		return f"Item {item} pushed to stack."
	def pop(self):
		if not self.items:
			return "Stack is empty."
		return f"Item {self.items.pop()} popped from stack."
@timer
def stack_operations():
	print("Stack operations - \n")
	s = Stack()
	print(s.push(1))  # Item 1 pushed to stack.
	print(s.push(2))  # Item 2 pushed to stack.
	print(s.pop())    # Item 2 popped from stack.

	print(s.items, "\n")


#Queue implementation
class Queue:
	def __init__(self):
		self.items = []
	
	def enqueue(self, item):
		self.items.append(item)
		return f"Item {item} added to queue."
	
	def dequeue(self):
		if not self.items:
			return "Queue is empty."
		return f"Item {self.items.pop(0)} removed from queue."
@timer
def queue_operations():
	print("Queue operations - \n")
	q = Queue()
	print(q.enqueue(1))  # Item 1 added to queue.
	print(q.enqueue(2))  # Item 2 added to queue.
	print(q.dequeue())   # Item 1 removed from queue.

	print(q.items, "\n")


#Linked List implementation
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	
	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node
	
	def display(self):
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print("None")
@timer
def linked_list_operations():
	print("Linked List operations - \n")
	ll = LinkedList()
	ll.append(1)
	ll.append(2)
	ll.append(3)
	ll.display()  # 1 -> 2 -> 3 -> None
	print("\n")


#First non-repeating character
@timer
def non_repeating_char():
	s = input("Enter the string to find non repeating char - ")
	char_count = {}
	for char in s:
		char_count[char] = char_count.get(char, 0) + 1

	print(char_count)
	
	for char in s:
		if char_count[char] == 1:
			print(f"First non-repeating character is: {char}")
			return f"First non-repeating character is: {char}"
	return None

#Sort list of dicts by multiple keys
@timer
def sort_list_of_dicts():
	print("Sorting list of dicts by multiple keys - \n")
	data = [
		{'name': 'Alice', 'age': 30, 'city': 'New York'},
		{'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
		{'name': 'Charlie', 'age': 30, 'city': 'Los Angeles'},
		{'name': 'David', 'age': 25, 'city': 'New York'}
	]

	sorted_data = sorted(data, key=lambda x: (x['name'], x['age'], x['city'])) #first preference to name alphabetically, then age, then city
	print("Sorted Data:", sorted_data)


#Find missing number in array [1..n]
@timer
def missing_number(nums):
	print("Finding the missing number form array - \n")
	n = len(nums) + 1
	expected_sum = n * (n + 1) // 2
	print("Expected number:", expected_sum - sum(nums))
	

# missing_number([1,2,4,5])  # 3


#fimd if it is pallindrome
def is_palindrome():
	s = input("Enter the string for pallindrome - ")
	if s == s[::-1]:
		print(f"{s} is a palindrome")
		return True
	else:
		print(f"{s} is not a palindrome")
		return False



#main function to call all the functions
def main():
	reverse_str()
	reverse_str_ws()
	reverse_str_rj()
	reverse_str_rr()
	reverse_str_wh()
	find_dupli([1, 2, 3, 4, 5, 1, 2])
	find_dupli2()
	print_gen_once()
	print_gen_for()
	print(list(fibonacci(7)))
	gen_exp()
	banking()
	class_static_methods()
	shallow_copy_slice()
	shallow_deep_copy()
	stack_operations()
	queue_operations()
	linked_list_operations()
	non_repeating_char()
	sort_list_of_dicts()
	missing_number([1,2,4,5])
	is_palindrome()


# if __name__ == "__main__":
# 	main()
# This code is designed to be run as a script, and it will execute the main function when run directly.
	 


	 







