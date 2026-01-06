#🧩 1. List Manipulation and Matrix Operations

'''
Write a function rotate_matrix(mat) that:
Takes a 3x3 matrix as input.
Rotates it 90 degrees clockwise.
Returns the rotated matrix using list comprehension.'
'''



#🧩 2. Dynamic List Modification

'''
Create a function modify_list that:
Takes a list and:
Inserts "Python" at index 2.
Appends "Rocks".
Extends with another list of your choice.'
Return the modified list.
'''



#🧩 3. List Unpacking and String Joining

'''
Write a function format_names(*args) that:
Accepts multiple names using *args.
Joins them into a comma-separated string.
Returns the formatted string.
✅ Input: format_names('Alice', 'Bob', 'Charlie')
✅ Output: "Alice, Bob, Charlie"'
'''



#🧩 4. Dictionary Manipulation

'''
Given a dictionary of students and marks, write a function to:
Filter students with marks > 75.
Return a list of their names.
✅ Input:

students = {'Alice': 80, 'Bob': 65, 'Charlie': 90}
✅ Output: ['Alice', 'Charlie']'
'''


#🧩 5. Control Flow with Loops

'''
Write a loop that:
Prints all numbers from 1 to 50.
Skips multiples of 5 (using continue).
Stops if the number is 42 (using break).'
'''


#🧩 6. Function with Default Parameters

'''
Write a function calculate_price that:
Takes price, tax=0.05, and discount=0.
Returns the final amount after applying tax and discount.
✅ Input: calculate_price(100, discount=10)
✅ Output: 95.0'
'''



#🧩 **7. Argument Handling with *args and kwargs

'''
Write a function order_summary that:
Accepts item names using *args.
Accepts customer details using **kwargs.
Prints the order summary.
✅ Input:

order_summary('Pizza', 'Burger', name='Alice', address='123 Main St')
✅ Output:'
'
Items: Pizza, Burger
Customer: Alice, Address: 123 Main St'
'''


#🧩 8. Global and Nonlocal Usage

'''
Implement a counter function:
Use nonlocal to track calls within a nested function.
Use global to track total calls globally.'
'''



#🧩 9. Class with Classmethod and Staticmethod

'''
Define a Temperature class:
Instance method: to_celsius(fahrenheit)
Class method: from_kelvin(cls, kelvin)
Static method: is_valid_temp(temp)
✅ Convert temperature across Celsius, Fahrenheit, and Kelvin.'
'''


#🧩 10. Encapsulation and Abstraction

'''
Create a BankAccount class:
Private attribute: _balance
Method to deposit and withdraw.
Abstract method apply_interest() in a base class.'
'''


#🧩 11. Inheritance and Method Overriding

'''
Create a Vehicle class and Car subclass:
Vehicle should have a method move().
Car should override move() to print "Driving".'
'''



#🧩 12. Multiple Inheritance and MRO

'''
Implement classes:
A → prints "Class A"
B(A) → prints "Class B"
C(A) → prints "Class C"
D(B, C) → prints "Class D"
✅ Print the MRO of D.'
'''



#🧩 13. Functional Programming with Map, Filter, Reduce

'''
Write a function using:
map() to square numbers.
filter() to extract even numbers.
reduce() to calculate their sum.
✅ Input: [1, 2, 3, 4, 5]
✅ Output: 20'
'''



#🧩 14. Zip for Data Pairing

'''
Write a function that:
Takes two lists: ['a', 'b', 'c'] and [1, 2, 3]
Uses zip() to combine them into a dictionary.
✅ Output: {'a': 1, 'b': 2, 'c': 3}'
'''



#🧩 15. Generator with Decorators

'''
Implement a generator fibonacci(n) and a decorator:
Decorator: Log the value yielded by the generator.'
'''



#🧩 16. Error Handling with Custom Exceptions

'''
Create a NegativeNumberError exception:
Raise it if a function receives a negative number.
✅ Input: check_positive(-5)
✅ Output: "Negative numbers are not allowed!"'
'''



#🧩 17. Nested Try-Except and Finally

'''
Write a function:
Try: Open a file and read contents.
Handle: FileNotFoundError, PermissionError
Finally: Always close the file.'
'''



#🧩 18. Multi-threading with Locks

'''
Simulate a bank with 3 threads:
Each thread withdraws from a shared account.
Use Lock to avoid race conditions.'
'''



#🧩 19. Multiprocessing for Parallel Execution

'''
Create a function to:
Compute factorial for a list of numbers.
Use multiprocessing.Pool for parallel computation.
✅ Input: [5, 10, 15]
✅ Output: [120, 3628800, 1307674368000]'
'''



#🧩 20. Thread and Process Communication

'''
Implement:
A producer process generating random numbers.
A consumer thread printing the numbers.
Use a shared Queue for communication.'
'''