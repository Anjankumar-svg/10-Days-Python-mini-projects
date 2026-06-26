ur_year=int(input("Enter your birth year: "))
present_year=2026
age=present_year-ur_year
print("Your age is:", age)
if age<18:
    print("You are a child.")
elif age>=18 and age<65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
