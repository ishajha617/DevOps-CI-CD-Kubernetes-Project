#loop :- Loops ka use tab hota hai jab hume kisi task ko baar-baar repeat karna ho bina code ko multiple times likhe.

# 1. for Loop
# for loop ka use tab karte hain jab hume pata ho kitni baar loop chalana hai.

# Syntax

# for variable in sequence:
#     code

# Example 1
# for i in range(5):
#     print(i)

# Har value i me store hoti hai aur print hoti hai.

# Example 2
# for i in range(-1, 5):
#     print(i)

# Example 3 (Table)
# num = 5

# sum = 5
# for i in range(1, 11):
#     print("sum:-", sum, "x", i, "=", sum * i)
    
# range() Function
# 1 Parameter
# range(5)

# 2 Parameters
# range(2,8)

# 3 Parameters
# range(2,11,2)

# Real-Time Example
# Student Attendance

# students = ["Rahul","Isha","Aman"]

# for student in students:
#     print(student)

# 2. while Loop
# Jab hume nahi pata ki loop kitni baar chalega tab while use karte hain.
# Condition True rahegi tab tak loop chalta rahega.

# Syntax

# while condition:
#     code

# Example
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Infinite Loop
# while True:
#     print("Hello")

# Ye kabhi stop nahi hoga.
# Isliye break lagana zaruri hai.

# Real-Time Example
# Password Verification

# password = ""

# while password != "admin123":
#     password = input("Enter Password: ")

# print("Login Successful")

# 3. Nested Loop
# Loop ke andar loop ko Nested Loop kehte hain.

# for i in range():
#     for j in range():
#         code

# Example

# for i in range(3):
#     for j in range(3):
#         print(i,j)

# Star Pattern

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# Triangle Pattern
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# 4. break Statement
# Loop ko turant stop karne ke liye use karte hain.
# Example
# for i in range(1,11):

#     if i == 6:
#         break

#     print(i)

# Real-Time Example
# ATM PIN Verification

# correct_pin = 1234

# for attempt in range(3):

#     pin = int(input("Enter PIN: "))

#     if pin == correct_pin:
#         print("Login Successful")
#         break

#     print("Wrong PIN")

# 5. continue Statement
# Current iteration skip karta hai.
# Loop stop nahi hota.

# for i in range(1,11):

#     if i == 5:
#         continue

#     print(i)

# Even Numbers Example

# for i in range(1,11):

#     if i % 2 != 0:
#         continue

#     print(i)

# 6. pass Statement
# pass kuch nahi karta.
# Placeholder hota hai.
# Future me code likhne ke liye use karte hain.

# for i in range(5):

#     if i == 3:
#         pass

#     print(i)

# Function Example
# def student_data():
#     pass

# Error nahi aayega.
# Baad me code likh sakte hain.

# Mini Project - Student Marks System

# students = 3

# for i in range(students):

#     name = input("Enter Name: ")
#     marks = int(input("Enter Marks: "))

#     if marks < 0:
#         continue

#     if marks >= 90:
#         grade = "A"

#     elif marks >= 75:
#         grade = "B"

#     elif marks >= 50:
#         grade = "C"

#     else:
#         grade = "Fail"

#     print(name, "Grade:", grade)

# ATM System Mini Project (While Loop + Input + Nested Conditions)
# Ye project beginner se intermediate level ka hai aur isme:

# ✅ Variables
# ✅ Input Function
# ✅ While Loop
# ✅ Nested Conditions
# ✅ Break
# ✅ Menu Driven Program
# ✅ Balance Check
# ✅ Deposit
# ✅ Withdraw
# ✅ Exit

# Use kiya gaya hai.

# pin = "1234"
# balance = 10000

# print("===== Welcome to ATM =====")

# # PIN Verification
# while True:

#     user_pin = input("Enter ATM PIN: ")

#     if user_pin == pin:

#         print("Login Successful")

#         while True:

#             print("\n===== ATM MENU =====")
#             print("1. Check Balance")
#             print("2. Deposit Money")
#             print("3. Withdraw Money")
#             print("4. Exit")

#             choice = input("Enter Choice: ")

#             # Check Balance
#             if choice == "1":
#                 print("Current Balance:", balance)

#             # Deposit
#             elif choice == "2":

#                 amount = float(input("Enter Deposit Amount: "))

#                 if amount > 0:
#                     balance = balance + amount
#                     print("Deposit Successful")
#                     print("Updated Balance:", balance)

#                 else:
#                     print("Invalid Amount")

#             # Withdraw
#             elif choice == "3":

#                 amount = float(input("Enter Withdraw Amount: "))

#                 if amount <= balance:

#                     if amount > 0:
#                         balance = balance - amount
#                         print("Please Collect Cash")
#                         print("Remaining Balance:", balance)

#                     else:
#                         print("Invalid Amount")

#                 else:
#                     print("Insufficient Balance")

#             # Exit
#             elif choice == "4":
#                 print("Thank You For Using ATM")
#                 break

#             else:
#                 print("Invalid Choice")

#         break

#     else:
#         print("Wrong PIN")


# Advanced ATM System (3 Attempts + Nested Conditions)

# correct_pin = "1234"
# balance = 5000
# attempt = 0

# while attempt < 3:

#     pin = input("Enter ATM PIN: ")

#     if pin == correct_pin:

#         print("Login Successful")

#         while True:

#             print("\n===== ATM MENU =====")
#             print("1. Balance Inquiry")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Fast Cash")
#             print("5. Exit")

#             choice = input("Enter Choice: ")

#             if choice == "1":
#                 print("Available Balance:", balance)

#             elif choice == "2":

#                 amount = int(input("Enter Deposit Amount: "))

#                 if amount > 0:
#                     balance += amount
#                     print("Amount Deposited Successfully")
#                     print("New Balance:", balance)

#                 else:
#                     print("Invalid Amount")

#             elif choice == "3":

#                 amount = int(input("Enter Withdraw Amount: "))

#                 if amount > 0:

#                     if amount <= balance:
#                         balance -= amount
#                         print("Withdrawal Successful")
#                         print("Remaining Balance:", balance)

#                     else:
#                         print("Insufficient Balance")

#                 else:
#                     print("Invalid Amount")

#             elif choice == "4":

#                 print("1. 500")
#                 print("2. 1000")
#                 print("3. 2000")

#                 fast_cash = input("Select Amount: ")

#                 if fast_cash == "1":

#                     if balance >= 500:
#                         balance -= 500
#                         print("Collect ₹500")
#                     else:
#                         print("Insufficient Balance")

#                 elif fast_cash == "2":

#                     if balance >= 1000:
#                         balance -= 1000
#                         print("Collect ₹1000")
#                     else:
#                         print("Insufficient Balance")

#                 elif fast_cash == "3":

#                     if balance >= 2000:
#                         balance -= 2000
#                         print("Collect ₹2000")
#                     else:
#                         print("Insufficient Balance")

#             elif choice == "5":
#                 print("Thank You")
#                 break

#             else:
#                 print("Invalid Option")

#         break

#     else:
#         attempt += 1
#         print("Wrong PIN")
#         print("Remaining Attempts:", 3 - attempt)

# if attempt == 3:
#     print("Card Blocked")

# Concepts Used
# Concept	Used
# while loop	PIN verification & menu
# nested while	ATM menu
# nested if	Withdraw & Fast Cash
# input()	User interaction
# variables	Balance, PIN
# break	Exit ATM
# condition	Validation 
# arithmetic operators	Deposit & Withdraw


# name = input("enter your name:- ")
# age = input("enter your age:- ")
# phone =input("enter your number :- ")

# if name == "isha":
#     if age == "23":
#         if phone == "88172690":
#             print("welcome")
#         else:
#             print("wrong number")
#     else:
#         print("wrong age")
# else:
#     print("wrong name")
# print("welcome to our side")


# name= input("ENTER your NAME:- ")
# age= int(input("enter your age:- "))
# acc_number=int(input("enter your acc no:- "))
# if name == "rao":
#     print("welcome rao")
# else:
#     print("wrong name")
# if age == 19:
#     print("welcome")
# if acc_number == 000000:
#     print =("next")
# else:
#     print = ("wrong accno")




# a = range(10)
# for i in a:
#     print(i)
# for i in range(5):
#     print(i)


 
 