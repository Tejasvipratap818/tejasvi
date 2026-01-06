#1. 

'''
Write a Python program that does the following:

Continuously ask the user to enter a number using input() inside a while loop.
If the number is less than or equal to 1, print "Invalid! Enter a positive integer greater than 1" and continue.
Check if the number is prime using a for loop.
If the number is prime, print "Prime number found: <num>" and break the loop.
If the number is not prime, print "Not a prime number. Try again!" and continue the loop.

'''

'''while True:
    x = int(input("Enter the number: "))
    
    if x <= 1:
        print("Invalid! Enter a positive integer greater than 1")
        continue 

    y = False 
    for i in range(2, x):
        if x % i == 0 :
            y= True
            break
    if y == True:
        print("not prime")  
    else:
        print("prime")  
         
           '''   



    


#2. 

'''
numbers = [10, 23, 36, 45, 50, 67, 72, 85, 91]
Write a program that:

Iterates through each number in the list using a for loop.
If the number is divisible by both 2 and 3, print "Divisible by 6: <num>" and continue.
If the number is odd, check:
If the number is greater than 80, print "Large odd number: <num>".
Otherwise, pass (do nothing).
If the number is even but not divisible by 3, print "Even but not multiple of 3: <num>".
'''

'''
numbers = [10, 23, 36, 45, 50, 67, 72, 85, 91]
for i in numbers :
    if i % 2 ==0 & i % 3 == 0 :
        print (i) 
        continue
    elif i % 2 != 0 :
        print("odd number")
    elif i > 80 & i % 2 != 0 :    
        print(i)
        pass
    elif i % 2 == 0 & i % 3 != 0 :
        print(  i)



'''



#3. 

'''
inventory = {
    "Apples": 10,
    "Oranges": 5,
    "Bananas": 8
}
Write a program that:

Runs a while True loop that asks the user to enter a fruit name and quantity to purchase.
If the fruit is not in the inventory, print "Item not available" and continue.
If the entered quantity exceeds stock, print "Insufficient stock" and continue.
If the entered quantity is valid, update the inventory by reducing the stock.
If the stock of any item reaches zero, remove it from the dictionary and print "Out of stock: <fruit>".
If all items are out of stock, print "All items sold out!" and break the loop.
'''
'''
inventory = {
    "Apples": 10,
    "Oranges": 5,
    "Bananas": 8

}
'''

'''
while True :
    fruit = input("enter fruit name ")
    if fruit not in inventory :
        print("fruit not availble")
        continue
    qty = int(input("enter the qty "))
    if qty > inventory[fruit]:
        print("Insufficient stock")

    if qty <= inventory[fruit]:
        inventory[fruit] = inventory[fruit] - qty
        print(inventory)
    if inventory[fruit] == 0:
        del inventory[fruit]
        print(inventory)
    if  inventory[fruit]   

    inventory = {}

if not inventory:
    print("The dictionary is empty!")
else:
    print("The dictionary has items.")    
'''


   

    


#4. 

'''
If the number is divisible by both 4 and 6, print "SpecialFizzBuzz" and continue.
If the number is only divisible by 4, print "Fizz".
If the number is only divisible by 6, print "Buzz".
If the number is prime, print "Prime: <num>".
Use pass for numbers that are odd but not prime.
Stop the loop if the sum of printed numbers exceeds 500.
'''

'''


while True:
    x = eval(input("enter the number "))
    if (x % 4 ==0) & (x % 6 == 0) :
        print("SpecialFizzBuzz")
        continue
    elif x % 4 ==0 :
        print("Buzz")

    elif x % 6 ==0 :
        print("Fizz")  

    '''








#5.

'''
students = ["Eve", "John", "Alice", "Bob", "Charlie"]
scores = [85, 92, 78, 90, 95]
top_scorers = {"John", "Alice", "Charlie", "Zara"}
Write a program that:

Converts students and scores into a dictionary.
Uses a while loop to repeatedly ask the user for a student’s name and print their score.
If the name is not in the dictionary, print "Student not found" and continue.
If the student is in top_scorers, print "Top Scorer: <name>".
If the student’s score is below 80, print "Needs Improvement" and pass.
Stop the loop if "exit" is entered or after 3 valid queries.
'''

'''

students = ["Eve", "John", "Alice", "Bob", "Charlie"]
scores = [85, 92, 78, 90, 95]
top_scorers = {"John", "Alice", "Charlie", "Zara"}

s_scores = dict(zip(students, scores))
print(s_scores)

name = input("enter the name ")
if name in s_scores :
    print ('yes name is in dict' )
else:
    print ("not availble in dict")    

if name in top_scorers :
    print ('yes topname is in dict' )
else:
    print ("topname is not availble in dict")    
      

if scores < 80:
            print(f"Needs Improvement")
    

'''




'''
# 1. Function Overloading with Default and Keyword Arguments
Write a function calculate_total that calculates the total price of an order with the following conditions:

1 The function should take the following parameters:
price (required) – the price of a single item.
quantity (default value: 1) – number of items purchased.
discount (default value: 0%) – percentage discount applied to the total price.
tax (default value: 5%) – tax applied after the discount.

2 The function should return the final price after applying the discount and tax.

3 Call the function using:
Positional arguments
Keyword arguments
A mix of both

'''

'''

def cal_price(price =100 , qty = 2, discount = 0.10, tax = 0.08 ,final_price = 100 + 0.08 ):

    total_price = price * qty
    discount = 0.10 * total_price
    price = total_price - discount 
    tax = 0.08 * price
    final_price = price + tax

    print("total total_price :" , total_price  )
    print("total discount  :" , discount  )
    print("total price :" , price  )
    print("total tax  :" , tax  )
    print("total final_price  :" , final_price) 


cal_price ()    

 '''   

    

'''
 
2. Using *args and **kwargs in Function Calls
Write a function order_summary that takes an arbitrary number of arguments (*args) and keyword arguments (**kwargs):

*args contains a list of food items ordered.
**kwargs contains additional details such as:
table_number (default: 1)
waiter_name (default: "Unknown")
The function should print the ordered items, the table number, and the waiter's name.

'''
'''
def  order_food(*foods, table_number=1, waiter_name="Unknown", **details):
    print ("\n food_details")
    print(foods)
    print("\n addition_details") 

    print(f"Table Number: {table_number}")
    print(f"Waiter Name: {waiter_name}")   
    for  key , value  in details.items() :
        print(f"{key}:{value}")


order_food("pizza","veg briyani" , table_number = 7 , waiter_name = "rahul" )


'''


'''
3. Modifying a Global Variable Inside a Function
You have a global variable counter = 0.

Write a function increment_counter() that:
Uses the global keyword to modify counter.
Increases counter by 5 on each function call.
Returns the updated value.
Call the function three times and print the value of counter after each call.

'''

'''
c=0
def counter(*n):
    global c
    c = c + 5
    return c
print(counter())    
print(counter())
print(counter())
'''




'''
4. Using nonlocal Inside Nested Functions
Write a function outer() that has:

A nested function inner() that modifies a variable using nonlocal.
A variable x = 10 inside outer().
The inner() function should:
Increase x by 5 using nonlocal.
Print "Inside inner: x = <value>".
The outer() function should:
Call inner().
Print "Inside outer: x = <value>".

'''

'''

def outer():
    x=20 
    def inner():
        nonlocal x 
        x += 5
        print(x)
    inner()    
    inner()  
    inner()  
outer() 

'''



'''
5. Complex Function Combining All Concepts
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

print(process_data(1, 2, 3, 4, operation="sum", double=True))  
print(process_data(5, 6, 7, 8, operation="product"))  
print(process_data(10, 20, 30, operation="max", double=True))  

'''

def process_data(*item, operation="sum" , double=True):

    items = item

    if operation == "sum":
        aggs = sum(items)

    if operation == "product":
        c = 1
        for i in items:
            c = c * i
        
        aggs = c

    if double :
        print(2 * aggs)

    else:
        print(aggs)


process_data(1, 2, 3, 4,)










