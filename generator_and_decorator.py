#1.

'''
Write a decorator called log_generator that:

Wraps any generator function.
Logs the value being yielded each time.
Returns the original generator’s output. 

✅ Example:

@log_generator
def number_sequence(n):
    for i in range(1, n + 1):
        yield i

gen = number_sequence(5)
for num in gen:
    print(num)
✅ Expected Output:

Yielding: 1
1
Yielding: 2
2
...
Yielding: 5
5
How would you track each value yielded without interrupting the generator's flow?

'''
# def log_generator (func):
#     def wrap(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         for value in gen:
#             print(f"Yielding: {value}") 
#             yield  value
#     return wrap
          

# @log_generator
# def number_sequence(n):
#     for i in range(1, n + 1):
#         yield i

# gen = number_sequence(5)
# for num in gen:
#     print(num)

        
   



#2. 

'''
Create a generator fibonacci() that yields numbers from the Fibonacci sequence.
Create a decorator limit_output(n) that stops the generator after n values.
✅ Example:

python

@limit_output(7)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for num in fibonacci():
    print(num)
✅ Expected Output:


0
1
1
2
3
5
8
How would you control a generator’s output using a decorator?
'''
# def limit_output(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             gen = func(*args, **kwargs)  
#             for i in range(n):  
#                 yield next(gen)  
#         return wrapper
#     return decorator
# def limit_output(func):
#     def wrapper(*args, **kwargs):
#         gen = func(*args, **kwargs)  # Call the generator function
#         limit = 7  # Hardcoded limit of 7 values
#         for i in range(limit):
#             yield next(gen)  # Yield the next value from the generator
#     return wrapper
# @limit_output(7)
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# for num in fibonacci():
#     print(num)

# def limit_output(func):
#     def wrapper(*args, **kwargs):
#         gen = func(*args, **kwargs)  # Call the generator function
#         limit = 7  # Hardcoded limit of 7 values
#         for i in range(limit):
#             yield next(gen)  # Yield the next value from the generator
#     return wrapper

# @limit_output
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# for num in fibonacci():
#     print(num)
#3. 

'''
Create two decorators:
double_output – Multiplies every yielded value by 2.
filter_even – Filters and yields only even numbers.
Use them to decorate a generator that yields numbers from 1 to 10.
✅ Example:


@double_output
@filter_even
def numbers():
    for i in range(1, 11):
        yield i

for num in numbers():
    print(num)
✅ Expected Output:
4
8
12
16
20
In which order do the decorators execute, and why does it matter?
'''

# Decorator to multiply the output by 2
# def double_output(func):
#     def wrapper(*args, **kwargs):
#         for value in func(*args, **kwargs):
#             yield value * 2
#     return wrapper

# # Decorator to filter even numbers
# def filter_even(func):
#     def wrapper(*args, **kwargs):
#         for value in func(*args, **kwargs):
#             if value % 2 == 0:
#                 yield value
#     return wrapper

# @double_output
# @filter_even
# def numbers():
#     for i in range(1, 11):
#         yield i

# # Testing the code
# for num in numbers():
#     print(num)


#4. 

'''
Write a generator prime_numbers() that yields prime numbers.
Write a decorator cache_last(n) to cache the last n values yielded.
Provide a method .get_cache() to retrieve the cached values.
✅ Example:


@cache_last(3)
def prime_numbers():
    n = 2
    while True:
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            yield n
        n += 1

gen = prime_numbers()
for _ in range(5):
    print(next(gen))

print(gen.get_cache())
✅ Expected Output:
  
2
3
5
7
11
[5, 7, 11]
How can you maintain generator state across multiple iterations?
'''




#5. 

'''
Create a generator large_sum(n) that yields cumulative sums from 1 to n.
Write a decorator time_it that:
Measures the execution time for each yield.
Prints the time taken between yields.
✅ Example:

@time_it
def large_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        yield total

for value in large_sum(5):
    print(value)
✅ Expected Output (approximate times):

Time taken: 0.00001s
1
Time taken: 0.00002s
3
...
15
How do you measure the time between consecutive yield statements?
'''