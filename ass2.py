print("lets get started")
x = 7
y = 15
xy = x - y
print(xy)

# Question 2
Age = 20
Name = "Ali"
print(f"{Name} is {Age} Years Old")

# QUESTION 3
entry = input("what is your Name:? ").upper()
print(entry)

# Question 5
total_bill = float(input("What is the Total Bill?: "))
people = 25
result = total_bill / people
print(f"Each person is earning {result}")

# Question 6
length = "What a Day"
print(len(length))
print(length[0])
print(length[9])

# Question 7
length = float(input("what is the length of a rectangle?: "))
width = float(input("what is the width of a rectangle?: "))
area = length * width
print(area)

# Question 8
student = input("Are you student (yes/no)?: ")
print(student)

# Question 9
number = int(input("input a number?: "))
f_division = number // 2
modulus = number % 2
print(f_division)
print(modulus)

# Question 10
named = input("what is your name?: ").title()
age_d = int(input("How old are you?: "))
country = input("what country are you from?: ").capitalize()
info = f"my name is {named} i am {age_d} years old, and i am from {country}"
print(info)