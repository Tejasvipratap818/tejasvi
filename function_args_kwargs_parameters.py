#1. 

'''
Write a function calculate_total that calculates the total price of an order with the following conditions:

The function should take the following parameters:
price (required) – the price of a single item.
quantity (default value: 1) – number of items purchased.
discount (default value: 0%) – percentage discount applied to the total price.
tax (default value: 5%) – tax applied after the discount.
The function should return the final price after applying the discount and tax.

Example Calls

print(calculate_total(100))  # Uses default quantity, discount, and tax  
print(calculate_total(100, 2, tax=10))  # Overrides quantity and tax  
print(calculate_total(price=200, quantity=3, discount=10, tax=8))  

'''

#2. 

'''
*args contains a list of food items ordered.
**kwargs contains additional details such as:
table_number (default: 1)
waiter_name (default: "Unknown")
The function should print the ordered items, the table number, and the waiter's name.
Example Calls

order_summary("Burger", "Pizza", "Pasta", table_number=5, waiter_name="John")  
order_summary("Sushi", "Ramen", waiter_name="Lisa")  
What is the output for these function calls?

'''

#3. 

'''
You have a global variable counter = 0.

Write a function increment_counter() that:
Uses the global keyword to modify counter.
Increases counter by 5 on each function call.
Returns the updated value.
Call the function three times and print the value of counter after each call.
Example Output

increment_counter()  # 5  
increment_counter()  # 10  
increment_counter()  # 15  
What is the final value of counter?
'''

#4. 

'''
Write a function outer() that has:

A nested function inner() that modifies a variable using nonlocal.
A variable x = 10 inside outer().
The inner() function should:
Increase x by 5 using nonlocal.
Print "Inside inner: x = <value>".
The outer() function should:
Call inner().
Print "Inside outer: x = <value>".
Example Call

outer()
What is the final value of x inside outer() after calling inner()?
'''

#5. 

'''
Write a function process_data() that:

Accepts positional arguments (*args) representing numbers.
Accepts keyword arguments (**kwargs) with options:
operation="sum" (default) → Returns the sum of all numbers.
operation="product" → Returns the product of all numbers.
operation="max" → Returns the maximum number.
Uses a global variable result to store the final value.
Uses a nested function modify_result() that:
Uses nonlocal to modify result.
Doubles result if a keyword argument double=True is passed.
Returns result.
Example Calls

print(process_data(1, 2, 3, 4, operation="sum", double=True))  
print(process_data(5, 6, 7, 8, operation="product"))  
print(process_data(10, 20, 30, operation="max", double=True))
'''