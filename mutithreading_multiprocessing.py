#1. Thread Synchronization with Locks

'''
Create a shared Counter class with:
A count attribute (starting at 0).
A increment() method that increases count by 1.
Start 5 threads where each thread increments the counter 100,000 times.
Use a Lock to ensure thread safety.
✅ Example Output (Expected Total Count):

Final count: 500000
'''


#2. Producer-Consumer Problem with Threads

'''
Implement the Producer-Consumer problem using:
Threads and a Queue.
One producer thread (generating 50 random numbers).
Two consumer threads (removing and processing numbers).
Ensure synchronization using thread-safe queues.
✅ Expected Output (varies due to randomness):

Producer added: 42
Consumer processed: 42
'''



#3. Parallel Factorial Calculation with Multiprocessing

'''
Write a function factorial(n) that calculates the factorial of a number.
Use multiprocessing.Pool to compute the factorial of numbers in a list in parallel.
Ensure results are printed in order.
✅ Example Input:

factorials([5, 10, 15])
✅ Expected Output:

120, 3628800, 1307674368000
'''


#4. Sharing Data Between Processes

'''
Use multiprocessing.Manager to share a list between processes.
Start 3 processes:
Each process adds 10 random numbers to the shared list.
Ensure all processes complete and print the final list.
✅ Expected Output (varies due to randomness):

Final list: [12, 45, ..., 89]
'''


#5. Mixed Thread and Process Execution

'''
Create a hybrid task:
Use multiprocessing to launch 3 processes.
Each process runs a function that starts 2 threads.
Each thread should:
Simulate work by sleeping for a random time.
Print when the task starts and ends.
✅ Expected Output (in random order due to concurrency):

Process 1, Thread A: Started
Process 1, Thread A: Completed
'''