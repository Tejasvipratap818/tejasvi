#1. 

'''
You are given a list of employee names:

employees = ["John", "Alice", "Bob"]
Perform the following operations:


Insert "Grace" at index 2 and append "David" at the end.
Extend the list with ["Emma", "Liam"], but add them at index 1.
Convert the final list into a single string where each name is separated by " | " (using .join()).
Reverse the final list and print only the first three names from it.
What is the final reversed list, and what are the first three names?

'''


employees = ["John", "Alice", "Bob"]
employees.insert(2 , 'grace' )
print(employees)

employees = ["John", "Alice", "Bob"]
employees.append('david')
print(employees)

employees = ["John", "Alice", "Bob"]
emp = ["Emma", "Liam"]
employees [1:1] = emp
print(employees)

employees = ["John", "Alice", "Bob"]
emp = " | ".join(employees)
print(emp)

employees = ["John", "Alice", "Bob"]
print(employees)


employees = ["John", "Alice", "Bob","durga" , "carem"]
employees.reverse() 
print(employees[:4])

#2. 

'''
You have the following 3×3 matrix representing sales data for three stores over three months:

sales_data = [
    [1200, 1500, 1700],  
    [1100, 1450, 1800],  
    [1050, 1600, 1750]  
]
Perform the following operations:

Unpack the first row into three variables and print their product.
Convert the matrix into a flattened list using list comprehension.
Find the sum of diagonal elements (from top-left to bottom-right).
Replace all values below 1500 with "Low" and all values above 1700 with "High".
What is the final modified matrix?
'''
sales_data = [
    [1200, 1500, 1700],  
    [1100, 1450, 1800],  
    [1050, 1600, 1750]  
]
r1 , r2 , r3 = sales_data 
print(r1) 

sales_data = [
    [1200, 1500, 1700],  
    [1100, 1450, 1800],  
    [1050, 1600, 1750]  
]
sales_data = [m for data in sales_data for m in data]
print(sales_data)

sales_data = [
    [1200, 1500, 1700],  
    [1100, 1450, 1800],  
    [1050, 1600, 1750]  
]
data=  sum( sales_data[i][i] for i in range(3))
print(data)

sales_data = [
    [1200, 1500, 1700],  
    [1100, 1450, 1800],  
    [1050, 1600, 1750]  
]

for s in sales_data:
    for e in s :
        if e< 1500:
            print("low" , end = " ")
            
        elif e > 1750 :
           
           print("high" , end = " " )
        else : 
            print(e , end =" " )
    print()   
           


#3. 

'''
A company tracks employee performance using a nested dictionary: 

performance = {
    "Alice": {"Q1": 78, "Q2": 85, "Q3": 90},
    "Bob": {"Q1": 88, "Q2": 92, "Q3": 85},
    "Charlie": {"Q1": 70, "Q2": 75, "Q3": 80}
}
Perform the following operations:

Add a new employee "David" with scores { "Q1": 82, "Q2": 87, "Q3": 89 }.
Find the employee with the highest Q3 score.
Calculate the average Q2 score of all employees.
Convert the dictionary into a flat dictionary where keys are in the format "Employee_Qx" (e.g., "Alice_Q1": 78).
What is the flattened dictionary, and who has the highest Q3 score?
'''

performance = {
    "Alice": {"Q1": 78, "Q2": 85, "Q3": 90},
    "Bob": {"Q1": 88, "Q2": 92, "Q3": 85},
    "Charlie": {"Q1": 70, "Q2": 75, "Q3": 80}
}

performance["david"] = {"Q1": 82, "Q2": 87, "Q3": 89}
print(performance)

qmx = max(pr["Q3"] for pr in  performance.values () )
print(qmx)


performance = {
    "Alice": {"Q1": 78, "Q2": 85, "Q3": 90},
    "Bob": {"Q1": 88, "Q2": 92, "Q3": 85},
    "Charlie": {"Q1": 70, "Q2": 75, "Q3": 80}
}

q2s = [ p["Q2"]  for p in performance.values ()   ]  
print(q2s)

s = sum(q2s)
print(s)

ln = len(q2s) 
print(ln)

avg = sum(q2s) / len(q2s) 
print(avg )                       # Calculate the average Q2 score of all employees.

q2s = sum([  p["Q2"]  for p in performance.values ()   ] )/len(performance.values ())
print(q2s)

performance = {
    "Alice": {"Q1": 78, "Q2": 85, "Q3": 90},
    "Bob": {"Q1": 88, "Q2": 92, "Q3": 85},
    "Charlie": {"Q1": 70, "Q2": 75, "Q3": 80}
}

for name , score in performance.items():
    for q , score in score.items():
        print(f"{name}_{q} -> {score} ")

performance = {
    "Alice": {"Q1": 78, "Q2": 85, "Q3": 90},
    "Bob": {"Q1": 88, "Q2": 92, "Q3": 85},
    "Charlie": {"Q1": 70, "Q2": 75, "Q3": 80}
}

ft = {f"{name}_{q}": score for name, score in  performance.items() for q ,score in score.items()}
#ft = {f"{name}_{q}": score for name, scores in performance.items() for q, score in scores.items()}

print(ft)
 
 


#4. 

'''
You are given two sets representing completed and pending project tasks:

completed_tasks = {"Task1", "Task2", "Task4", "Task6", "Task8"}
pending_tasks = {"Task3", "Task4", "Task5", "Task6", "Task7"}
Perform the following operations:

Find tasks that are completed but were never pending.
Find tasks that are in both sets (completed and pending).
Find tasks that are either pending or completed but not both.
After a new task "Task9" is completed, update completed_tasks and find the total number of unique tasks.
What are the results of these operations?
'''

completed_tasks = {"Task1", "Task2", "Task4", "Task6", "Task8"}
pending_tasks = {"Task3", "Task4", "Task5", "Task6", "Task7"}

result = completed_tasks.difference(pending_tasks)
print(result)

result = completed_tasks.intersection(pending_tasks)
print(result)

result1 = completed_tasks.union(pending_tasks).difference(completed_tasks.intersection(pending_tasks))
print(result)

completed_tasks.update(["Task9"])
print(completed_tasks)

result = completed_tasks.union(pending_tasks)
print(result)

result = len(completed_tasks.union(pending_tasks))
print(result)

#5. 

'''
You are given data about students and their marks:

students = ["Eve", "John", "Alice", "Bob", "Charlie"]
marks = [85, 92, 78, 90, 95]
top_scorers = {"John", "Alice", "Charlie", "Zara"}
Perform the following operations:


Convert students and marks into a dictionary.
Find students who are in both the dictionary and top_scorers (intersection).
Find students who are in top_scorers but not in the dictionary (difference).
Sort the dictionary by marks in descending order and return the top two students.
'''

students = ["Eve", "John", "Alice", "Bob", "Charlie"]
marks = [85, 92, 78, 90, 95]
top_scorers = {"John", "Alice", "Charlie", "Zara"}



s_marks = dict(zip(students , marks ))
print(s_marks)

result = set(students).intersection(top_scorers)
print(result)

result = set(students).difference(top_scorers)
print(result)

sorted_list = sorted(s_marks.items(), key=lambda x: x[1] , reverse=True)
top_2_students = sorted_list[:2]
print(top_2_students)
