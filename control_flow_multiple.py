#Course Admission Criteria tool

#1. If Age > 18 then you are eligible
# 2. If Age < 65 then you are eligible
# 3. Not eligible


age=int(input("Enter Age : "))
#if age >= 18 and age <= 65
if 18 <= age <= 65:
    print("Eligible")
else:
    print("Not Eligible")