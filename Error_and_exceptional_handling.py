#1. 

'''
Create a custom exception hierarchy:
BankError: Base class for bank-related errors.
InsufficientFundsError: Raised when withdrawal exceeds balance.
InvalidAmountError: Raised when the amount is negative.
Implement a BankAccount class:
deposit(amount): Raises InvalidAmountError if amount ≤ 0.
withdraw(amount): Raises InsufficientFundsError if insufficient balance.
✅ Example:

acc = BankAccount(1000)
try:
    acc.withdraw(2000)
except BankError as e:
    print(f"Error: {e}")
✅ Expected Output:

Error: Insufficient funds
How do you design a hierarchy of custom exceptions?
'''
# class BankError(Exception):
#     pass

# class InvalidAmountError(BankError):
#     pass
# class InsufficientFundsError(BankError):
#     pass 

# class BankAccount :
#     def __init__(self , balance):
#         self.balance=balance

#     def withdraw (self , amount):
#             if amount>self.balance:
#                 raise InsufficientFundsError(f"InsufficientFunds: {self.balance}")
#             self.balance -= amount
#             print(f"{amount} reminig balance {self.balance}")

#     def deposite(self , amount):
#           if amount <=0:
#                raise InvalidAmountError(f" InvalidAmount :  {self.balance}") 
#           self.balance += amount
#           print(f"{amount} and updtate balance{self.balance}")

# acc = BankAccount(1000)
# try:
#     acc.withdraw(2000)
# except BankError as e:
#     print(f"Error: {e}")
# finally :
#      print("complete withdraw")
# try:
#      acc.deposite(-500) 
# except   BankError as e :
#      print(f"error: {e}")   
# finally:
#      print("complete deposite ")       





#2. 

'''
Write a function safe_divide(a, b) that:
Raises ZeroDivisionError if b == 0.
Raises TypeError if inputs are not numbers.
Handle the function call with:
Multiple except blocks for specific exceptions.
else to print the division if no error occurs.
finally to print "Operation Complete".
✅ Example:

try:
    print(safe_divide(10, 0))
except Exception as e:
    print(e)
✅ Expected Output:

division by zero
Operation Complete
What is the purpose of else and finally in error handling?
'''

# def safe_divide(a, b):

#     try :
#          result = a / b 
#     except ZeroDivisionError:
#          print(" divide by zero  ")
         
#     except TypeError :
#          print("input only int")  
         
#     else :
#          print("succesfully" , result) 
#          return result
#     finally:
#         print("Operation Complete")
        
        

# s = safe_divide(10, 0)

# try:
#     print(safe_divide(10, 0))  
# except Exception as e:
#     print(e)            


#3. 

'''
Write a function process_data() that:
Catches ValueError and logs "Invalid value!".
Re-raises the error after logging.
Call process_data() in another function main() and:
Handle the re-raised ValueError.
Print "Error handled in main()".
✅ Example:

try:
    main()
except ValueError:
    print("Error handled in main()")
✅ Expected Output:

Invalid value!
Error handled in main()
Why might you re-raise exceptions, and how do you do it?
'''

# def process_data():
#      try :
#           value = int("invailid data")
#      except ValueError :
#           print("invalid value")  
            

# def main():
#      try:
#          process_data()
#      except ValueError:
#            print("Error handled")  


# main()

# try:
#     main()
# except ValueError:
#     print("Error handled in main()")

              

              


#4. 

'''
Create a custom context manager FileHandler:
Open a file in __enter__().
Close the file in __exit__() (even if an exception occurs).
Handle FileNotFoundError gracefully while logging "File not found".
✅ Example:

with FileHandler("missing.txt", "r") as f:
    content = f.read()
✅ Expected Output:

File not found
How do you ensure resources are cleaned up even during exceptions?
'''

# class FileHandler:
#      def __init__(self , file_name , mode):
#           self.file_name=file_name
#           self.mode=mode

#      def __enter__(self):
               


#5. 

'''
Write a function validate_password(password) that:
Raises ValueError if the password is less than 8 characters.
Raises TypeError if the input is not a string.
Include custom error messages in each exception.
✅ Example:

try:
    validate_password(12345)
except Exception as e:
    print(e)
✅ Expected Output:

Password must be a string.
Why should you provide custom messages when raising exceptions?
'''

def validate_password(password):
         if type(password) is not str:
    
            raise TypeError("plese write str ")
         if len(password)<8:
            raise ValueError("password is less than 8 characters")

v= validate_password(12345) 
try:
    validate_password(12345)
except Exception as e:
     print(e)