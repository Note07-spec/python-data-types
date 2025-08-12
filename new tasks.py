print("start task")

# Question 1
f_name = input("what is your firstname?: ").strip()
l_name = input("what is your lastname?: ").strip()
print(f"welcome {f_name} {l_name}, to python programming")

# Question 2
days = int(input("How many days?: "))
seconds = days * 24 * 60 * 60
print(seconds)

# Question 3
hello = input("say hello?: ")
world = input("say world?: ")
print(f"{world} {hello}")

# Question 4
word = input("write a word?: ")
num = int(input("write a number?: "))
result = word * num
print(f" {result}")

# Question 5
length = input("write a sentence?: ")
first_r = len(length)
second_r = len(length.replace(" ", ""))
print(first_r)
print(second_r)

# Question 6
int_1 = input("write a number?: ")
int_2 = input("write a number again?: ")
check = int_1 + int_2
print(check)

# Question 7
num_1 = int(input("input first number?: "))
num_2 = int(input("input second number?: "))
num_3 = int(input("input third number?: "))
avg = num_1 + num_2 + num_3 / 3
print(f"{avg :.2f}")

# Question 8
mins = float(input("how many minutes?: "))
hours = mins / 60
print(hours)

# Question 9
fullname = input("what is your full name?: ").title()
print(fullname)

# Question 10
# symbol_1 = input("write a symbol?: ")
# pattern_1 = int(input("write a number?: "))
# answer_1 = symbol_1 * pattern_1
# symbol_2 = input("write a symbol?: ")
# pattern_2 = int(input("write a number?: "))
# answer_2 = symbol_2 * pattern_2
# symbol = input("write a symbol?: ")
# pattern = int(input("write a number?: "))
# answer = symbol * pattern
# print(f"{answer_1}\n {answer_2}\n {answer}")