print("lets get it")

name = "Ajileye Abdulrahman"
Age = 20
is_student = bool(input("Are you a student?: (True/False) "))
print(f"My name is {name} I am {Age} Years old Student status: {is_student}")

# # Question No 2
Age_d = int(input("what is your Age?: "))
Height = float(input("What is your height?: "))
result = type(Age_d),
another = type(Height),
print(f"{result} {another}")

# Question 3
current_year = 2025
birth_Year = int(input("What is your birth year?: "))
actual_age = current_year - birth_Year
print(actual_age)

# Question 4
name_id = input("What is your Fullname?: ")
score = float(input("What is your score out of 100?: "))
if_passed = input("Did you pass (YES/NO)?: ")
print(f"My Name is {name_id} My score is {score} and did i pass {if_passed} the passed aggregate is 50")

# Question 5
weight = float(input("what is your weight?: "))
height_d = float(input("what is your Height?: "))
calc = weight/(height_d **2)

print(calc)
